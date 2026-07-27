# Day 2: Data Acquisition & Preprocessing

Today, we focus on acquiring and preparing our dataset for machine learning, aligning with the `jivoi/awesome-ml-for-cybersecurity` repository recommendations.

## Tasks for Day 2:

1.  **Acquire Dataset**: Ensure the `malicious_phish.csv` dataset is in your project directory. (This was handled on Day 1).

2.  **Initial Data Inspection**: Run `analyze_dataset.py` to:
    *   Inspect dataset structure (`df.info()`).
    *   Check for duplicate rows (`df.duplicated().sum()`).
    *   Identify missing values (`df.isnull().sum()`).
    *   Analyze the original `type` distribution and the binary `label` distribution.

3.  **Clean Duplicates and Balance Labels**: Run `data_preparation.py` to:
    *   Remove duplicate URL entries.
    *   Map original `type` labels (`benign`, `defacement`, `phishing`, `malware`) to binary labels (`0` for benign, `1` for malicious).
    *   Undersample the majority class (benign URLs) to balance the dataset.
    *   Save the cleaned and balanced dataset as `balanced_dataset.csv`.

## Deliverable for Day 2:

*   A `balanced_dataset.csv` file in your project directory, containing unique URLs with a balanced distribution of benign and malicious labels.
*   Updated `project_journal.md` with notes on data inspection, cleaning, and balancing decisions.
