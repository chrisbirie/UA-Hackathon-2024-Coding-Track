def calculate_score(rank_name, scoring_data):
    final_score = 0

    # Example scoring criteria: Assuming scoring_data contains tuples (rank_name, rank_score)
    for name, score in scoring_data:
        # Example: If the user's rank matches the scoring criteria, add the corresponding score
        if name == rank_name:
            final_score = score

    return final_score