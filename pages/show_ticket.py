from database.ticket_repository import *
from database.queue_repository import *
import streamlit as st

def show_tickets():

    col1, col2 = st.columns([9, 1])

    with col2:
        if st.button("<- Back"):

            st.session_state.role = "admin"
            st.session_state.selected = None
            st.session_state.dev_id = None

            st.rerun()

    st.subheader("Ticket Details")

    ticket = get_tickets(st.session_state.selected)

    st.write(f"### {ticket[1]}")
    st.write(f"Status: {ticket[2]}")

    if st.button("Assign", key="open_page"):

        assign_ticket(
            st.session_state.selected,
            st.session_state.dev_id
        )

        assign_from_queue(
            st.session_state.selected,
            st.session_state.dev_id
        )

        st.session_state.role = "admin"
        st.session_state.selected = None
        st.session_state.dev_id = None

        st.rerun()