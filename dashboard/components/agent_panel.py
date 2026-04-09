import streamlit as st
import os

STATUS_FILE = "logs/agent_status.log"


def render_agents():
    st.subheader("🤖 Tactical Agent Swarm")

    if not os.path.exists(STATUS_FILE):
        st.info("Agent swarm is currently in hibernation.")
        return

    try:
        with open(STATUS_FILE, "r") as f:
            status_lines = f.readlines()
        
        if not status_lines:
            st.write("Idle")
            return

        # Display last 3 status updates in a stylized way
        latest_updates = status_lines[-3:]
        latest_updates.reverse()

        for line in latest_updates:
            icon = "⚡"
            if "Planner" in line: icon = "📋"
            elif "Developer" in line: icon = "💻"
            elif "Reviewer" in line: icon = "🔍"
            elif "Nexus" in line: icon = "🌌"
            
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.05); border-radius: 10px; padding: 10px; margin-bottom: 8px; border: 1px solid rgba(0, 242, 254, 0.1);">
                <span style="color: #00f2fe; margin-right: 10px;">{icon}</span>
                <span style="color: #f8f9fa; font-family: 'Inter', sans-serif; font-size: 0.9em;">{line.strip()}</span>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Error accessing agent telemetry: {e}")
