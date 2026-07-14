from collections import defaultdict
from vector_store.vector_store import ticket_collection
from database.ticket_repository import get_tickets
from database.level_repository import get_dev_by_level
from database.recommendations import (
    insert_recommendations,
    delete_recommendations,
)
from database.queue_repository import get_workload


def find_similar_tickets(title, description, n=30):

    query = f"""
Title:
{title}

Description:
{description}
"""

    return ticket_collection.query(
        query_texts=[query],
        n_results=n
    )


def group_by_developer(results):

    grouped = defaultdict(lambda: {
        "distances": [],
        "ratings": [],
        "level": None,
        "specialization": None,
    })

    metas = results["metadatas"][0]
    distances = results["distances"][0]

    for meta, dist in zip(metas, distances):

        dev = meta["developer_id"]

        grouped[dev]["distances"].append(dist)
        grouped[dev]["ratings"].append(meta.get("rating", 0) or 0)
        grouped[dev]["level"] = meta.get("level")
        grouped[dev]["specialization"] = meta.get("specialization")

    return grouped


def add_new_developers(grouped, level):

    developers = get_dev_by_level(f"level {level}")

    for dev in developers:

        dev_id = dev[0]

        if dev_id not in grouped:

            grouped[dev_id] = {
                "distances": [],
                "ratings": [],
                "level": level,
                "specialization": dev[2]
            }

    return grouped


def normalize_similarity(grouped):

    all_d = [
        d
        for g in grouped.values()
        for d in g["distances"]
    ]

    if all_d:
        mn = min(all_d)
        mx = max(all_d)

    scores = {}

    for dev, data in grouped.items():

        if not data["distances"]:

            similarity = 0
            rating = 0

        else:

            sims = []

            for dist in data["distances"]:

                if mx == mn:
                    sim = 1

                else:
                    sim = 1 - ((dist - mn) / (mx - mn))

                sims.append(sim)

            similarity = sum(sims) / len(sims)
            rating = (
                sum(data["ratings"])
                / len(data["ratings"])
            ) / 100

        scores[dev] = {
            "similarity": similarity,
            "rating": rating,
            "level": data["level"],
            "specialization": data["specialization"]
        }

    return scores


def apply_specialization(scores, category):

    BONUS = 0.15

    for dev in scores:

        if scores[dev]["specialization"] == category:

            scores[dev]["specialization_score"] = BONUS

        else:

            scores[dev]["specialization_score"] = 0

    return scores


def apply_workload(scores):

    workloads = {}

    max_load = 1

    for dev in scores:

        load = get_workload(dev)

        workloads[dev] = load

        max_load = max(max_load, load)

    for dev in scores:

        availability = 1 - (workloads[dev] / max_load)

        if workloads[dev] == 0:
            availability += 0.10

        availability = min(1, availability)

        scores[dev]["availability"] = availability

    return scores


def compute_final_scores(scores):

    ranking = []

    for dev, data in scores.items():

        final = (

            0.35 * data["similarity"]

            + 0.20 * data["rating"]

            + 0.15 * data["specialization_score"]

            + 0.30 * data["availability"]

        )

        ranking.append({

            "developer_id": dev,

            "score": round(final, 4)

        })

    ranking.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return ranking


def save_recommendations(ticket_id, ranking):

    delete_recommendations(ticket_id)

    for rank, item in enumerate(ranking[:3], start=1):

        insert_recommendations(

            ticket_id,

            item["developer_id"],

            rank,

            item["score"]

        )


def recommend(ticket_id, category, level):

    ticket = get_tickets(ticket_id)

    if ticket is None:
        return []

    results = find_similar_tickets(

        ticket[1],

        ticket[2],

        n=30

    )

    grouped = group_by_developer(results)

    grouped = add_new_developers(grouped, level)

    scores = normalize_similarity(grouped)

    scores = apply_specialization(scores, category)

    scores = apply_workload(scores)

    ranking = compute_final_scores(scores)

    save_recommendations(ticket_id, ranking)

    return ranking