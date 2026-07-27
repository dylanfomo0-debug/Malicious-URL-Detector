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
*   **Balance**: Dataset was significantly imbalanced (Benign: 428,103, Malicious: 223,088).

### 3. Key Decisions & Rationales
*   **Duplicate Removal**: Removed 10,066 duplicate rows to prevent model bias and overfitting.
*   **Binary Label Conversion**: Mapped `phishing`, `malware`, and `defacement` to `1` (malicious) and `benign` to `0`. This simplifies the classification task to a binary problem.
*   **Dataset Balancing**: Applied undersampling to the majority class (benign) to match the minority class (malicious), resulting in a balanced dataset. This mitigates bias towards the majority class.

### 4. Final Data Stats
| Stage | Samples |
| :--- | :--- |
| Original | 651,191 |
| After removing duplicates | 641,125 |
| Final balanced dataset | 426,090 |

### 5. What I Learned
*   Real-world datasets often require cleaning (e.g., duplicate removal) before model training.
*   Class imbalance is a common issue in cybersecurity datasets and must be addressed to prevent model bias.
*   Binary classification simplifies the problem when the primary goal is to distinguish between safe and unsafe.

---

## Day 3: Feature Engineering

### 1. Feature Categories Implemented
*   **Lexical Features**: Quantitative characteristics of the URL string.
*   **Text Vectors (TF-IDF)**: Statistical representations of URL tokens.

### 2. Key Decisions & Rationales
*   **Custom Tokenization**: Implemented a custom tokenizer (`get_tokens` function) that splits URLs by `/`, `-`, and `.` and filters out common, non-informative tokens (`www`, `com`). This approach is tailored for URL structures.
*   **TF-IDF Vectorization**: Used `TfidfVectorizer` with the custom tokenizer. This method assigns weights to tokens based on their frequency in a URL and rarity across the dataset, highlighting potentially malicious terms.
*   **Lexical Feature Selection**: Extracted features such as URL length, counts of specific characters (`.`, `-`, `_`, `/`, `?`, `=`, `@`, `&`), presence of IP addresses (`use_ip`), and HTTPS status (`is_https`). These features are known indicators of malicious URLs.

### 3. Deliverables
*   `lexical_features.csv`: Contains the extracted lexical features and the binary labels.
*   `tfidf_vectorizer.joblib`: The trained TF-IDF vectorizer, saved for consistent tokenization during inference.

### 4. What I Learned
*   Effective feature engineering for URLs requires specialized tokenization and feature selection beyond standard NLP techniques.
*   Lexical features provide valuable structural insights into URLs.
*   TF-IDF helps in identifying significant tokens by considering their importance within the document and across the corpus.
