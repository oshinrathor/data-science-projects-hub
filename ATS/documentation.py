"""
==============================
   Anaconda + VS Code Cheat Sheet
==============================

# -----------------------------
# 1. Check Conda installation
# -----------------------------
# Check version of Conda
# Run in terminal:
conda --version

# Check where Conda is installed
where conda

# -----------------------------
# 2. Create a named Conda environment
# -----------------------------
# Create a permanent environment for your project
conda create -n ATS python=3.10 -y

# -----------------------------
# 3. Activate the environment
# -----------------------------
# Activate ATS environment in terminal session
conda activate ATS

# Check Python version inside the environment
python --version

# -----------------------------
# 4. List Conda environments
# -----------------------------
conda env list

# Optional: Check which Python executable is being used
where python

# -----------------------------
# 5. Key Lessons / Notes
# -----------------------------
# 1. Conda environment 'ATS' is permanent:
#    - Stored in D:\SOFTWARES\Anaconda3\envs\ATS
#    - Does NOT disappear when PC is turned off
#    - No need to recreate each time

# 2. Activation is temporary per terminal session:
#    - Must run 'conda activate ATS' whenever you open a new terminal

# 3. VS Code interpreter:
#    - Select ATS as interpreter for your project
#    - Scripts will run in ATS environment
#    - Terminal auto-activation in VS Code is optional

# 4. Named environment vs local venv:
#    - '-n ATS' creates a named environment (recommended)
#    - No 'venv/' folder appears inside project folder (normal)
#    - '-p ./venv' creates a local environment in project folder (less recommended)

# 5. Python version choice:
#    - Python 3.10 is stable and fully compatible with ML/AI libraries
#    - Newer versions (3.11+) may cause library compatibility issues

# 6. Multiple Python installations:
#    - Keep only Anaconda Python for ML work
#    - WindowsApps Python can be ignored
#    - Optional: uninstall other system Pythons

# 7. Project setup workflow:
#    - Environments are separate from project folders
#    - One environment can be used across multiple projects
#    - ATS environment persists and does NOT need recreation

# -----------------------------
# 6. Example ML Project Workflow
# -----------------------------
# 1. Create new environment (one-time):
conda create -n MyProject python=3.10 -y

# 2. Activate environment (each session):
conda activate MyProject

# 3. Open VS Code and select interpreter for this project

# 4. Install libraries inside environment:
pip install numpy pandas matplotlib seaborn jupyter
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install tensorflow
pip install transformers datasets scikit-learn sentencepiece

#5. To run code file and launch on streamlit:
streamlit run app.py

#6. Remember to open in browser for Streamlit apps:
http://localhost:8501/

#7. Using latest Google Gemini API Version:
gemini-2.5-flash

# 8. Work on your project — environment is permanent and reusable
"""
