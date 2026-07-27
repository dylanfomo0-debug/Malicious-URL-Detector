# Day 3: Feature Engineering

Today, we transform our raw URL strings into numerical features that a machine learning model can process.

## Tasks for Day 3:

1.  **Implement Feature Engineering Script**: Create and run `feature_engineering.py` to:
    *   Load the `balanced_dataset.csv` from Day 2.
    *   Define a `get_tokens` function for custom URL tokenization (splitting by `/`, `-`, `.` and removing `www`, `com`).
    *   Implement `extract_lexical_features` to calculate:
        *   URL length (`url_len`)
        *   Counts of specific characters (`.`, `-`, `_`, `/`, `?`, `=`, `@`, `&`)
        *   Presence of IP address (`use_ip`)
        *   HTTPS status (`is_https`)
    *   Initialize and fit a `TfidfVectorizer` using the custom `get_tokens` function on the URL column.
    *   Save the extracted lexical features to `lexical_features.csv`.
    *   Save the fitted `TfidfVectorizer` to `tfidf_vectorizer.joblib`.

## Deliverable for Day 3:

*   `lexical_features.csv`: A CSV file containing the extracted lexical features and labels.
*   `tfidf_vectorizer.joblib`: The fitted TF-IDF vectorizer object.
*   Updated `project_journal.md` with notes on feature engineering decisions and insights.
