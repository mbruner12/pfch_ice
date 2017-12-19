from bs4 import BeautifulSoup
import requests, re, json, os
 
#here is the URL to the browse collection pages
start_url = 'https://www.immigrantjustice.org/issues/transparencyandhumanrights#Facility docs'
#lets ask requests to get that page, we can turn off the SSL too
collection_page = requests.get(start_url, verify=False)

urls = ['https://www.immigrantjustice.org/issues/transparencyandhumanrights/adelanto-ca-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/albany-county-ny','https://www.immigrantjustice.org/issues/transparencyandhumanrights/baker-county-fl','https://www.immigrantjustice.org/issues/transparencyandhumanrights/bedford-heights-oh','https://www.immigrantjustice.org/issues/transparencyandhumanrights/bergen-county-nj','https://www.immigrantjustice.org/issues/transparencyandhumanrights/berks-county-pa','https://www.immigrantjustice.org/issues/transparencyandhumanrights/boone-county-ky','https://www.immigrantjustice.org/issues/transparencyandhumanrights/bristol-county-ma','https://www.immigrantjustice.org/issues/transparencyandhumanrights/broward-transitional-facility-fl-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/buffalo-federal-detention-facility-ny','https://www.immigrantjustice.org/issues/transparencyandhumanrights/butler-county-oh','https://www.immigrantjustice.org/issues/transparencyandhumanrights/butler-county-ks','https://www.immigrantjustice.org/issues/transparencyandhumanrights/caldwell-county-mo','https://www.immigrantjustice.org/issues/transparencyandhumanrights/calhoun-county-mi','https://www.immigrantjustice.org/issues/transparencyandhumanrights/cambria-county-pa','https://www.immigrantjustice.org/issues/transparencyandhumanrights/carver-county-mn','https://www.immigrantjustice.org/issues/transparencyandhumanrights/cass-county-ne','https://www.immigrantjustice.org/issues/transparencyandhumanrights/central-arizona-detention-center-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/charleston-county-sc-sheriff-al-cannon-detention-center','https://www.immigrantjustice.org/issues/transparencyandhumanrights/chase-county-ks','https://www.immigrantjustice.org/issues/transparencyandhumanrights/cibola-county-correctional-center-nm','https://www.immigrantjustice.org/issues/transparencyandhumanrights/clinton-county-pa','https://www.immigrantjustice.org/issues/transparencyandhumanrights/contra-costa-county-ca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/dekalb-county-al','https://www.immigrantjustice.org/issues/transparencyandhumanrights/delaney-hall-nj','https://www.immigrantjustice.org/issues/transparencyandhumanrights/dodge-county-wi','https://www.immigrantjustice.org/issues/transparencyandhumanrights/douglas-county-ne','https://www.immigrantjustice.org/issues/eastern-regional-jail-west-virginia','https://www.immigrantjustice.org/issues/transparencyandhumanrights/east-hidalgo-tx','https://www.immigrantjustice.org/issues/transparencyandhumanrights/el-centro-service-processing-center-ca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/el-paso-county-co','https://www.immigrantjustice.org/issues/transparencyandhumanrights/el-paso-service-processing-center-tx','https://www.immigrantjustice.org/issues/transparencyandhumanrights/elizabeth-contract-detention-facility-nj-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/eloy-az-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/essex-county-nj','https://www.immigrantjustice.org/issues/transparencyandhumanrights/etowah-county-al','https://www.immigrantjustice.org/issues/transparencyandhumanrights/florence-correctional-center-az-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/florence-service-processing-center-az','https://www.immigrantjustice.org/issues/transparencyandhumanrights/frederick-county-md','https://www.immigrantjustice.org/issues/transparencyandhumanrights/franklin-county-ma','https://www.immigrantjustice.org/issues/transparencyandhumanrights/freeborn-mn','https://www.immigrantjustice.org/issues/transparencyandhumanrights/glades-county-fl','https://www.immigrantjustice.org/issues/hall-county-ne','https://www.immigrantjustice.org/issues/transparencyandhumanrights/hardin-county-ia','https://www.immigrantjustice.org/issues/transparencyandhumanrights/henderson-county-nc','https://www.immigrantjustice.org/issues/transparencyandhumanrights/houston-contract-detention-facility-tx-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/howard-county-md','https://www.immigrantjustice.org/issues/transparencyandhumanrights/hudson-county-nj','https://www.immigrantjustice.org/issues/transparencyandhumanrights/hutto-correctional-center-tx-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/immigration-centers-america-farmville-va','https://www.immigrantjustice.org/issues/transparencyandhumanrights/irwin-county-ga','https://www.immigrantjustice.org/issues/transparencyandhumanrights/jack-harwell-detention-center-tx','https://www.immigrantjustice.org/issues/transparencyandhumanrights/james-musick-facility-ca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/joe-corley-detention-centermontgomery-county-tx','https://www.immigrantjustice.org/issues/transparencyandhumanrights/johnson-county-tx','https://www.immigrantjustice.org/issues/kankakee-county-il','https://www.immigrantjustice.org/issues/transparencyandhumanrights/karnes-county-tx-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/kenosha-county-wi','https://www.immigrantjustice.org/issues/transparencyandhumanrights/koegh-dwyer-correctional-facility-nj','https://www.immigrantjustice.org/issues/transparencyandhumanrights/krome-service-processing-center-fl','https://www.immigrantjustice.org/issues/transparencyandhumanrights/laredo-processing-center-tx-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/lasalle-county-tx','https://www.immigrantjustice.org/issues/transparencyandhumanrights/mchenry-county-il','https://www.immigrantjustice.org/issues/transparencyandhumanrights/mesa-verde-ca-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/monroe-county-mi','https://www.immigrantjustice.org/issues/transparencyandhumanrights/monroe-county-fl','https://www.immigrantjustice.org/issues/transparencyandhumanrights/morgan-county-mo','https://www.immigrantjustice.org/issues/transparencyandhumanrights/morrow-county-oh','https://www.immigrantjustice.org/issues/transparencyandhumanrights/northwest-detention-center-wa-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/orange-county-fl','https://www.immigrantjustice.org/issues/transparencyandhumanrights/orange-county-ny','https://www.immigrantjustice.org/issues/transparencyandhumanrights/otero-county-prison-facility-nm','https://www.immigrantjustice.org/issues/transparencyandhumanrights/otero-county-processing-center-nm','https://www.immigrantjustice.org/issues/transparencyandhumanrights/pike-county-pa','https://www.immigrantjustice.org/issues/transparencyandhumanrights/plymouth-county-ma','https://www.immigrantjustice.org/issues/transparencyandhumanrights/polk-county-ia','https://www.immigrantjustice.org/issues/transparencyandhumanrights/polk-county-tx','https://www.immigrantjustice.org/faq/port-isabel-service-processing-center-tx-ahtna-inc','https://www.immigrantjustice.org/issues/transparencyandhumanrights/pulaski-county-jail-il-formerly-tri-county-jail','https://www.immigrantjustice.org/issues/transparencyandhumanrights/ramsey-county-mn','https://www.immigrantjustice.org/issues/transparencyandhumanrights/rice-county-ks','https://www.immigrantjustice.org/issues/transparencyandhumanrights/sacramento-county-ca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/rolling-plains-tx','https://www.immigrantjustice.org/issues/transparencyandhumanrights/san-diegootay-mesa-contract-detention-facility-ca-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/santa-ana-ca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/seneca-county-oh','https://www.immigrantjustice.org/issues/transparencyandhumanrights/sherburne-county-mn','https://www.immigrantjustice.org/issues/transparencyandhumanrights/south-louisiana-detention-center-la-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/south-texas-detention-complex-tx-geo-group','https://www.immigrantjustice.org/issues/transparencyandhumanrights/st-clair-mi','https://www.immigrantjustice.org/issues/transparencyandhumanrights/stewart-county-ga-cca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/strafford-county-nh','https://www.immigrantjustice.org/issues/transparencyandhumanrights/suffolk-county-ma','https://www.immigrantjustice.org/issues/transparencyandhumanrights/tensas-parish-la','https://www.immigrantjustice.org/issues/transparencyandhumanrights/theo-lacy-facility-ca','https://www.immigrantjustice.org/issues/transparencyandhumanrights/tulsa-county-ok','https://www.immigrantjustice.org/issues/transparencyandhumanrights/utah-county-ut','https://www.immigrantjustice.org/issues/transparencyandhumanrights/wakulla-county-fl','https://www.immigrantjustice.org/issues/transparencyandhumanrights/worcester-county-md','https://www.immigrantjustice.org/issues/transparencyandhumanrights/york-county-pa','https://www.immigrantjustice.org/issues/transparencyandhumanrights/yuba-county-ca']

 
# all_item_divs = soup.find_all('h5')
# for a_div in all_item_divs:
#       # find the first <a> link
#       item = a_div.find("a")
#       if item == None:
#          print("Not here!")
#       else:
#          lets_go = item['href']
#          if lets_go == None:
#            print("Not here!")
#          else:
#             base_url = 'http://www.immigrantjustice.org'
#             full_url = base_url + lets_go
#             urls.append(full_url)
#             urls = list(set(urls))

