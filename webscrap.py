import requests
from bs4 import BeautifulSoup

r = requests.get('https://stores.airtel.in/')
 
# check status code for response received
# success code - 200
print(r)
 
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
soup1 = soup.prettify()
print(soup1)


file = open("web.txt","w+")
file.write(soup1)       