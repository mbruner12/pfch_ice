import pandas as pd

#company(trac)
ftw = pd.read_json('foia_data.json', orient='rows')
get_it_right = pd.DataFrame.transpose(ftw)
print(get_it_right.sort_values(by=['Outcome Type']))