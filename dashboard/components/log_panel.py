import streamlit as st
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(BASE_DIR, "logs", "system.log")


def render_logs():

    st.subheader("Agent Activity")

    if not os.path.exists(LOG_FILE):
        st.write("No logs yet")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.readlines()[-30:]

    for line in logs:
        st.text(line.strip())