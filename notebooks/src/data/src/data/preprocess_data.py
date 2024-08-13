import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    # Convert date column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Sort data by date
    df = df.sort_values('timestamp')
    
    # Handle missing values (example: forward fill)
    df.fillna(method='ffill', inplace=True)
    
    # Save preprocessed data
    processed_path = file_path.replace('raw', 'processed')
    df.to_csv(processed_path, index=False)
    print(f"Preprocessed data saved to {processed_path}")

if __name__ == '__main__':
    preprocess_data('data/raw/AAPL_daily.csv')
