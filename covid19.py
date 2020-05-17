from bs4 import BeautifulSoup
import requests

world_url = "https://www.worldometers.info/coronavirus/"
country_url = "https://www.worldometers.info/coronavirus/country/turkey" # you can change it

# WORLD DATA STRING
req = requests.get(world_url)
bs = BeautifulSoup(req.text, "html.parser")
world_data = bs.find_all("div", class_ = "maincounter-number")

# COUNTRY DATA STRING
creq = requests.get(country_url)
cbs = BeautifulSoup(creq.text, "html.parser")
country_data = cbs.find_all("div", class_ = "maincounter-number")

def totalCases():
    return world_data[0].text.strip()
    
def totalDeaths():
    return world_data[1].text.strip()

def totalRecovered():
    return world_data[2].text.strip()
    
def Cases():
    return country_data[0].text.strip()

def Deaths():
    return country_data[1].text.strip()

def Recovered():
    return country_data[2].text.strip()
