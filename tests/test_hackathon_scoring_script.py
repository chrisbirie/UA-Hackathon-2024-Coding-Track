import os
import unittest
from unittest.mock import patch
from scripts.hackathon_scoring_script import main

class TestMainFunction(unittest.TestCase):
    @patch("scripts.hackathon_scoring_script.load_scoring_data_from_url")
    @patch("scripts.hackathon_scoring_script.load_user_data_from_url")
    @patch("scripts.hackathon_scoring_script.prepare_results_data")
    @patch("scripts.hackathon_scoring_script.create_excel_workbook")
    def test_main_function(self, mock_create_excel, mock_prepare_results, mock_load_user_data, mock_load_scoring_data):
        # Define mock return values
        scoring_data = {"key": "value"}  # Example dictionary for scoring data
        user_data = {"username": "John"}  # Example dictionary for user data
        results_data = [{"key": "value"}]  # Example list of dictionaries for results data

        # Set return values for mock functions
        mock_load_scoring_data.return_value = scoring_data
        mock_load_user_data.return_value = user_data
        mock_prepare_results.return_value = results_data

        # Call the main function
        main()

        # Check if the functions were called with the correct arguments
        mock_load_scoring_data.assert_called_once_with("https://raw.githubusercontent.com/chrisbirie/UA-Hackathon-2024-Coding-Track/main/scoring.csv")
        mock_load_user_data.assert_called_once_with("https://raw.githubusercontent.com/chrisbirie/UA-Hackathon-2024-Coding-Track/main/codewars_usernames_test.csv")
        mock_prepare_results.assert_called_once_with(user_data, scoring_data)
        mock_create_excel.assert_called_once_with("data/hackathon_scores.xlsx", results_data)

if __name__ == '__main__':
    unittest.main()