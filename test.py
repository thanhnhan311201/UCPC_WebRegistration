import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope =["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("List_of_teams")
wks = spreadsheet.worksheet("demo")

team = input("Enter team name: ")
member1 = input("Enter member 1: ")
cmnd1 = input("Enter member 1's cmnd/cccd: ")
phone1 = input("Enter member 1's phone: ")
member2 = input("Enter member 2: ")
cmnd2 = input("Enter member 2's cmnd/cccd: ")
phone2 = input("Enter member 2's phone: ")
member3 = input("Enter member 3: ")
cmnd3 = input("Enter member 3's cmnd/cccd: ")
phone3 = input("Enter member 3's phone: ")
email = input("Enter email: ")
school = input("Enter school: ")
password = input("Enter password: ")

idx = len(wks.get_all_values()) + 1
wks.update_cell(idx, 1, team)
wks.update_cell(idx, 2, email)
wks.update_cell(idx, 3, password)
wks.update_cell(idx, 4, school)
wks.update_cell(idx, 5, member1)
wks.update_cell(idx, 6, cmnd1)
wks.update_cell(idx, 7, phone1)
wks.update_cell(idx, 8, member2)
wks.update_cell(idx, 9, cmnd2)
wks.update_cell(idx, 10, phone2)
wks.update_cell(idx, 11, member3)
wks.update_cell(idx, 12, cmnd3)
wks.update_cell(idx, 13, phone3)