# Day 1: Understand the Goal & Set Up Environment

Welcome to Day 1 of building your Malicious URL Detector! Today, we focus on understanding the fundamental concepts and setting up your development environment.

## Tasks for Day 1:

1.  **Understand the Core Methodology**: Review the `background_theory.md` document to grasp the fundamental concepts of malicious URL detection, including lexical features, N-grams, tokenization, vectorization, and classification models.

2.  **Environment Setup**:
    *   **Install Python**: Ensure Python 3.x is installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).
    *   **Install a Development Environment**: Choose and install either Jupyter Notebook (`pip install jupyter`) or VS Code ([code.visualstudio.com](https://code.visualstudio.com/)) with the Python extension.
    *   **Install Key Data Science Libraries**: Install the necessary Python libraries by running:
        ```bash
        pip install pandas numpy scikit-learn nltk
        ```
    *   **Download NLTK Data**: Open a Python interpreter and run:
        ```python
        import nltk
        nltk.download("punkt")
        nltk.download("wordnet")
        ```

## Deliverable for Day 1:

*   A working Python environment with `pandas`, `numpy`, `scikit-learn`, and `nltk` installed.
*   Your chosen development environment (Jupyter Notebook or VS Code) set up and ready for coding.
*   A foundational understanding of the project's theoretical underpinnings from `background_theory.md`.
