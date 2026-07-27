import pandas as pd
from sklearn.utils import resample

def prepare_data(input_csv="dataset.csv", output_csv="balanced_dataset.csv"):
    print("Loading dataset...")
    df = pd.read_csv(input_csv)

    print("Initial dataset shape:", df.shape)
    print("Initial label distribution:\n", df["type"].value_counts())

    # 1. Remove duplicates
    print("Removing duplicate rows...")
    df.drop_duplicates(inplace=True)
    print("Dataset shape after removing duplicates:", df.shape)

    # Map types to binary labels (0: benign, 1: malicious)
    df["label"] = df["type"].apply(lambda x: 0 if x == "benign" else 1)
    print("Binary label distribution after mapping:\n", df["label"].value_counts())

    # Separate majority and minority classes
    df_majority = df[df.label == 0]  # Benign URLs
    df_minority = df[df.label == 1]  # Malicious URLs

    # 2. Balance labels (Undersampling majority class)
    print("Balancing dataset using undersampling...")
    # Undersample majority class to match minority class size
    df_majority_undersampled = resample(df_majority, 
                                        replace=False,    # sample without replacement
                                        n_samples=len(df_minority), # to match minority class
                                        random_state=42)  # reproducible results

    # Combine minority class with undersampled majority class
    df_balanced = pd.concat([df_majority_undersampled, df_minority])

    # Display new class counts
    print("Dataset shape after balancing:", df_balanced.shape)
    print("Balanced label distribution:\n", df_balanced["label"].value_counts())

    # Save the balanced dataset
    df_balanced.to_csv(output_csv, index=False)
    print(f"Balanced dataset saved to {output_csv}")

if __name__ == "__main__":
    prepare_data()
