import re, csv

with open("allcontents.csv","r") as a_open_file:
	for a_line in a_open_file:
		p = re.compile('([0-9]{4})')
		m = p.findall(a_line)
		print ("Year:",m)



# #compile our pattern
# p = re.compile('([0-9]{4})')

# #search method
# m = p.findall(our_text)
