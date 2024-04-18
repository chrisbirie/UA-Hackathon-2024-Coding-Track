import csv
import requests 

def download_csv_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

def load_scoring_data_from_url(url):
    csv_text = download_csv_from_url(url)
    scoring_data = []
    for row in csv.reader(csv_text.splitlines()):
        rank, score = row
        scoring_data.append({'rank': rank, 'score': score})
    return scoring_data

def load_user_data_from_url(url):
    csv_text = download_csv_from_url(url)
    user_data = []
    for row in csv.reader(csv_text.splitlines()):
        username, full_name = row
        user_data.append({'username': username, 'full_name': full_name})
    return user_data