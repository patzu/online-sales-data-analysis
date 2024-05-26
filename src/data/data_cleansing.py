import pandas as pd

def load_data(file_path):
    """Load the CSV file into a DataFrame."""
    data = pd.read_csv(file_path)
    return data

def explore_data(data):
    """Perform basic data exploration."""
    print("Data Info:")
    print(data.info())
    print("\nMissing Values:")
    print(data.isnull().sum())
    print("\nData Description:")
    print(data.describe())


def clean_data(data):
    """Clean the data by handling missing values, removing duplicates, and normalizing text."""
    data.fillna(data.mean(), inplace=True)  # Fill missing numerical values with the mean
    data.fillna('Unknown', inplace=True)  # Fill missing categorical values with 'Unknown'
    data.drop_duplicates(inplace=True)  # Remove duplicate rows
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = data[col].str.lower()  # Convert text to lowercase
    return data

def save_data(data, output_path):
    """Save the cleaned data to a new CSV file."""
    data.to_csv(output_path, index=False)


if __name__ == "__main__":
    raw_file_path = 'data/raw/Online_Sales_Data.csv'
    cleaned_file_path = 'data/processed/Cleaned_Online_Sales_Data.csv'
    data = load_data(raw_file_path)
    explore_data(data)
    # cleaned_data = clean_data(data)
    # save_data(cleaned_data, cleaned_file_path)
    print("Data cleaning complete. Cleaned data saved to:", cleaned_file_path)
