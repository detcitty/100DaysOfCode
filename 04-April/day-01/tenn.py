url = "https://apps.health.tn.gov/FacilityListings"
import requests
from bs4 import BeautifulSoup
result = requests.get(url)

print(result.status_code)
c = result.content

soup = BeautifulSoup(c, "lxml")
