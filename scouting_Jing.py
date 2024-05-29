import pathlib
import gspread
import time
file_path=pathlib.Path(__file__)
json_path=pathlib.Path(file_path).parent/"scouting-jing-4c9747d8a2c5.json"
account=gspread.servise_account(json_path)
sheet=account.open("open")
all=sheet.worksheet("All")

team=None
def data(inf):
    line = inf.acell("Q1").value
    inf.update('A'+line,all.acell("B2").value)
    inf.update('C'+line,int(all.acell("D2").value))
    inf.update('D'+line,all.acell("E2").value)
    inf.update('E'+line,all.acell("F2").value)
    inf.update('G'+line,all.acell("H2").value)
    inf.update('H'+line,int(all.acell("I2").value))
    inf.update('I'+line,int(all.acell("J2").value))
    inf.update('J'+line,int(all.acell("K2").value))
    inf.update('K'+line,int(all.acell("L2").value))
    inf.update('L'+line,all.acell("M2").value)
    inf.update('M'+line,all.acell("N2").value)
    inf.update('N'+line,int(all.acell("O2").value))
    inf.update('O'+line,all.acell("P2").value)
    inf.update('P'+line,all.acell("Q2").value)
    inf.update('Q1',int(l)+1)