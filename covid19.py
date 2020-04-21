from bs4 import BeautifulSoup
import requests

class Veriler:
    def __init__(self):
        world_url = "https://www.worldometers.info/coronavirus/"
        country_url = "https://www.worldometers.info/coronavirus/country/turkey" # you can change it

        # WORLD DATA STRING
        req = requests.get(world_url)
        bs = BeautifulSoup(req.text, "html.parser")
        self.world_data = bs.find_all("div", class_ = "maincounter-number")

        # COUNTRY DATA STRING
        creq = requests.get(country_url)
        cbs = BeautifulSoup(creq.text, "html.parser")
        self.country_data = cbs.find_all("div", class_ = "maincounter-number")

    def totalCases(self):
        return self.world_data[0].text.strip()

    def totalDeaths(self):
        return self.world_data[1].text.strip()

    def totalRecovered(self):
        return self.world_data[2].text.strip()

    def Cases(self):
        return self.country_data[0].text.strip()

    def Deaths(self):
        return self.country_data[1].text.strip()

    def Recovered(self):
        return self.country_data[2].text.strip()
