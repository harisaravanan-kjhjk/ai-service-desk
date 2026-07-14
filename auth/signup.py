import streamlit as st

from utilities.hash import hash_password
from database.user_repository import (
    get_user,
    store_user
)


def signup_page():

    st.subheader("Welcome New User!")

    username = st.text_input(
        "Username",
        key="signup_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="signup_password"
    )

    r_password = st.text_input(
        "Repeat Password",
        type="password",
        key="signup_rpassword"
    )

    role = st.selectbox(
        "Role",
        ["developer", "customer"],
        key="signup_role"
    )

    if st.button("Register"):

        if get_user(username) is not None:
            st.error("User already exists")

        elif len(password) < 8:
            st.error("Password is too short")

        elif password != r_password:
            st.error("Passwords do not match")

        else:

            store_user(
                username,
                hash_password(password),
                role
            )

            st.session_state.logged_in = True
            st.session_state.name = username
            st.session_state.role = role

            st.rerun()