import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

scope =["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("List_of_teams")
wks = spreadsheet.worksheet("demo")

idx = f'A{str(len(wks.get_all_values()) + 1)}'
information = np.array([['ACB', 'Thanhf Nhaan', 'Demo', '123', '123', '123', '123', '123', '123', '123', '123', '123']])
wks.update(idx, information.tolist())