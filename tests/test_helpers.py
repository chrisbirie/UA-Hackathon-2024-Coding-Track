import unittest
from unittest.mock import patch
from datetime import datetime
from hackathon_data.helpers import prepare_results_data, format_datetime
from hackathon_data.codewars_api import get_user_data, get_challenge_data

class TestPrepareResultsData(unittest.TestCase):
    @patch('hackathon_data.helpers.get_user_data')
    @patch('hackathon_data.helpers.get_challenge_data')
    @patch('hackathon_data.helpers.calculate_score')
    @patch('hackathon_data.helpers.format_datetime')
    def test_prepare_results_data(self, mock_format_datetime, mock_calculate_score, mock_get_challenge_data, mock_get_user_data):
        # Mock user data and challenges
        user_data = [{'username': 'user1', 'full_name': 'User One'}, {'username': 'user2', 'full_name': 'User Two'}]
        scoring_data = [{'rank': '8 kyu', 'score': '5'}]
        completed_challenge_data = {'data': [{'id': 'challenge1', 'completedAt': '2023-04-01T12:00:00.399Z', 'completedLanguages':['javascript','java']}]}
        challenge_data = {'name': 'challenge1', 'rank': {'name': '8 kyu'}}
        # Mock API responses
        mock_get_user_data.return_value = completed_challenge_data
        mock_get_challenge_data.return_value = challenge_data
        mock_format_datetime.side_effect = self.mock_format_datetime
        mock_calculate_score.return_value = 5  # Mocking score calculation

        # Call the function under test
        result = prepare_results_data(user_data, scoring_data)
        print(result)
        # Assert the result
        expected_result = [
           # ('user1', 'User One', 'challenge1', 'javascript, java', '2023-04-01 12:00:00', '8 kyu', 5),
            ('user2', 'User Two', 'challenge1', 'javascript, java', '2023-04-01 12:00:00', '8 kyu', 5)  ]
        self.assertEqual(result, expected_result)

    def mock_format_datetime(self, in_date):
        return datetime.strptime(in_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")


    def test_format_datetime(self):
        self.assertEqual(format_datetime('2023-04-01T12:00:00.399Z'), '2023-04-01 12:00:00')
        self.assertEqual(format_datetime(''), '')

if __name__ == '__main__':
    unittest.main()