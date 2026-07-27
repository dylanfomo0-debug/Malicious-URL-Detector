# Day 3: Feature Engineering

Today, we transform our raw URL strings into numerical features that a machine learning model can process. This is the stage where domain knowledge about cybersecurity is used to create meaningful representations of the data.

## 1. Feature Categories

We focus on two main categories of features:

1.  **Lexical Features**: These are quantitative characteristics extracted from the URL's structure (e.g., length, special character counts).
2.  **Text Vectors (TF-IDF)**: These represent the semantic content of the URL by breaking it into tokens and calculating their importance.

## 2. Lexical Feature Extraction

Lexical features are often strong indicators of malicious intent. For example, attackers frequently use long URLs to hide the actual destination or use special characters like `@` to spoof legitimate domains.

### Key Features Extracted:
*   **URL Length**: Malicious URLs tend to be longer than benign ones.
*   **Special Character Counts**: We count occurrences of `.`, `-`, `_`, `/`, `?`, `=`, `@`, and `&`.
*   **IP Address Presence**: Detecting if the URL uses a raw IP address instead of a domain name.
*   **HTTPS Status**: Checking if the URL uses the secure `https` protocol.

## 3. Custom Tokenization & TF-IDF

Standard text tokenizers (like those used for English sentences) are not ideal for URLs. Following the best practices from the `jivoi/awesome-ml-for-cybersecurity` repository, we implemented a custom tokenizer.

### The Custom Tokenizer
Our tokenizer splits URLs by common delimiters: `/`, `-`, and `.`. It also filters out non-informative tokens like `www` and `com`. This helps the model focus on meaningful segments like `wp-admin`, `login`, or `virus`.

### TF-IDF Vectorization
We use **TF-IDF (Term Frequency-Inverse Document Frequency)** to vectorize these tokens. TF-IDF is superior to simple counting because it rewards tokens that are frequent in a specific URL but rare across the entire dataset, effectively highlighting suspicious "keywords."

## 4. Implementation

We created a Python script (`feature_engineering.py`) that:
1.  Loads the balanced dataset from Day 2.
2.  Extracts lexical features using custom logic and `urllib.parse`.
3.  Vectorizes the URLs using `TfidfVectorizer` with our custom tokenizer.
4.  Saves the extracted features and the fitted vectorizer for use in training.

## 5. Deliverable for Day 3

By the end of Day 3, you have:
*   Implemented a **custom URL tokenizer**.
*   Extracted a suite of **lexical features**.
*   Created a **TF-IDF vectorizer** fitted to your dataset.
*   Saved your processed features in `lexical_features.csv` and your vectorizer in `tfidf_vectorizer.joblib`.

Your data is now fully "engineered" and ready for the model training phase starting on Day 4!
