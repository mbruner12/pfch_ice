import pandas as pd

files = ['012016.xlsx',
 '022016.xlsx',
 '032016.xlsx',
 '042016.xlsx',
 '052016.xlsx',
 '062016.xlsx',
 '072016.xlsx',
 '082016.xlsx',
 '092016.xlsx',
 '102016.xlsx',
 '112016.xlsx',
 '122016.xlsx',
 '201501.xlsx',
 '201502.xlsx',
 '201503.xlsx',
 '201504.xlsx',
 '201505.xlsx',
 '201506.xlsx',
 '201507.xlsx',
 '201508.xlsx',
 '20150901through0915.xlsx',
 '20150916through0930.xlsx',
 '201510through201511.xlsx',
 '201512.xlsx']

all_data = pd.DataFrame()

for f in files:
    ice_logs = pd.read_excel(f)
    pretty_log = ice_logs.rename(columns={c: c.replace(' ','_') for c in ice_logs.columns})
    all_data = all_data.append(pretty_log)

all_data.set_index('Request_ID', inplace=True)
print(all_data.head())
