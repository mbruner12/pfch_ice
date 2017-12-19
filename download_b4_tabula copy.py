#we want to load the beautiful soup module that we installed so we can use it in our script
#the module is named bs4 and it has multiple parts, but we just want to use the BeautifulSoup part
from bs4 import BeautifulSoup
from tabula import read_pdf
 
#we also want to have a way to talk to the internet so we need the request module too
import requests, re
 
#here is the URL to the browse foia pages
all_urls = "https://www.ice.gov/foia/library" 
#lets ask requests to get that page, we can turn off the SSL too
foia_page = requests.get(all_urls, verify=False)

#we are storing the HTML of the page into the variable page_html using the .text attribute of the request result
page_html = foia_page.text
#now we are going to ask BS to parse the page
soup = BeautifulSoup(page_html, "html.parser")


#prints all links
all_links = soup.find_all("a",href=re.compile("icefoialogs"))
#get links with "icefoialogs"

for save_file in all_links:
#replace / with - and use that as a file name
#split to make url title of pdf, split it on the /
	new_name = save_file["href"].split("/")[-1]
	# print (save_file.text)
	print("downloading", new_name)
	r = requests.get(save_file["href"], stream=True, verify=False)
	if r.status_code == 200:
		with open(new_name, 'wb') as f:
			for chunk in r:
				f.write(chunk)
	df = read_pdf(new_name)
	print (df)



	# r = requests.get(save_file, stream=True, verify=False)
	# with open(save_file + ".pdf", 'wb') as f:
	
	# f.write(save_file)

#replace / with - and use that as a file name
#split to make url title of pdf, split it on the /