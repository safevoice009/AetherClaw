import streamlit as st
import os

STATUS_FILE = "../logs/agent_status.log"


def render_agents():

    st.subheader("Agent Status")

    if not os.path.exists(STATUS_FILE):
        st.write("No agent activity yet")
        return

    with open(STATUS_FILE) as f:
        lines = f.readlines()

    if lines:
        st.write(lines[-1])
    else:
        st.write("Idle")