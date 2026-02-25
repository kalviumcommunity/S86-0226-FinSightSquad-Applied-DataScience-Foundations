# S86-0226-FinSightSquad-Applied-DataScience-Foundations

**Environment Setup**

- **OS:** Windows
- **Status (as of 2026-02-24):** Python and Anaconda installed and verified

**What I installed**

- Python (installed and callable from Command Prompt)
- Anaconda (Anaconda Distribution for Windows)

**Steps I followed (brief)**

1. Downloaded the Anaconda installer for Windows from the official site.
2. Ran the installer and completed the setup (default options).
3. Opened Command Prompt and Anaconda Prompt to verify installations.

**Verification commands (run in Command Prompt or Anaconda Prompt)**

Run these commands and paste the outputs into this README for permanent proof.

Python version:

```

Conda (Anaconda) version:
conda --version
```

Python executable path (optional):

```
python -c "import sys; print(sys.executable)"
```

List Conda environments (shows `base`):

```
conda info --envs
```

Example: paste your actual terminal outputs here after running the commands above.

```
# Python --version
# REPLACE_WITH_YOUR_OUTPUT

# conda --version
# REPLACE_WITH_YOUR_OUTPUT
```

**Optional — create a dedicated Data Science environment**

Run these in Anaconda Prompt if you want a separate environment for the sprint:

```
conda create -n ds-sprint python=3.10 -y
conda activate ds-sprint
conda install numpy pandas matplotlib jupyter -y
```

**Video walkthrough (record ~2 minutes)**

Please include all of the following in your short screen recording:

- Terminal showing `python --version` (proof Python is callable)
- Terminal showing `conda --version` (proof Anaconda/conda is accessible)
- A brief walkthrough of this README section showing where you saved the verification outputs

Keep the recording concise and focused — this validates that the setup is real and reproducible.

This project requires a verified local Data Science environment before starting the sprint. Below is a concise checklist, reproducible commands, and placeholders where you should paste your actual terminal outputs and links to your short verification video and PR.

- **Operating system:** Windows
- **Date checked:** 2026-02-24

**What to verify (run these in Command Prompt, PowerShell, or Anaconda Prompt)**

Commands to run (copy/paste the outputs into the "Proof outputs" section below):

```powershell
# 1) Python version
python --version

# 2) Quick Python REPL check (prints a short string)
python -c "print('hello from python')"

# 3) Conda version
conda --version

# 4) List Conda environments
conda info --envs

# 5) Jupyter: launch Notebook or Lab and open in your browser
jupyter notebook
# or
jupyter lab
```

**Proof outputs (paste exact terminal output here)**

```text
# Python --version
REPLACE_WITH_PYTHON_VERSION_OUTPUT

# python -c "print('hello from python')"
REPLACE_WITH_PYTHON_REPL_OUTPUT

# conda --version
REPLACE_WITH_CONDA_VERSION_OUTPUT

# conda info --envs
REPLACE_WITH_CONDA_ENVS_OUTPUT

# Jupyter launch notes (server URL, no errors)
REPLACE_WITH_JUPYTER_LAUNCH_NOTES
```

**Environment used**

- **Active environment when testing:** REPLACE_WITH_active_env_name (e.g., base or ds-sprint)
- **Python executable path (optional):**

```powershell
python -c "import sys; print(sys.executable)"
```

Paste output here:

```text
REPLACE_WITH_PYTHON_EXECUTABLE_PATH
```

**Jupyter verification steps (brief)**

- Launch `jupyter notebook` or `jupyter lab` from the terminal while the environment is active.
- The browser should open and display the Notebook/Lab UI without errors.
- Create a new Python notebook and run a cell containing:

```python
print('jupyter is connected to the active environment')
```

- Confirm the output appears below the cell. Paste a short note here confirming success.

**Video walkthrough (≈2 minutes)**

Record a short screen video that includes:

- Terminal showing `python --version` and the REPL check.
- Terminal showing `conda --version` and `conda info --envs` with the active environment visible.
- Launching Jupyter Notebook or JupyterLab and running the small Python cell shown above.
- A brief glance at this README verification section where you've pasted outputs.

Add your video link here:

- Video link: REPLACE_WITH_SCREEN_RECORDING_LINK

**Pull Request**

After pasting outputs and adding the video link, create a Pull Request to submit this verification. Add the PR link here once created.

- PR link: REPLACE_WITH_PR_LINK

**Why this matters (short)**

- Ensures Python, Conda, and Jupyter are installed and work together.
- Prevents environment-related blockers during the sprint.
- Provides reproducible proof for mentors and teammates.
**Next steps**

- Paste the actual command outputs into the "Example" block above so this README serves as proof.
- (Optional) Push changes and create a Pull Request per the milestone instructions.