doc_links = []

for source in urls:
  doc_page = requests.get(source, verify=False)
  page_html = doc_page.text
  soup = BeautifulSoup(page_html, 'html.parser')
  link = soup.find('noscript')
  messy_link = link.find('a')
  # link = soup.find('div', attrs = {"class":"DC-paginator-description"})
  print(source)
  print(messy_link['href'])
  doc_links.append(messy_link['href'])


print(doc_links)
     # with open(id_page +'.html','w') as whatever:
     #   		whatever.write(three_page.text)

# if os.path.exists(id_page +'.html'):
#      print("fit for buisness:", a_page) 
#   else:
#      three_page = requests.get(id_page, verify=False)
#      with open(id_page +'.html','w') as whatever:
#           whatever.write(three_page.text)

      
      # open a file / new directory
      # find "how do I check whther a file exists using Python" to not duplicate files if it crashes
      #  f
    
 
# 'https://www.immigrantjustice.org/issues/transparencyandhumanrights/denver-contract-detention-facility-co-geo-group'

# 'https://www.immigrantjustice.org/issues/transparencyandhumanrights/south-texas-dilley-family-detention-center',



# print(urls)
# # for get_links in urls:
# # 	one_item = requests.get(get_links, verify=False)
# # 	a_page_html = one_item.text
# # 	soup = BeautifulSoup(a_page_html, 'html.parser')
# # 	doc = soup.find_all('noscript')
# # 	print(doc)  
       



# # 