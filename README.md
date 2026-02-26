# Milestone 01: Jupyter Notebook Workspace Orientation

## Objective

This milestone ensures correct setup and understanding of the Jupyter Notebook workspace before beginning Data Science tasks.

The goal is to confidently:

- Launch Jupyter Notebook from the terminal
- Understand the Jupyter Home interface
- Navigate directories intentionally
- Create and manage notebooks correctly

---

## 1. Launching Jupyter Notebook

### Step 1: Activate Conda Environment

```bash
conda activate datasci
Step 2: Navigate to Project Directory
cd C:\Users\YourName\Documents\DataScienceSprint
Step 3: Launch Jupyter Notebook
jupyter notebook

Jupyter successfully opened in the browser without errors.

2. Understanding the Jupyter Home Interface

The Home interface includes:

File and folder listing panel

Navigation breadcrumbs

"New" button for creating notebooks

Upload button for adding files

File type indicators (folders, notebooks, scripts)

This confirms understanding of the workspace layout.

3. Folder Navigation

Successfully:

Navigated into project folders

Used breadcrumbs to return to parent directories

Verified project root directory

Confirmed notebook save location

4. Creating and Running a Notebook

Created:

milestone_01_workspace_setup.ipynb

Verified:

Correct Python kernel is active

Notebook executes properly

Test cell executed:

print("Jupyter is working correctly.")

Output confirmed execution functionality.

5. Notebook File Management

Practiced:

Renaming notebook

Saving changes

Closing notebook safely

Reopening from Home interface

Conclusion

This milestone confirms:

Proper environment activation

Correct directory management
## Data Organization Milestone: Raw / Processed / Output

This milestone ensures your project separates data by lifecycle stage to keep work reproducible and auditable.

What to do:

- Keep original, untouched inputs in `data/raw/` (treat as read-only).
- Save cleaned or transformed datasets in `data/processed/`.
- Save plots, reports, and models in `outputs/` (subfolders: `figures/`, `reports/`).
- Never write processed or output files into `data/raw/`.

Files added to support this milestone:

- `scripts/organize_data.py` — small example script showing a safe read-from-raw, write-to-processed pattern.
- `scripts/README_MILESTONE_DATA_ORG.md` — quick usage notes for the script.
- `outputs/VIDEO_INSTRUCTIONS.txt` — short recording checklist.
- `outputs/video_link.txt` — placeholder to paste your video link.

Recording the short (~2 minute) video:

- Show the `data/raw/` folder and explain why raw data is immutable.
- Show the `data/processed/` folder and explain naming for processing stages.
- Show the `outputs/` folder and describe output artifact types.
- State how your scripts enforce one-directional flow (read raw → write processed/output).
- Save the video, upload it where instructed by your course, and paste the link into `outputs/video_link.txt`.

Submission checklist:

- [ ] Raw files remain unchanged in `data/raw/`.
- [ ] Processed files live only in `data/processed/`.
- [ ] Outputs live in `outputs/` (figures, reports, models).
- [ ] Add your video link to `outputs/video_link.txt` and submit as required.

This section documents the data hygiene expectations for reproducible data science.


Understanding of Jupyter interface

Intentional notebook creation

Basic notebook management skills

The workspace is now correctly configured for upcoming Data Science tasks.