import streamlit as st
from database.resolution_repository import *
from database.ticket_repository import *
from database.user_repository import *
from pages.logger_page import logger_page
from database.resolution_repository import *

def developer_page():
    st.title("Developer Homepage")
    tab1,tab2,tab3=st.tabs(["active-tickets","tickets-in-progress","completed-tickets"])
    
    with tab1:
        tickets=get_assigned_by_category(get_by_name(st.session_state.name)[0],"open")
        for ticket in tickets:
            st.write(ticket[1])
            st.write(ticket[2])
            if st.button("View notes",key=f"tview1_{ticket[0]}"):
                st.session_state.role="notes_page"
                st.session_state.ticket_id=ticket[0]
                st.rerun()
            selected=st.selectbox("Status",["in-progress","resolved"],key=f"t1_{ticket[0]}")
            if selected:
                if st.button("Update_status",key=f"tb1_{ticket[0]}"):
                    if selected=="resolved":
                        update_ticket(ticket[0],selected)
                        st.session_state.curr_ticket=ticket[0]
                        st.session_state.role="logger_page"
                        st.rerun()
                    else:
                        update_ticket(ticket[0],selected)
                        st.rerun()
            st.divider()

    with tab2:
        tickets=get_assigned_by_category(get_name_by_id(st.session_state.name)[0],"in-progress")
        for ticket in tickets:
            st.write(ticket[1])
            st.write(ticket[2])
            if st.button("View notes",key=f"tview2_{ticket[0]}"):
                st.session_state.role="notes_page"
                st.session_state.ticket_id=ticket[0]
                st.rerun()
            selected=st.selectbox("Status",["resolved"],key=f"t2_{ticket[0]}")
            if selected:
                if st.button("Update_status",key=f"tb2_{ticket[0]}"):
                    if selected=="resolved":
                        update_ticket(ticket[0],selected)
                        st.session_state.curr_ticket=ticket[0]
                        st.session_state.role="logger_page"
                        st.rerun()
                    else:
                        update_ticket(ticket[0],selected)
                        st.rerun()
            st.divider()

    with tab3:
        tickets=get_assigned_by_category(get_name_by_id(st.session_state.name)[0],"resolved")
        for ticket in tickets:
            st.write(ticket[1])
            st.write(ticket[2])
            remark=get_details_for_dev_page(ticket[0],get_by_name(st.session_state.name)[0])
            if remark is None:
                update_ticket(ticket[0],"in-progress")
                st.rerun()
            st.write(f"rating: {remark[0]}")
            st.write(f"suggestions:{remark[1]}")
            if st.button("Update",key=f"tb3_{ticket[0]}"):
                st.session_state.curr_ticket=ticket[0]
                st.session_state.role="logger_page"
                st.rerun()
            st.divider()
    

