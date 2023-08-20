from bs4 import BeautifulSoup
import requests

url = "https://disfold.com/world/companies/?page=1"
rezultat = requests.get(url).text
doc = BeautifulSoup(rezultat, "html.parser")

