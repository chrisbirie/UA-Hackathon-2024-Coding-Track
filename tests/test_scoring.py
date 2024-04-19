import unittest
from hackathon_data.scoring import calculate_score

class TestCalculateScore(unittest.TestCase):

    # Happy path test
    def test_calculate_score_with_matching_rank(self):
        # Arrange
        rank_name = "Gold"
        scoring_data = [{'rank': 'Bronze' , 'score': 10},{'rank': 'Silver', 'score': 20},{'rank': 'Gold', 'score': 30}]
        
        # Act
        score = calculate_score(rank_name, scoring_data)
        
        # Assert
        self.assertEqual(score, 30, "ID: HappyPath-MatchingRank")

    # Edge case test: rank_name not in scoring_data
    def test_calculate_score_without_matching_rank(self):
        # Arrange
        rank_name = "Platinum"
        scoring_data = [{'rank': 'Bronze' , 'score': 10},{'rank': 'Silver', 'score': 20},{'rank': 'Gold', 'score': 30}]
        
        # Act
        score = calculate_score(rank_name, scoring_data)
        
        # Assert
        self.assertEqual(score, 0, "ID: EdgeCase-NoMatchingRank")

    # Edge case test: Empty scoring_data
    def test_calculate_score_empty_scoring_data(self):
        # Arrange
        rank_name = "Gold"
        scoring_data = []
        
        # Act
        score = calculate_score(rank_name, scoring_data)
        
        # Assert
        self.assertEqual(score, 0, "ID: EdgeCase-EmptyScoringData")

if __name__ == '__main__':
    unittest.main()