import json
import time

import streamlit as st

from agents.l1_agent import ask_l1_agent
from agents.prompt_repair_llm import fall_back_llm
from agents.triage_ticket import triage_ticket

from database.queue_repository import *
from database.ticket_repository import *
from database.user_repository import *

from utilities.logout import show_logout_sidebar


def customer_page():
    st.title("Customer Home Page")

    tab1, tab2 = st.tabs([
        "Create Ticket",
        "View Tickets"
    ])

    # -------------------------
    # Create Ticket
    # -------------------------
    with tab1:

        st.subheader("AI Assistant")

        if st.session_state.messages == []:
            st.session_state.messages = [{
                "role": "AI",
                "message": "Describe your problem."
            }]

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["message"])

        prompt = st.chat_input(key="main_chat")

        if prompt:

            st.session_state.messages.append({
                "role": "user",
                "message": prompt
            })

            with st.chat_message("AI"):
                with st.spinner("Thinking..."):
                    data = ask_l1_agent(
                        st.session_state.messages[-8:]
                    )

            try:

                content = json.loads(data)

                title = content["title"]
                description = content["inference"]

                if not content["ticket_ready"]:

                    st.session_state.messages.append({
                        "role": "AI",
                        "message": content["next_question"]
                    })

                else:

                    ticket_id = put_tickets(
                        title,
                        description,
                        get_by_name(st.session_state.name)[0],
                        "AI"
                    )

                    st.session_state.messages = []

                    if content["resolution_status"] == "resolved":

                        update_ticket(ticket_id, "resolved")

                        st.success(
                            "Issue solved successfully."
                        )

                    else:

                        queue_id = put_queue(ticket_id, 1)

                        with st.chat_message("AI"):
                            with st.spinner("Triaging ticket..."):

                                try:

                                    ticket = get_tickets(ticket_id)

                                    triage = json.loads(
                                        triage_ticket(
                                            ticket[1],
                                            ticket[2]
                                        )
                                    )

                                    assign_level_category_queue(
                                        queue_id,
                                        triage["level"],
                                        triage["category"]
                                    )

                                except Exception as e:
                                    st.error(e)
                                    time.sleep(10)

                        st.success("Ticket created successfully.")

            except Exception:

                # Fallback parser if the LLM returns malformed JSON
                st.write(data)

            st.rerun()

    # -------------------------
    # View Tickets
    # -------------------------
    with tab2:

        st.subheader("View Tickets")

        tickets = get_tickets_customer(
            st.session_state.name
        )

        for ticket in tickets:

            st.write(f"### {ticket[1]}")
            st.write(f"Status: {ticket[3]}")

            st.divider()