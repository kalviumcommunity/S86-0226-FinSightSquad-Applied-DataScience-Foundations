**Histogram Milestone**

- **Goal**: Visualize numeric data distributions using histograms, interpret shapes, and compare distributions.

- **Files added**: `src/histograms.py` (utility to build histograms and basic interpretations).

- **How to run**:

  - Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

  - Run the script on the sample CSV:

    ```bash
    python src/histograms.py --csv data/sample_01_standard.csv --compare
    ```

  - Outputs are written to `outputs/histograms/` as HTML (interactive) and PNG (static if `kaleido` available).

- **What the script does**:

  - Detects numeric columns automatically.
  - Creates a histogram (with a boxplot margin) for each numeric column.
  - Optionally compares distributions by `transaction_type` (debit/credit) using `--compare`.
  - Prints simple summary statistics and a one-line interpretation based on skewness.

- **Interpreting outputs**:

  - Look for skewness: right-skewed data often indicate many small values and few large ones (common in transaction amounts).
  - Multi-modal patterns show multiple peaks — consider grouping or splitting data for deeper analysis.
  - Outliers appear as isolated bars far from the main mass and should be investigated.

- **Video guidance (2-minute script)**:

  1. Title slide (5s): "Histogram EDA — [Your Name]".
  2. Show running the script (20s): `python src/histograms.py --csv data/sample_01_standard.csv --compare`.
  3. Open one HTML histogram (30s): explain bins vs frequency and point out median/mean from console output.
  4. Explain skewness (25s): show a right-skewed example and interpret what it implies for transactions.
  5. Show comparison (20s): debit vs credit distribution and a brief takeaway.
  6. Closing (10s): suggest next steps (log transform, outlier handling, use histograms for feature engineering).

**Notes**: If you want, I can run the script and save a set of example images, or generate a small Jupyter notebook with inline plots and explanations. Tell me which you prefer.
