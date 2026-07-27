# Day 2: Data Acquisition & Preprocessing

Today, we focus on gathering our dataset and preparing it for machine learning, following the resources and methodologies from the [jivoi/awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) repository. This involves loading the data, cleaning it, and addressing class imbalance.

## 1. Data Acquisition from Awesome ML for Cybersecurity

The [jivoi/awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) repository is a curated list of tools and resources. For malicious URL detection, it points to several key datasets and tutorials.

### Recommended Sources
*   **Malicious URLs Data Sets**: The repository links to the [UCSD Malicious URL dataset](http://sysnet.ucsd.edu/projects/url/), which is a foundational resource in this field.
*   **Tutorial Methodology**: We are following the core approach outlined in the [Using Machine Learning to Detect Malicious URLs](http://web.archive.org/web/20170514093208/http://fsecurify.com/using-machine-learning-detect-malicious-urls/) tutorial (by Faizan Ahmad), which is a featured resource in the repository.

In our project, we are using the `malicious_phish.csv` dataset, which contains over 650,000 labeled URLs, aligning with the large-scale data requirements discussed in the repository's papers.

## 2. Data Preprocessing & Cleaning

As highlighted in the repository's featured tutorials, raw URL data requires specialized preprocessing.

### Step 1: Initial Data Inspection

We analyzed our dataset to identify duplicates and check the label distribution. This is a critical step emphasized in the "Data Science Pipeline" section of the repository's recommended readings.

**Analysis Results:**
*   **Total Entries**: 651,191
*   **Duplicates**: 10,066
*   **Class Imbalance**: ~66% Benign vs. ~34% Malicious.

### Step 2: Custom Tokenization (The "Awesome" Way)

The featured tutorial in the `awesome-ml-for-cybersecurity` repo suggests a custom tokenizer for URLs. Unlike standard text, URLs have unique delimiters like `.`, `/`, and `-`. 

**The Tutorial's Tokenizer Logic:**
1.  Split by `/` (slashes).
2.  Split the resulting segments by `-` (dashes).
3.  Split those segments by `.` (dots).
4.  Remove redundant tokens and common, non-informative segments like `com`.

This custom tokenization ensures that the model learns meaningful "features" like `virus`, `exe`, `php`, or `wp-admin` rather than just treating the entire URL as a single string.

### Step 3: Balancing the Dataset

The repository's papers often discuss the "imbalanced data" problem in cybersecurity. If we train on 400,000 benign URLs and only 200,000 malicious ones, the model might become biased toward predicting "Benign."

**Our Balancing Strategy (Undersampling):**
We undersampled the majority class (Benign) to match the minority class (Malicious), resulting in a perfectly balanced dataset of **426,090 unique URLs** (213,045 of each class). This ensures the model learns to distinguish between both classes with equal importance.

## 3. Deliverable for Day 2

By the end of Day 2, you have:
*   Acquired a dataset aligned with the **jivoi/awesome-ml-for-cybersecurity** recommendations.
*   Identified the need for **custom tokenization** based on the repository's featured tutorial.
*   Created a **balanced and cleaned** `balanced_dataset.csv` file, ready for the advanced feature engineering we'll perform on Day 3.

You are now following the same technical path used by professional cybersecurity researchers!
