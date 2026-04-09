import streamlit as st
import os

PROJECT_DIR = "projects"

def render_projects():
    st.subheader("📁 AetherArchive: Active Projects")

    if not os.path.exists(PROJECT_DIR):
        st.info("AetherArchive is currently empty. Initialize a project to see it here.")
        return

    projects = [d for d in os.listdir(PROJECT_DIR) if os.path.isdir(os.path.join(PROJECT_DIR, d))]

    if not projects:
        st.info("No projects found in AetherArchive.")
        return

    for p in projects:
        with st.expander(f"📦 {p.upper()}"):
            st.write(f"Status: **Finalized**")
            st.write(f"Location: `/{PROJECT_DIR}/{p}`")