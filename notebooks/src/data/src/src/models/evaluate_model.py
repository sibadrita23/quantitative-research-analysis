import pandas as pd
import matplotlib.pyplot as plt
import pickle

def plot_results(data_path, model_path):
    df = pd.read_csv(data_path)
    
    # Features and target
    X = df[['Moving_Avg', 'Returns']]
    y = df['Close']
    
    # Load the trained model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Predictions
    df['Predictions'] = model.predict(X)
    
    # Plot actual vs predicted
    plt.figure(figsize=(14, 7))
    plt.plot(df['timestamp'], df['Close'], label='Actual Price')
    plt.plot(df['timestamp'], df['Predictions'], label='Predicted Price', linestyle='--')
    plt.title('Actual vs Predicted Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot_results('data/processed/engineered_features.csv', 'models/linear_regression_model.pkl')
