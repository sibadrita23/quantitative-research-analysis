import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_model(data_path):
    df = pd.read_csv(data_path)
    
    # Features and target
    X = df[['Moving_Avg', 'Returns']]
    y = df['Close']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the trained model
    with open('models/linear_regression_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Model trained and saved as 'linear_regression_model.pkl'")

if __name__ == '__main__':
    train_model('data/processed/engineered_features.csv')
