import pandas as pd
import os


def load_dataset(file_path):
    """Load the AML transaction dataset from CSV file."""
    print(f"Loading dataset from: {file_path}")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    
    print(f"\nDataset loaded successfully!")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    return df


def save_sample(df, output_path, sample_size=1000):
    """Save a small sample of the dataset for quick testing."""
    print(f"\nCreating sample of {sample_size} rows...")
    
    sample_df = df.sample(n=min(sample_size, len(df)), random_state=42)
    sample_df.to_csv(output_path, index=False)
    print(f"Sample saved to: {output_path}")
    
    return sample_df

