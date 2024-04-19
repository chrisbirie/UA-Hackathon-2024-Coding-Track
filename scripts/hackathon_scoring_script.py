from hackathon_data.excel_utils import create_excel_workbook
from hackathon_data.file_utils import load_user_data_from_url, load_scoring_data_from_url
from hackathon_data.helpers import prepare_results_data
from datetime import datetime

def main():
    # URLs for scoring and usernames data
    scoring_url = "https://raw.githubusercontent.com/chrisbirie/UA-Hackathon-2024-Coding-Track/main/assets/files/scoring.csv"
    usernames_url = "https://raw.githubusercontent.com/chrisbirie/UA-Hackathon-2024-Coding-Track/main/assets/files/codewars_usernames.csv"

    # Load scoring data from URL
    scoring_data = load_scoring_data_from_url(scoring_url)

    # Load user data from URL
    user_data = load_user_data_from_url(usernames_url)

    start_time = datetime(2024, 4, 19, 9, 0, 0)
    end_time = datetime(2024, 4, 19, 23, 59)
    data = prepare_results_data(user_data, scoring_data, start_time, end_time)

    # Create Excel workbook
    filename = "data/hackathon_scores.xlsx"
    workbook = create_excel_workbook(filename, data)

if __name__ == "__main__":
    main()
