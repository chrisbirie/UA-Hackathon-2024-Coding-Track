import unittest
from unittest.mock import patch, Mock
from hackathon_data.file_utils import load_scoring_data_from_url, load_user_data_from_url

class FakeResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass
    
class TestScoringAndUserDataLoading(unittest.TestCase):
    @patch('hackathon_data.file_utils.requests.get')
    def test_load_scoring_data_from_url(self, mock_get):
        # Mocking the response from requests.get
        mock_response = FakeResponse("rank,score\nvalue1,10\nvalue2,20\n")
        mock_get.return_value = mock_response

        # Testing the function
        scoring_url = "https://example.com/scoring.csv"
        scoring_data = load_scoring_data_from_url(scoring_url)

        # Assertions
        self.assertEqual(len(scoring_data), 3)
        self.assertEqual(scoring_data[0], {'rank': 'rank', 'score': 'score'})
        self.assertEqual(scoring_data[1], {'rank': 'value1', 'score': '10'})
        self.assertEqual(scoring_data[2], {'rank': 'value2', 'score': '20'})

    @patch('hackathon_data.file_utils.requests.get')
    def test_load_user_data_from_url(self, mock_get):
        # Mocking the response from requests.get
        mock_response = FakeResponse("username,full_name\nuser1,John Doe\nuser2,Jane Doe\n")
        mock_get.return_value = mock_response

        # Testing the function
        user_url = "https://example.com/users.csv"
        user_data = load_user_data_from_url(user_url)

        # Assertions
        self.assertEqual(len(user_data), 3)
        self.assertEqual(user_data[0], {'username': 'username', 'full_name': 'full_name'})
        self.assertEqual(user_data[1], {'username': 'user1', 'full_name': 'John Doe'})
        self.assertEqual(user_data[2], {'username': 'user2', 'full_name': 'Jane Doe'})

if __name__ == '__main__':
    unittest.main()