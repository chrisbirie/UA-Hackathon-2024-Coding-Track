import unittest
from unittest.mock import Mock, patch
import requests
from hackathon_data.codewars_api import get_user_data, get_challenge_data

class TestCodewarsAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data_success(self, mock_get):
        completed_challenges = {"totalPages":1,"totalItems":1,"data":[{"id":"514b92a657cdc65150000006","name":"Multiples of 3 and 5","slug":"multiples-of-3-and-5","completedAt":"2017-04-06T16:32:09Z","completedLanguages":["javascript","coffeescript","ruby","javascript","ruby","javascript","ruby","coffeescript","javascript","ruby","coffeescript"]}]}
        mock_get.return_value.json.return_value = completed_challenges
        # Call the function with a mock challenge ID
        response = get_user_data("514b92a657cdc65150000006")

        # Assertions
        self.assertEqual(response, completed_challenges)
        
    @patch('requests.get')
    def test_get_user_data_connection_issue(self, mock_get):
        mock_get.side_effect = requests.RequestException("Connection error")

        result = get_user_data("mock_username")

        self.assertEqual(result, {})
        
    @patch('requests.get')
    def test_get_challenge_data_success(self, mock_get):
        mock_response = {"id":"5277c8a221e209d3f6000b56","name":"Valid Braces","slug":"valid-braces","url":"http://www.codewars.com/kata/valid-braces","category":"algorithms","description":"Write a function called `validBraces` that takes a string ...","tags":["Algorithms","Validation","Logic","Utilities"],"languages":["javascript","coffeescript"],"rank":{"id":-4,"name":"4 kyu","color":"blue"},"createdBy":{"username":"xDranik","url":"http://www.codewars.com/users/xDranik"},"approvedBy":{"username":"xDranik","url":"http://www.codewars.com/users/xDranik"},"totalAttempts":4911,"totalCompleted":919,"totalStars":12,"voteScore":512,"publishedAt":"2013-11-05T00:07:31Z","approvedAt":"2013-12-20T14:53:06Z"}
        mock_get.return_value.json.return_value = mock_response

        # Call the function with a mock challenge ID
        result = get_challenge_data("5277c8a221e209d3f6000b56")

        # Assertions
        self.assertEqual(result, mock_response)
        
    @patch('requests.get')
    def test_get_challenge_data_connection_issue(self, mock_get):
        mock_get.side_effect = requests.RequestException("Connection error")

        result = get_challenge_data("mock_username")

        self.assertEqual(result, {})