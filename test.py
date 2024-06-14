import read_data
import unittest
import constants
from os import listdir
class TestParkinsonsDetection(unittest.TestCase):

    def test_read_data_from_csv_raises_type_error(self):

        self.assertRaises(TypeError, read_data.read_from_csv_to_data, 2)

    def test_read_data_from_csv_raises_file_not_found_error(self):
    
        self.assertRaises(FileNotFoundError, read_data.read_from_csv_to_data, "2")

    def test_read_data_from_csv_returns_2d_list(self):

        result = read_data.read_from_csv_to_data(constants.DATA_FILE)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)
