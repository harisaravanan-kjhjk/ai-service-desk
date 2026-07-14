import streamlit as st
from database.resolution_repository import *
from database.user_repository import *
from agents.evaluation_agent import evaluate_resolution
from database.ticket_repository import get_tickets
import json
from vector_store.resolution_vector_service import sync_resolution,sync_ticket
def logger_page():
    col1,col2=st.columns([9,1])
    with col2:
        if st.button("<- Back",key="back"):
            st.session_state.role="developer"
            st.rerun()
    st.title("logger page")
    st.write("Enter the summary of resolution: ")
    summary=st.text_area("summary",key="summary")
    st.write("Enter the root cause: ")
    root_cause=st.text_area("root cause",key="root")
    st.write("Enter the steps taken: ")
    steps_taken=st.text_area("steps_taken",key="steps")
    st.write("Verification methods taken: ")
    verification=st.text_area("verification",key="verification")
    if summary and root_cause and steps_taken and verification:
        if st.button("Assign",key="assign"):
            if not get_details_for_dev_page(st.session_state.curr_ticket,get_by_name(st.session_state.name)[0]):
                create_note(st.session_state.curr_ticket,get_by_name(st.session_state.name)[0],summary,root_cause,steps_taken,verification)
                sync_ticket(st.session_state.curr_ticket)
            else:
                update_note(st.session_state.curr_ticket,get_by_name(st.session_state.name)[0],summary,root_cause,steps_taken,verification)
            data=evaluate_resolution(get_tickets(st.session_state.curr_ticket)[2],summary,root_cause,steps_taken,verification)
            st.write(data)
            content=json.loads(data)
            try:
                rating=content["rating"]
                suggestion=content["suggestion"]
                update_rating(st.session_state.curr_ticket,get_by_name(st.session_state.name)[0],rating,suggestion)
                sync_resolution(st.session_state.curr_ticket,get_by_name(st.session_state.name)[0])
                st.session_state.role="developer"
                pass
            except Exception as e:
                st.exception(e)
            st.rerun()

    

