import gspread
from google.oauth2.service_account import Credentials

def setup_google_sheet():
    #
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file('.\\aijobagent-458205-6b2d277530a2.json', scopes=scope)
    client = gspread.authorize(creds)

    sheet = client.open("Job Applications").sheet1
    # sheet.clear()
    sheet.append_row(["Title", "Company", "Experience", "Salary", "Location", "Posted Date", "Link", "Job Description"])
    return sheet
