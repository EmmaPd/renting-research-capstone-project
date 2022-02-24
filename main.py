import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

class DataEntryBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def entry_data(self, n):
        self.driver.get(FORM_LINK)
        time.sleep(2)
        address_driver = self.driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_driver.send_keys(addresses[n])
        time.sleep(2)


        price_driver = self.driver.find_element(By.XPATH,
                                           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_driver.send_keys(correct_prices[n])
        time.sleep(2)

        link_driver = self.driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_driver.send_keys(correct_links[n])
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()


FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSc1OgLLto77EZgfiJ52v6VOrhdmCR1ps0q9ejPRZCoEELwYGQ/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

chrome_driver = r"C:\Users\emanuela.pandele\Downloads\Development - Selenium Webdriver\chromedriver.exe"

headers = {
    "User-Agent": "Chrome/96.0.4664.110",
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"

}

response = requests.get(ZILLOW_LINK, headers=headers)
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")

parsed_addresses = soup.find_all(name="address")
addresses = [address.text.split(",")[0] for address in parsed_addresses]
print(addresses)

parsed_links = soup.find_all("a", class_="list-card-link")
links = [link.get("href") for link in parsed_links]
links = list(dict.fromkeys(links))
correct_links = []
for link in links:
    if link.startswith("http"):
        correct_links.append(link)
    else:
        link = f"https://www.zillow.com/{link}"
        correct_links.append(link)
print(correct_links)

parsed_prices = soup.find_all(class_="list-card-price")
prices = [price.text for price in parsed_prices]

correct_prices = []
for price in prices:
    if "+" in price:
        price = price.split()[0] + "/mo"
        correct_prices.append(price)
    else:
        correct_prices.append(price)

print(correct_prices)

entry_bot = DataEntryBot()

for n in range(len(addresses)):
    entry_bot.entry_data(n)


