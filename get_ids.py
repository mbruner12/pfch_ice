from bs4 import BeautifulSoup
import requests, re, json



all_ids = []
all_names = ['icefoia1.json', 'icefoia2.json', 'icefoia3.json', 'icefoia4.json', 'icefoia5.json',
'icefoia6.json', 'icefoia7.json', 'icefoia8.json', 'icefoia9.json']

#all_names = list of file na

for file_name in all_names:
	print ('working on', file_name, len(all_ids))
	with open(file_name) as data_file:    
	    data = json.load(data_file)
	    for v in data:
	        a_id = v['id']
	        if a_id not in all_ids:
	        	all_ids.append(a_id)

# # print(all_ids)

# with open('all_ids.txt','w') as whatever:
# 	whatever.write(all_ids)
json.dump(all_ids,open('all_ids','w'),indent=4)

