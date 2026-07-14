import streamlit as st

from utilities.hash import hash_password
from database.user_repository import get_user


def login_page():

    st.subheader("Login Page")

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        user = get_user(username)

        if user is None:
            st.error("No such user exists")

        elif user[2] != hash_password(password):
            st.error("Incorrect password")

        else:

            st.session_state.logged_in = True
            st.session_state.name = username
            st.session_state.role = user[3]

            st.rerun()