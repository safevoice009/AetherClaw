import streamlit as st
import psutil

def render_system():
    st.subheader("📡 AetherClaw Telemetry")

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    col1, col2 = st.columns(2)
    with col1:
        st.metric("CPU Resonance", f"{cpu}%")
    with col2:
        st.metric("RAM Saturation", f"{ram}%")
    
    if cpu > 80:
        st.warning("High CPU load detected. AetherClaw throttle engaged.")