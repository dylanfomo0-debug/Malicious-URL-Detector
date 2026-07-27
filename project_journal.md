# Project Journal: Malicious URL Detector

## Day 2: Data Acquisition & Preprocessing

### 1. Dataset Overview
*   **Dataset**: `malicious_phish.csv`
*   **Source**: Kaggle (via jivoi/awesome-ml-for-cybersecurity)
*   **Total Samples**: 651,191
*   **Columns**: `url`, `type`
*   **Classes**: `benign`, `phishing`, `malware`, `defacement`

### 2. Initial Inspection Findings
*   **Missing Values**: None detected.
*   **Duplicates**: 10,066 duplicate rows found.
*   **Balance**: Dataset was significantly imbalanced (Benign: 428k, Malicious: 223k).

### 3. Key Decisions & Rationales
*   **Why Data Cleaning?**: Duplicate URLs can cause the model to learn the same examples repeatedly, leading to overfitting and biased results. Removing them ensures the model learns from unique samples.
*   **Why Balance the Dataset?**: If left imbalanced, the classifier might become biased toward predicting "benign" simply because it dominates the training data. We used **undersampling** on the benign class to create a 50/50 split.
*   **Why Binary Labels?**: We merged `phishing`, `malware`, and `defacement` into a single "Malicious" class (1). This simplifies the task to a binary classification, focusing on the core problem: is the URL dangerous or not?

### 4. Final Data Stats
| Stage | Samples |
| :--- | :--- |
| Original | 651,191 |
| After removing duplicates | 641,125 |
| Final balanced dataset | 426,090 |

---

## Day 3: Feature Engineering

### 1. Feature Categories
We extracted two main types of features to represent the URLs numerically:
*   **Lexical Features**: Quantitative characteristics of the URL string.
*   **Text Vectors (TF-IDF)**: Statistical representations of the "words" or tokens within the URL.

### 2. Key Concepts & Decisions
*   **Custom Tokenization**: Following the `awesome-ml-for-cybersecurity` tutorial, we used a custom tokenizer that splits URLs by `/`, `-`, and `.`. This is more effective than standard text tokenizers because it isolates meaningful segments like `wp-admin` or `login`.
*   **Why TF-IDF?**: Term Frequency-Inverse Document Frequency (TF-IDF) was chosen over simple counts. It highlights unique, suspicious tokens (like `virus` or `exe`) while down-weighting common ones (like `www` or `com`).
*   **Lexical Analysis**: We extracted features like URL length, special character counts (`@`, `?`, `-`), and the presence of an IP address. These are strong indicators of malicious intent (e.g., attackers often use `@` to spoof domains or long paths to hide the destination).

### 3. Features Extracted
*   `url_len`: Total length of the URL.
*   `count_dot`, `count_hyphen`, `count_slash`, etc.: Counts of specific characters.
*   `use_ip`: Binary flag for raw IP addresses in the domain.
*   `is_https`: Security status of the protocol.

### 4. What I Learned
*   URLs require specialized tokenization compared to natural language.
*   Feature engineering is where "domain knowledge" (cybersecurity) meets "data science."
*   Lexical features provide structural context, while TF-IDF captures semantic patterns.
