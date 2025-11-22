# Anti-Money Laundering (AML) Detection System

## Project Summary

This project implements an Anti-Money Laundering detection system using machine learning techniques to identify suspicious financial transactions. The system analyzes transaction patterns to flag potential money laundering activities.

## Dataset

**SAML-D Synthetic Transaction Monitoring Dataset**
- Source: [Kaggle - SAML-D Dataset](https://www.kaggle.com/)
- The dataset contains synthetic financial transaction records with labeled fraud cases

## What is AML and Fraud Detection?

**Anti-Money Laundering (AML)** refers to laws, regulations, and procedures designed to prevent criminals from disguising illegally obtained funds as legitimate income.

**Fraud Detection** uses data analysis and machine learning to identify suspicious patterns in financial transactions that may indicate:
- Money laundering
- Identity theft
- Payment fraud
- Unusual transaction patterns

## Project Goals

- Analyze transaction patterns in the dataset
- Build features that capture suspicious behavior
- Develop models to detect potential money laundering activities
- Create an interpretable system for financial compliance

## Environment Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd aml_project
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Place your dataset CSV file in the `data/raw/` folder

### Running the Project

1. Start with exploratory data analysis:
   ```bash
   jupyter notebook notebooks/01_EDA.ipynb
   ```

2. Run preprocessing:
   ```bash
   jupyter notebook notebooks/02_preprocessing.ipynb
   ```

3. Feature engineering:
   ```bash
   jupyter notebook notebooks/03_feature_engineering.ipynb
   ```

## Project Structure

```
aml_project/
│
├── data/
│   ├── raw/              # Original dataset files
│   ├── processed/        # Cleaned and processed data
│
├── notebooks/
│   ├── 01_EDA.ipynb                    # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb          # Data cleaning and preprocessing
│   ├── 03_feature_engineering.ipynb    # Feature creation
│
├── src/
│   ├── load_data.py            # Data loading utilities
│   ├── preprocessing.py        # Preprocessing functions
│   ├── feature_engineering.py  # Feature engineering functions
│
├── README.md
├── requirements.txt
```

## Contributors

Data Mining Course - Term 9

## License

This is an academic project for educational purposes.
