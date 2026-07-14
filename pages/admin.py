import streamlit as st
from database.user_repository import *
from database.level_repository import *
from database.queue_repository import *
from utilities.logout import show_logout_sidebar
from pages.show_ticket import show_tickets
from database.ticket_repository import *
from pages.show_ticket import show_tickets
from database.recommendations import *
from agents.hints_agent import developer_guidance
from vector_store.similarity import recommend
from database.resolution_repository import debug_resolution
import json

def admin_page():
    st.title("Admin page")
    developers=get_developer()
    assigned_developer=assigned_devs()
    tab1,tab2,tab3=st.tabs(["pending admission","assigned devs","recommendations"])
    if assigned_developer is None:
        assigned_developer = []
    with tab1:
        st.subheader("Unassigned developers")
        for dev in developers:
            if dev[0] not in [d[0] for d in assigned_developer]:
                st.write(dev[1])
                name=dev[1]
                level=st.selectbox("levels",["level 1","level 2","level 3"],key=f"dev_{dev[0]}")
                specialization=st.selectbox("Specialization",
                             [  
        "Authentication",
        "Database",
        "Backend",
        "Frontend",
        "DevOps",
        "Other"
                ],key=f"spec_{dev[0]}")
                if specialization=="other":
                    specialization=st.text_input("Enter specialization")
                if st.button("Assign",key=f"bt_{name}"):
                    insert_level(dev[0],level,specialization)
                    st.rerun()
                st.divider()
    
    with tab2:
        st.subheader("Developer List")
        l1,l2,l3=st.tabs(["level-1","level-2","level-3"])
        col1,col2=st.columns([9,1])
        with l1:
            devs=get_dev_by_level("level 1")
            ticket=get_unassigned_tickets(1)
            ticket=[tic[0] for tic in ticket]
            for dev in devs:
                st.write(f"Name: {dev[1]}")
                st.write(f"Specialization: {dev[2]}")
                selected=st.selectbox("Ticket-id",ticket,key=f"l1_{dev[1]}")
                if selected:
                    if st.button("Assign",key=f"bt_{dev[1]}"):
                        assign_ticket(selected,dev[0])
                        assign_from_queue(selected,dev[0])
                        place_holder_ticket=get_tickets(selected)
                        note=developer_guidance(place_holder_ticket[1],place_holder_ticket[2],1)
                        st.write(note)
                        content=json.loads(note)
                        st.write(content)
                        add_note(selected,content)
                        st.rerun()
                st.divider()
        with l2:
            devs2 = get_dev_by_level("level 2")
            ticket2 = [tic[0] for tic in get_unassigned_tickets(2)]

            for dev in devs2:
                st.write(f"Name: {dev[1]}")
                st.write(f"Specialization: {dev[2]}")

                selected = st.selectbox(
                    "Ticket-id",
                    ticket2,
                    key=f"l2_{dev[1]}"
                )

                if selected:
                    if st.button(
                        "Assign",
                        key=f"bt_l2_{selected}_{dev[0]}"
                    ):
                        assign_ticket(selected, dev[0])
                        assign_from_queue(selected, dev[0])

                        ticket = get_tickets(selected)

                        note = developer_guidance(
                            ticket[1],
                            ticket[2],
                            2
                        )

                        add_note(selected, note)

                        st.rerun()

                st.divider()
        with l3:
            devs3 = get_dev_by_level("level 3")
            ticket3 = [tic[0] for tic in get_unassigned_tickets(3)]

            for dev in devs3:
                st.write(f"Name: {dev[1]}")
                st.write(f"Specialization: {dev[2]}")

                selected = st.selectbox(
                    "Ticket-id",
                    ticket3,
                    key=f"l3_{dev[1]}"
                )

                if selected:
                    if st.button(
                        "Assign",
                        key=f"bt_l3_{selected}_{dev[0]}"
                    ):
                        assign_ticket(selected, dev[0])
                        assign_from_queue(selected, dev[0])

                        ticket = get_tickets(selected)

                        note = developer_guidance(
                            ticket[1],
                            ticket[2],
                            3
                        )

                        add_note(selected, note)

                        st.rerun()

                st.divider() 
    with tab3:

        l1, l2, l3 = st.tabs(["Level 1", "Level 2", "Level 3"])

        def show_level(level, other_levels):

            tickets = get_unassigned_tickets(level)

            if not tickets:
                st.info("No tickets waiting at this level.")
                return

            for tic in tickets:

                ticket = get_tickets(tic[0])

                st.subheader(f"Ticket #{ticket[0]}")
                st.write(f"**Title:** {ticket[1]}")
                st.write(f"**Description:** {ticket[2]}")

                st.write("### Change Level")

                new_level = st.selectbox(
                    "Move to",
                    other_levels,
                    key=f"level_{ticket[0]}"
                )

                if st.button(
                    "Update Level",
                    key=f"update_{ticket[0]}"
                ):
                    update_queue(ticket[0], new_level)
                    st.success("Queue level updated.")
                    st.rerun()

                st.write("### AI Recommendations")

                recommendations = get_recommendations(ticket[0])

                if not recommendations:
                    recommend(ticket[0],get_category(ticket[0]),level)
                    st.rerun()
                else:

                    medals = {
                        1: "🥇",
                        2: "🥈",
                        3: "🥉"
                    }

                    for developer_id, rank, score in recommendations:

                        developer = get_by_id(developer_id)

                        st.write(
                            f"{medals.get(rank,'')} "
                            f"**{developer[0]}** "
                            f"(Score: {score:.3f})"
                        )

                st.divider()

        with l1:
            show_level(1, [2, 3])

        with l2:
            show_level(2, [1, 3])

        with l3:
            show_level(3, [1, 2])
     
