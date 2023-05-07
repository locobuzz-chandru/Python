import pandas as pd
from datetime import datetime

parser = lambda x: pd.to_datetime(x, format='%d-%m-%Y %H:%M:%S')
df = pd.read_csv('People_data.csv', date_parser=parser, parse_dates=['Birth Date'])

# df = pd.to_datetime('29-10-1987', format='%Y-%m-%d %H:%M:%S', errors='ignore')

# from datetime import datetime as dt
#
# dtm = lambda x: dt.strptime(str(x), "%d.%m.%Y")
# df = pd.read_csv('People_data.csv', dayfirst=True, parse_dates=True)
#
# df["Birth Date"] = df["Birth Date"].apply(dtm)

print(df)
