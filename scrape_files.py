from bs4 import BeautifulSoup
import pandas as pd
import glob, json

all_data = {}

file_names = glob.glob('*.html')

total = len(file_names)

counter = 0

for file in file_names:
	with open(file) as a_html:
		text = a_html.read()
		counter = counter + 1
		print("Working on" + file)
		print (counter,"of",total)
		soup = BeautifulSoup(text, 'html.parser') 		
		table = soup.find('table')
		if table != None:
			data_dict = {}
			for a_row in table.find_all('tr'):
				columns = a_row.find_all('td')
				data_dict[columns[0].get_text()] = columns[1].get_text().strip()
				new_entry = {file:data_dict}
				all_data.update(new_entry)

json.dump(all_data,open('foia_data.json','w'),indent=4)
		

# table = soup.find_all('tr')
# 		data_dict = {}
# 		print(table)
# 		for a_row in table.find_all('td'):
# 			# columns = a_row.find_all('td')
# 			data_dict[a_row[0].get_text()] = a_row[1].get_text().strip()
# 		print(data_dict) 
		



		# table = soup.find('table')
		# data_dict = {}
		# for a_row in table.find_all('tr'):
		# 	columns = a_row.find_all('td')
		# 	data_dict[columns[0].get_text()] = columns[1].get_text().strip()
		# print(data_dict) 
		
