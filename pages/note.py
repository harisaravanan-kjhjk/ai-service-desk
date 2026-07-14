import json
import streamlit as st
from database.ticket_repository import get_tickets

def display_note():
    st.header("Notes for devs")
    ticket=get_tickets(st.session_state.ticket_id)
    note = ticket[6]
    col1,col2=st.columns([9,1])
    with col2:
        if st.button("Back"):
            st.session_state.role="developer"
            st.rerun()
    if not note:
        st.write("No notes available.")
        return

    if isinstance(note, str):
        try:
            note = json.loads(note)
        except json.JSONDecodeError:
            st.write(note)
            return

    if isinstance(note, dict):
        for key, value in note.items():
            st.subheader(key.replace("_", " ").title())

            if isinstance(value, list):
                for item in value:
                    st.markdown(f"- {item}")
            else:
                st.write(value)
    else:
        st.write(str(note))
    

    