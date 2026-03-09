# Understanding Data Shapes and Column Data Types Milestone

## 📋 Assignment Overview

This milestone focuses on understanding DataFrame shapes and column data types in Pandas—critical skills for any data analysis task. You'll learn to inspect dataset structure, identify data types, and detect potential issues before processing.

## 🎯 Learning Objectives

By completing this milestone, you will:
- ✅ Interpret DataFrame shape confidently
- ✅ Identify the number of rows and columns
- ✅ Understand column data types at a high level
- ✅ Detect incorrect or unexpected data types
- ✅ Make informed decisions before data processing

## 📁 Files Created

### 1. Main Script
**Location:** `scripts/data_shapes_types_milestone.py`

This comprehensive script demonstrates:
- Understanding DataFrame shape (rows × columns)
- Identifying rows vs columns correctly
- Understanding common Pandas data types
- Inspecting column data types intentionally
- Recognizing type-related issues early
- Proper inspection workflow

### 2. Video Instructions
**Location:** `outputs/VIDEO_INSTRUCTIONS_SHAPES_TYPES.txt`

Complete guide for recording your 2-minute video walkthrough including:
- Section-by-section breakdown
- Suggested narration examples
- Recording tips and checklist
- Common mistakes to avoid

## 🚀 How to Complete This Assignment

### Step 1: Review the Script
Read through the script to understand the concepts:
```bash
# Open in your editor
code scripts/data_shapes_types_milestone.py
```

### Step 2: Run the Script
Execute the script to see the output:
```bash
python scripts/data_shapes_types_milestone.py
```

### Step 3: Study the Output
The script will show you:
1. **Section 1:** How to inspect DataFrame shape
2. **Section 2:** Understanding rows vs columns
3. **Section 3:** Column data types explained
4. **Section 4:** Why types matter (with examples)
5. **Section 5:** Detecting type-related issues
6. **Section 6:** Complete inspection workflow
7. **Bonus:** Example of problematic data types

### Step 4: Record Your Video (~2 minutes)
Follow the instructions in `outputs/VIDEO_INSTRUCTIONS_SHAPES_TYPES.txt`:
- Show the script running
- Explain each major section
- Demonstrate understanding, not just reading
- Make sure screen is clearly visible
- Audio should be clear

### Step 5: Submit
- Create a Pull Request (if required)
- Submit video link as instructed
- Ensure video meets all criteria

## 🔑 Key Concepts Covered

### 1. DataFrame Shape
```python
df.shape  # Returns (rows, columns)
# Example: (7, 5) means 7 rows and 5 columns
```

### 2. Data Types in Pandas
- **object:** Text/string data or mixed types
- **int64:** Integer numbers (whole numbers)
- **float64:** Floating-point numbers (decimals)
- **datetime64:** Date and time values
- **bool:** Boolean True/False values

### 3. Why Types Matter
✅ **Correct Type (numeric):**
```python
df['Amount'].sum()  # Returns: 764.75 ✓
```

❌ **Wrong Type (string):**
```python
df['Amount'].sum()  # Returns: '125.545.0' ✗ (concatenates!)
```

### 4. Inspection Functions
```python
df.shape           # Get dimensions (rows, columns)
df.dtypes          # Get column data types
df.info()          # Get comprehensive overview
df.describe()      # Get statistical summary
df.head()          # See first 5 rows
```

## 💡 Best Practices

1. **Always check shape after loading data**
   - Know how much data you're working with
   - Understand the dataset dimensions

2. **Never assume column data types**
   - Explicitly check types using df.dtypes
   - Verify numeric columns aren't stored as strings

3. **Shape and types guide all next steps**
   - Use this info to plan your analysis
   - Prevents errors during processing

4. **This step prevents downstream errors**
   - Catching issues early saves debugging time
   - Ensures analysis results are trustworthy

## ⚠️ Common Issues to Watch For

### Issue 1: Numeric Data Stored as Strings
**Problem:** Can't perform calculations
```python
# Check
df.dtypes  # If numeric column shows 'object', it's wrong

# Fix
df['column'] = pd.to_numeric(df['column'], errors='coerce')
```

### Issue 2: Date Columns as Text
**Problem:** Can't use date operations
```python
# Check
df.dtypes  # If date column shows 'object', needs conversion

# Fix
df['date_column'] = pd.to_datetime(df['date_column'])
```

### Issue 3: Mixed Types in Columns
**Problem:** Inconsistent behavior
- Always have uniform types within a column
- Use appropriate error handling during conversion

## 📊 Sample Output Explained

When you run the script, you'll see:

```
DataFrame Shape: (7, 5)
  - Number of Rows (Observations): 7
  - Number of Columns (Features): 5
```

**This means:**
- 7 transaction records
- 5 attributes per transaction
- 35 total data points

```
Column Data Types:
Date               object
Category           object
Amount            float64
Type               object
Payment_Method     object
```

**This means:**
- Most columns are text (object)
- Amount is numeric (float64) - correct for money
- Date might need conversion to datetime

## 🎥 Video Recording Checklist

Before recording:
- [ ] Script runs without errors
- [ ] Terminal font is large and readable
- [ ] Screen capture software is ready
- [ ] Clear background/workspace

During recording:
- [ ] Show and run the script
- [ ] Explain each major section
- [ ] Point out key concepts
- [ ] Demonstrate the problematic example
- [ ] Speak clearly at moderate pace

After recording:
- [ ] Video is ~2 minutes long
- [ ] Screen is clearly visible
- [ ] Audio is clear
- [ ] All 5 main sections covered
- [ ] Shows understanding, not just execution

## 📚 Additional Resources

### Official Pandas Documentation
- [DataFrame.shape](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html)
- [DataFrame.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
- [DataFrame.info()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)
- [Data Types Overview](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes)

### Bonus Reading (Optional)
- Pandas Data Types and Performance Considerations
- Type Conversion Best Practices
- Handling Mixed-Type Data

## ✅ Success Criteria

You've successfully completed this milestone when:
1. ✅ You can explain what df.shape represents
2. ✅ You understand the difference between rows and columns
3. ✅ You can identify common Pandas data types
4. ✅ You understand why correct types matter
5. ✅ You can detect type-related issues in a dataset
6. ✅ You've recorded a clear 2-minute demonstration video

## 🎓 Next Steps

After mastering shapes and types:
1. Move to data cleaning milestones
2. Learn about handling missing values
3. Practice data transformation
4. Build complete analysis pipelines

## 📝 Notes

- This is a **foundational** skill - master it well
- Most data errors start with misunderstanding shape or types
- Always inspect before processing
- Make this your standard workflow

## 🆘 Troubleshooting

**Script doesn't run:**
```bash
# Check you're in the right directory
cd "d:\Kalvium\Simulation work\Sem-4\MoneyMind (Sprint - 3)\S86-0226-FinSightSquad-Applied-DataScience-Foundations"

# Try running again
python scripts/data_shapes_types_milestone.py
```

**Import errors:**
```bash
# Ensure pandas is installed
pip install pandas numpy
```

**Data file not found:**
- Ensure `data/raw/sample_transactions.csv` exists
- Check the file path is correct

## 📞 Support

If you encounter issues:
1. Re-read the script comments
2. Check the video instructions
3. Review the output carefully
4. Consult official Pandas documentation
5. Ask your instructor or TA

---

**Remember:** Understanding data shapes and types is like reading a map before starting a journey. It prevents you from getting lost in your analysis!

Good luck! 🎯✨
