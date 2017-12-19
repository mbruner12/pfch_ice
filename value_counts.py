import pandas as pd
from pandas.io.json import json_normalize

#company(trac)
ftw = pd.read_json('foia_data.json', orient='rows')
closer = pd.DataFrame.transpose(ftw)
trac_page = pd.io.json.json_normalize(closer)

print(trac_page)

# print(get_it_right['Company'].value_counts())
# print(get_it_right['Company','Disposition'])

# we = pd.read_excel('')



# # company(ice logs)
# another_one = pd.read_excel('201512.xlsx')
# print(another_one)


# Kind of record
# print(get_it_right['Description'].value_counts())

