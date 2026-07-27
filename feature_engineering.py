import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def get_tokens(url):
    """
    Custom tokenizer for URLs based on the jivoi/awesome-ml-for-cybersecurity tutorial.
    """
    # Split by slash, dash, and dot
    tokens = re.split(r'[/\-\.]', url)
    
    # Remove redundant tokens and 'com'
    tokens = [t for t in tokens if t and t != 'com' and t != 'www']
    
    # Return unique tokens
    return list(set(tokens))

def extract_lexical_features(df):
    """
    Extract lexical and structural features from the raw URLs.
    """
    print("Extracting lexical features...")
    
    # URL Length
    df['url_len'] = df['url'].apply(len)
    
    # Count specific characters
    df['count_dot'] = df['url'].apply(lambda i: i.count('.'))
    df['count_hyphen'] = df['url'].apply(lambda i: i.count('-'))
    df['count_underline'] = df['url'].apply(lambda i: i.count('_'))
    df['count_slash'] = df['url'].apply(lambda i: i.count('/'))
    df['count_question'] = df['url'].apply(lambda i: i.count('?'))
    df['count_equal'] = df['url'].apply(lambda i: i.count('='))
    df['count_at'] = df['url'].apply(lambda i: i.count('@'))
    df['count_and'] = df['url'].apply(lambda i: i.count('&'))
    
    # Presence of IP address
    def use_ip(url):
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
        return 1 if match else 0
    df['use_ip'] = df['url'].apply(use_ip)
    
    # HTTPS status (1 if https, 0 otherwise)
    df['is_https'] = df['url'].apply(lambda i: 1 if urlparse(i).scheme == 'https' else 0)
    
    return df

if __name__ == "__main__":
    # Load the balanced dataset from Day 2
    print("Loading balanced dataset...")
    df = pd.read_csv("balanced_dataset.csv")
    
    # Extract Lexical Features
    df = extract_lexical_features(df)
    
    # Text Vectorization using TF-IDF with custom tokenizer
    print("Vectorizing URLs using TF-IDF...")
    vectorizer = TfidfVectorizer(tokenizer=get_tokens)
    X_tfidf = vectorizer.fit_transform(df['url'])
    
    # Save the vectorizer for Day 4/5
    joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')
    
    # Combine lexical features with TF-IDF features might be too large for a CSV
    # So we'll save the lexical features separately
    lexical_features = ['url_len', 'count_dot', 'count_hyphen', 'count_underline', 
                        'count_slash', 'count_question', 'count_equal', 'count_at', 
                        'count_and', 'use_ip', 'is_https']
    
    df_lexical = df[lexical_features + ['label']]
    df_lexical.to_csv("lexical_features.csv", index=False)
    
    print("Day 3: Feature engineering complete.")
    print(f"Lexical features saved to lexical_features.csv")
    print(f"TF-IDF vectorizer saved to tfidf_vectorizer.joblib")
