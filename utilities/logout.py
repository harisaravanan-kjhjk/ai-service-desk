import streamlit as st

def show_logout_sidebar():
    with st.sidebar:
        username = st.session_state.get("name", "Unknown User")
        st.write(f"Logged in as: {username}")

        if st.button("Logout", key=f"logout_button{st.session_state.name}"):
            st.session_state.clear()
            st.rerun()