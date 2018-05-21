import bs4
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://bulawayo24.com/latest'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
Allheadlines=page_soup.find_all("div",{"class":"list_holder"})
for headerr in Allheadlines:
	headlines=headerr.h3.text
	print(headlines)
    
my_link = 'https://www.masvingomirror.com/search/label/Local%20News'
uEmma = uReq(my_link)
page_htmll = uEmma.read()
uEmma.close()
page_emma = soup(page_htmll,"html.parser")
masvingoHeadlines = page_emma.find_all("h2",{"class":"post-body entry-content"})
masHead = masvingoHeadlines[0]
print(masHead)




