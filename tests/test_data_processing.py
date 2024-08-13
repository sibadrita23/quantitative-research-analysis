import unittest
import pandas as pd
from src.data.preprocess_data import preprocess_data

class TestDataProcessing(unittest.TestCase):

    def test_preprocess_data(self):
        # Sample data
        data = {'timestamp': ['2022-01-01', '2022-01-02', None], 'Close': [150.0, None, 152.0]}
        df = pd.DataFrame(data)
        
        # Save the sample data
        df.to_csv('data/raw/sample.csv', index=False)
        
        # Run preprocessing
        preprocess_data('data/raw/sample.csv')
        
        # Load the processed data
        processed_df = pd.read_csv('data/processed/sample.csv')
        
        # Check if missing values were filled
        self.assertFalse(processed_df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
