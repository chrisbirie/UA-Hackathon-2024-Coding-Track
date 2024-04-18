from hackathon_data.codewars_api import get_user_data, get_challenge_data
from hackathon_data.scoring import calculate_score
from datetime import datetime 

def prepare_results_data(user_data, scoring_data):
    user_data = user_data[1:]  # Skips the first row (header)
    scoring_data = scoring_data[1:]  # Skips the first row (header)
    data = []

    for user in user_data:
        # Get user data from CodeWars API
        user_completed_challenges = get_user_data(user['username'])
        # Get completed challenges data for the user
        completed_challenges = user_completed_challenges.get('data', [])
        for challenge in completed_challenges:
            # Get challenge details from CodeWars API
            challenge_info = get_challenge_data(challenge['id'])
            # Extract relevant challenge data
            challenge_name = challenge_info.get('name', '')
            completed_languages = challenge.get('completedLanguages', [])
            end_time = format_datetime(challenge.get('completedAt', ''))
            rank = challenge_info.get('rank', {})
            rank_name = rank.get('name','')

            # Calculate score for the challenge
            score = calculate_score(rank_name, scoring_data)
        
            # Append data to excel_data list
            data.append((user['username'], user['full_name'], challenge_name, ', '.join(completed_languages), end_time, rank_name, score))

    
    return data

def format_datetime(in_date):
    if in_date == '':
        return in_date

    date_time_object = datetime.strptime(in_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_date_time = date_time_object.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_date_time