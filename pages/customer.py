from agents.customer_graph.graph import graph
import streamlit as st
from agents.customer_graph.create_initial_state import create_initial_state
from database.queue_repository import *
from database.ticket_repository import *
from database.user_repository import *



def customer_page():
    st.write(debug_queue())
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

        if "customer_state" not in st.session_state:

            st.session_state.customer_state = create_initial_state(
                get_by_name(st.session_state.name)[0]
            )

            st.session_state.customer_state["messages"].append({
                "role": "AI",
                "message": "Describe your problem."
            })

        state = st.session_state.customer_state

        for msg in state["messages"]:
            with st.chat_message(msg["role"]):
                st.write(msg["message"])

        prompt = st.chat_input(key="main_chat")

        if prompt:

            state["messages"].append({
                "role": "user",
                "message": prompt
            })

            with st.spinner("Thinking..."):
                state = graph.invoke(state)

            st.session_state.customer_state = state

            if state["response"]:

                state["messages"].append({
                    "role": "AI",
                    "message": state["response"]
                })

            if state["ticket_ready"]:

                if state["resolution_status"] == "resolved":

                    st.success("Issue solved successfully.")

                else:

                    st.success(
                        "Ticket created successfully and added to the queue."
                    )

                st.session_state.customer_state = create_initial_state(
                    get_by_name(st.session_state.name)[0]
                )

                st.session_state.customer_state["messages"].append({
                    "role": "AI",
                    "message": "Describe your problem."
                })

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