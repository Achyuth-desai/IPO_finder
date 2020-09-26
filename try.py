from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

url = "https://www.nyse.com/ipo-center/recent-ipo"
driver = webdriver.Firefox()
driver.get(url)

time.sleep(2)

list_header = ""
data = ""
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.close()

f = open("new.csv", "w", encoding="utf-8")

header = soup.find_all("table")[0].find('tr')

for items in header:
	try:
		list_header = list_header + items.get_text() + ","
	except:
		continue
f.write(list_header)
f.write("\n")

HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for tr in HTML_data:
	td = tr.find_all("td")
	for element in td:
		try:
			data = element.get_text().replace(",", "|") + ","
			f.write(data)
		except:
			continue
	f.write("\n")
f.close()
import comp_final
os.remove("old.csv")
os.rename("new.csv", "old.csv")
import mail