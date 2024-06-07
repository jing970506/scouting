import pathlib
import gspread
import time
file_path=pathlib.Path(__file__)
json_path=pathlib.Path(file_path).parent.parent/"scouting-jing-4c9747d8a2c5.json"
account=gspread.service_account(json_path)
sheet=account.open("scouting")
aii=sheet.worksheet("All")

team=None
def data(inf):
    global aii
    line = inf.acell("Q1").value
    inf.update('A'+line,aii.acell("B2").value)
    inf.update('C'+line,int(aii.acell("D2").value))
    inf.update('D'+line,aii.acell("E2").value)
    inf.update('E'+line,aii.acell("F2").value)
    inf.update('G'+line,aii.acell("H2").value)
    inf.update('H'+line,int(aii.acell("I2").value))
    inf.update('I'+line,int(aii.acell("J2").value))
    inf.update('J'+line,int(aii.acell("K2").value))
    inf.update('K'+line,int(aii.acell("L2").value))
    inf.update('L'+line,aii.acell("M2").value)
    inf.update('M'+line,aii.acell("N2").value)
    inf.update('N'+line,int(aii.acell("O2").value))
    inf.update('O'+line,aii.acell("P2").value)
    inf.update('P'+line,aii.acell("Q2").value)
    inf.update('Q1',int(line)+1)
while True:
    team = aii.acell('A2').value
    if team!=None:
        data(sheet.worksheet(team))
        aii.delete_rows(2)
        time.sleep(20)
    else:
        print("沒有比賽")
        time.sleep(5)
    print(0)