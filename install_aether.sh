#!/bin/bash

# 🌌 AetherClaw Universal Installer (v3.0)
# Usage: curl -sSL https://raw.githubusercontent.com/safevoice009/AetherClaw/main/install_aether.sh | bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🌌 Initializing AetherClaw v3.0 'Omnipresence' Deployment...${NC}"
echo "--------------------------------------------------------"

# 1. Environment Detection
if [ -d "$HOME/.termux" ]; then
    echo -e "${BLUE}[SYSTEM] Termux detected. Applying mobile optimizations...${NC}"
    ENV="TERMUX"
else
    ENV="STANDARD"
fi

# 2. Dependency Check (Python)
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python 3 is not installed. Please install it first.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}[CHECK] Python $PYTHON_VERSION detected.${NC}"

# 3. Installing Tactical Dependencies
echo -e "${BLUE}[ACTION] Installing core dependencies...${NC}"
python3 -m pip install -r requirements.txt --quiet
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[SUCCESS] Dependencies integrated.${NC}"
else
    echo -e "${RED}[ERROR] Dependency installation failed. Check your internet connection.${NC}"
    exit 1
fi

# 4. Configuration Setup
if [ ! -f ".env" ]; then
    echo -e "${BLUE}[ACTION] Configuring Intelligence Nexus (.env)...${NC}"
    cp .env.example .env
    echo -e "${GREEN}[SUCCESS] .env created from template. Please edit it with your API keys.${NC}"
fi

# 5. Hardware Intelligence Report
echo -e "${BLUE}[ACTION] Running Hardware Resonance Check...${NC}"
python3 utils/hardware_detect.py

echo -e "${GREEN}--------------------------------------------------------"
echo -e "🌌 AetherClaw is now DEPLOYED."
echo -e "--------------------------------------------------------${NC}"
echo -e "To start the Strategic Hub (Dashboard):"
echo -e "  ${BLUE}streamlit run dashboard/app.py${NC}"
echo ""
echo -e "To start the Tactical CLI (AetherLite - Recommended for $ENV):"
echo -e "  ${BLUE}python3 supervisor/aether_lite.py 'your-goal'${NC}"
echo "--------------------------------------------------------"
