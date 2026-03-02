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

---

## Conditional Statements for Data Logic Milestone

This milestone focuses on writing conditional statements to control program flow based on data-driven logic. Conditions allow your code to make decisions, which is essential for validation, branching workflows, and real-world data handling.

### Objective

Understanding conditional logic is a core programming skill that enables you to move beyond linear scripts and build intelligent behavior into your code.

Learn to:

- Understand how conditional statements work in Python
- Use `if`, `elif`, and `else` correctly
- Write conditions based on numeric and string data
- Combine conditions using logical operators (`and`, `or`, `not`)
- Apply conditionals to simple data scenarios

### Why This Matters

Common beginner issues include:

- Code that runs but produces incorrect results
- Conditions that never trigger as expected
- Incorrect indentation causing logic bugs
- Overly complex or unreadable condition blocks

This milestone ensures that:

- Your code behaves predictably
- Decisions are based on correct data checks
- Edge cases are handled intentionally
- Logic is readable and maintainable

### Run the Script

```bash
python scripts/conditional_statements_milestone.py
```

### What the Script Demonstrates

1. **Basic if Statements**
   - Simple numeric and string conditions
   - Understanding when code blocks execute
   - Budget checks, status verification

2. **if-else Decision Branching**
   - Handling both true and false paths
   - Account balance validation
   - Age eligibility checks
   - Transaction type routing

3. **Multiple Conditions with elif**
   - Credit score evaluation (4 tiers)
   - Income bracket classification
   - Investment risk level assessment
   - Sequential condition checking

4. **Logical Operators**
   - `and` - Both conditions must be true (premium feature eligibility)
   - `or` - At least one condition must be true (fee waiver qualification)
   - `not` - Invert boolean values (account accessibility)
   - Combined operators (loan application approval)

5. **Real-World Data Validation**
   - Portfolio allocation validator (must sum to 100%)
   - Transaction authorization (limit checks, balance verification)
   - Data quality checking (completeness validation)

### Learning Outcomes

After completing this milestone, you will be able to:

- Write clear and correct conditional statements
- Control program flow based on data values
- Handle multiple conditions safely
- Avoid common logic and indentation errors
- Use conditionals confidently in data workflows
- Implement data validation and business logic

### Files Added

- `scripts/conditional_statements_milestone.py` — comprehensive examples of if, elif, else, and logical operators
- `scripts/README_MILESTONE_CONDITIONAL.md` — detailed documentation and learning guide
- `outputs/VIDEO_INSTRUCTIONS_CONDITIONAL.txt` — video recording checklist with step-by-step guidance

### Video Requirements (~2 minutes)

Record a screen-capture video demonstrating:

1. A simple `if` statement with explanation
2. An `if-else` example showing both branches
3. An `if-elif-else` example with multiple conditions
4. Use of logical operators (`and`, `or`, or `not`)
5. Explanation of why conditions behave as they do

**Submission:**
- Video should be approximately 2 minutes
- Screen must be clearly visible
- Explain concepts verbally as you demonstrate
- Upload video and paste link into `outputs/video_link.txt`

### Key Concepts Covered

**Comparison Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`

**Logical Operators:** `and`, `or`, `not`

**Control Flow:** `if`, `elif`, `else`

**Best Practices:**
- Proper indentation (critical in Python)
- Readable condition ordering
- Avoiding overlapping conditions
- Clear variable naming in conditions

### Submission Checklist

- [ ] Run `scripts/conditional_statements_milestone.py` successfully
- [ ] Understand all five sections of the output
- [ ] Record ~2 minute video covering all requirements
- [ ] Upload video and add link to `outputs/video_link.txt`
- [ ] Review `scripts/README_MILESTONE_CONDITIONAL.md` for additional guidance
- [ ] Submit Pull Request (if required by course)

### Next Steps

After mastering conditional statements, you'll be ready to:

- Build more complex data validation logic
- Implement business rules in data workflows
- Create interactive decision-making programs
- Combine conditionals with loops for iteration
- Handle edge cases in data processing

**Remember:** Conditional logic is the backbone of intelligent programs. This milestone ensures you can write clear, correct decisions in Python confidently.