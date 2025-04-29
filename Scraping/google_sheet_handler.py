import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_SHEETS_CREDENTIALS_FILE, SHEET_NAME

def setup_google_sheet():
    #
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(GOOGLE_SHEETS_CREDENTIALS_FILE, scopes=scope)
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1
    sheet.clear()
    sheet.append_row(["Title", "Company", "Experience", "Salary", "Location", "Posted Date", "Link", "Job Description", "Resume"])
    return sheet

# def get_job_descriptions():
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     creds = Credentials.from_service_account_file(GOOGLE_SHEETS_CREDENTIALS_FILE, scopes=scope)
#     client = gspread.authorize(creds)

#     sheet = client.open(SHEET_NAME).sheet1
#     job_descriptions = sheet.col_values(8)  # Assuming job description is column 8
#     return job_descriptions