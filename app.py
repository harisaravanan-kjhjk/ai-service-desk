import streamlit as st

from database.db import *
from auth.login import login_page
from auth.signup import signup_page
from pages.admin import admin_page
from pages.customer import customer_page
from pages.developer import developer_page
from utilities.logout import show_logout_sidebar
from pages.show_ticket import show_tickets
from pages.logger_page import logger_page
from pages.note import display_note
def main():

    init_db()
    if "curr_ticket" not in st.session_state:
        st.session_state.curr_ticket=None

    if "id" not in st.session_state:
        st.session_state.id=None

    if "messages" not in st.session_state:
        st.session_state.messages=[]
        
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "name" not in st.session_state:
        st.session_state.name = None

    if "role" not in st.session_state:
        st.session_state.role = None

    show_logout_sidebar()

    if not st.session_state.logged_in:

        st.title("Ticket Management System")

        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            login_page()

        with tab2:
            signup_page()

    else:

        if st.session_state.name == "admin":
            admin_page()

        elif st.session_state.role == "customer":
            customer_page()

        elif st.session_state.role == "developer":
            developer_page()

        elif st.session_state.role == "ticket":
            show_tickets()

        elif st.session_state.role == "logger_page":
            logger_page()
        elif st.session_state.role == "notes_page":
            display_note()

main()