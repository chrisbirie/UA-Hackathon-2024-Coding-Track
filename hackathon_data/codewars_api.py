import requests

def get_user_data(username):
    url = f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed?page=0"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching user data for {username}: {e}")
        return {}

def get_challenge_data(challenge_id):
    url = f"https://www.codewars.com/api/v1/code-challenges/{challenge_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching challenge data for {challenge_id}: {e}")
        return {}