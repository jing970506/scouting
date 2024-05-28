import pathlib
import gspread
import time
file_path=pathlib.Path(__file__)
json_path=pathlib.Path(file_path).parent/"scouting-jing-4c9747d8a2c5.json"
account=gspread.servise_account(json_path)
sheet=account.open("open")
all=sheet.worksheet("All")

team=None