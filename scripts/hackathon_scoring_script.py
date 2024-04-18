from hackathon_data.excel_utils import create_excel_workbook
from hackathon_data.file_utils import load_user_data_from_url, load_scoring_data_from_url
from hackathon_data.helpers import prepare_results_data

def main():
    # URLs for scoring and usernames data
    scoring_url = "https://raw.githubusercontent.com/chrisbirie/UA-Hackathon-2024-Coding-Track/main/scoring.csv"
    usernames_url = "https://raw.githubusercontent.com/chrisbirie/UA-Hackathon-2024-Coding-Track/main/codewars_usernames_test.csv"

    # Load scoring data from URL
    scoring_data = load_scoring_data_from_url(scoring_url)

    # Load user data from URL
    user_data = load_user_data_from_url(usernames_url)

    data = prepare_results_data(user_data, scoring_data)

    # Create Excel workbook
    filename = "data/hackathon_scores.xlsx"
    workbook = create_excel_workbook(filename, data)

if __name__ == "__main__":
    main()