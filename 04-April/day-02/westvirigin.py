url = "https://ohflac.wvdhhr.org/Apps/Lookup/FacilitySearch"

import requests
from bs4 import BeautifulSoup
result = requests.get(url)

print(result.status_code)
c = result.content

soup = BeautifulSoup(c, "lxml")

#print(soup.findAll(id="content"))

#print(soup.head)

#print(soup.findAll('state'))

#print(soup.find_all('state'))
print(soup.text)

#Trying to download rosters using Pything
#Website is built using asp.Net
