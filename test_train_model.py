import unittest
import pandas as pd
from train_model import load_and_preprocess, split_data

class TestTrainModel(unittest.TestCase):
    def test_load_and_preprocess(self):
        X, y = load_and_preprocess('parkinsons data.csv')
        self.assertNotIn('name', X.columns)
        self.assertNotIn('status', X.columns)
        self.assertEqual(len(X), len(y))

    def test_split_data(self):
        X, y = load_and_preprocess('parkinsons data.csv')
        X_train, y_train, X_test, y_test = split_data(X, y)
        self.assertEqual(len(X_train), len(X) // 2)
        self.assertEqual(len(X_test), len(X) - (len(X) // 2))

if __name__ == '__main__':
    unittest.main()
