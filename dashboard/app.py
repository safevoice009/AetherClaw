import streamlit as st
import psutil
import os
import streamlit.components.v1 as components

from components.system_panel import render_system
from components.project_panel import render_projects
from components.agent_panel import render_agents
from components.log_panel import render_logs

st.set_page_config(page_title="AetherClaw | Strategic Control Center", layout="wide", page_icon="🌌")

# --- Advanced 3D WebGL Background (Digital Nebula) ---
three_js_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; background: transparent; }
        #canvas-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            background: radial-gradient(circle at 50% 50%, #0a0a1e 0%, #000000 100%);
        }
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.160.0/build/three.module.js"
            }
        }
    </script>
    <script type="module">
        import * as THREE from 'three';

        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);

        // Particle System for Nebula
        const particlesCount = 2000;
        const positions = new Float32Array(particlesCount * 3);
        const colors = new Float32Array(particlesCount * 3);
        const sizes = new Float32Array(particlesCount);

        for (let i = 0; i < particlesCount; i++) {
            positions[i * 3] = (Math.random() - 0.5) * 10;
            positions[i * 3 + 1] = (Math.random() - 0.5) * 10;
            positions[i * 3 + 2] = (Math.random() - 0.5) * 10;

            colors[i * 3] = Math.random() * 0.5 + 0.5; // R
            colors[i * 3 + 1] = Math.random() * 0.2; // G
            colors[i * 3 + 2] = Math.random(); // B

            sizes[i] = Math.random() * 0.05;
        }

        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));

        const material = new THREE.PointsMaterial({
            size: 0.05,
            vertexColors: true,
            transparent: true,
            opacity: 0.6,
            blending: THREE.AdditiveBlending
        });

        const points = new THREE.Points(geometry, material);
        scene.add(points);

        camera.position.z = 5;

        function animate() {
            requestAnimationFrame(animate);
            points.rotation.y += 0.001;
            points.rotation.x += 0.0005;
            renderer.render(scene, camera);
        }

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        animate();
    </script>
</body>
</html>
"""

components.html(three_js_html, height=0)

# World-Class Glassmorphism CSS (Premium Upgrade)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Outfit:wght@400;700&display=swap');
    
    .stApp {
        background: transparent;
        color: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: transparent;
    }
    
    .stSidebar {
        background: rgba(10, 10, 30, 0.75) !important;
        backdrop-filter: blur(25px);
        border-right: 1px solid rgba(0, 242, 254, 0.2);
    }
    
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        border: none;
        color: #0c0c0c;
        border-radius: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(0, 242, 254, 0.4);
        color: #ffffff;
    }
    
    [data-testid="stHeader"] { background: transparent; }
    
    /* Input styling */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Layout
col_header, col_logo = st.columns([5, 1])

with col_header:
    st.title("🌌 AetherClaw Hub")
    st.markdown("#### *Autonomous Strategic Intelligence Framework*")
    st.caption("Powered by the AetherFlow tri-agent loop")

with col_logo:
    # Look for the new 3D logo in assets or root
    logo_path = "assets/aetherclaw_logo.png" if os.path.exists("assets/aetherclaw_logo.png") else "dashboard/aetherclaw_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)

# Sidebar controls
st.sidebar.title("🛠️ Command Deck")
st.sidebar.markdown("---")

goal = st.sidebar.text_input("🎯 Define Objective", placeholder="Target project or research goal...")

if st.sidebar.button("🚀 IGNITE AETHERFLOW"):
    if goal:
        # Simulate command broadcast
        os.makedirs("../logs", exist_ok=True)
        with open("../logs/commands.log", "a") as f:
            f.write(f"BUILD:{goal}\n")
        st.sidebar.success(f"Objective '{goal[:20]}...' deployed.")
    else:
        st.sidebar.warning("Please specify an objective.")

if st.sidebar.button("🛑 SYSTEM PURGE"):
    with open("../logs/commands.log", "a") as f:
        f.write("STOP\n")
    st.sidebar.error("Halting all autonomous processes.")

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
**Status:** `OPERATIONAL`
**Resonance:** `OPTIMAL`
**Version:** `1.2.0-PRO`
""")

# Main Dashboard
col1, col2 = st.columns(2)

with col1:
    render_system()

with col2:
    render_agents()

st.markdown("---")
render_projects()
st.markdown("---")
render_logs()

# World-Class Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: rgba(255,255,255,0.3); padding: 40px; border-top: 1px solid rgba(255,255,255,0.05);'>"
    "AetherClaw Autonomous Ecosystem &copy; 2026<br>"
    "Engineering & Architecture by "
    "<a href='https://github.com/safevoice009' style='color: #00f2fe; text-decoration: none; font-weight: 700;'>@safevoice009</a>"
    "</div>",
    unsafe_allow_html=True
)