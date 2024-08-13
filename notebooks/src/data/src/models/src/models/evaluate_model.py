import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

def evaluate_model(data_path, model_path):
    df = pd.read_csv(data_path)
    
    # Features and target
    X = df[['Moving_Avg', 'Returns']]
    y = df['Close']
    
    # Load the trained model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Predictions
    predictions = model.predict(X)
    
    # Evaluation
    mse = mean_squared_error(y, predictions)
    print(f"Mean Squared Error: {mse}")

if __name__ == '__main__':
    evaluate_model('data/processed/engineered_features.csv', 'models/linear_regression_model.pkl')
