def calculate_score(rank_name, scoring_data):

    # Example scoring criteria: Assuming scoring_data contains tuples (rank_name, rank_score)
    for item in scoring_data:
        # Example: If the user's rank matches the scoring criteria, add the corresponding score
        if item['rank'] == rank_name:
            return int(item['score'])

    return 0