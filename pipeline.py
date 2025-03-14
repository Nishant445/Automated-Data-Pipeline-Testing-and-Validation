import pandas as pd

# Load the data
def load_data(file_path):
    return pd.read_csv(file_path)

# Clean the data Removing the missing values
def clean_data(df):
    return df.dropna()

# Saving the clean data
def save_data(df, output_path):
    df.to_csv(output_path, index=False)

# Run pipeline
if __name__  == "__main__":
    df = load_data("data/orders.csv")
    df_cleaned = clean_data(df)
    save_data(df_cleaned, "data/cleaned_orders.csv")
    print("Data pipeline executed successfully")
    
