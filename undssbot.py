import bs4
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'http://zimbabwe.shafaqna.com/EN/ZW'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
LatestHeadlines = page_soup.find_all("div",{"class":"news-box"})
csvfile = "Allheadlines.csv"
f = open(csvfile,"w")
header = "Allheadlines, Source, \n"
f.write(header)
header = LatestHeadlines[0]
for header in LatestHeadlines:
    Allheadlines = header.h2.text
    Source = header.span.i.text
    print("Headline :" + Allheadlines)
    print("NewsSource : " + Source)
    f.write(Allheadlines + "," + Source +"," + "\n")
f.close()
