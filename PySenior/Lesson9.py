# import urllib.request
# import requests

# response = requests.get("https://httpbin.org/get")
# print(response.content)
# print(f"Datatype – {type(response.content)}")

# print(response.text)
# print(type(response.text))

# response = requests.get("https://coinmarketcap.com/")
# print(response.text)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
print(response.status_code)

soup = BeautifulSoup(response.text, features='html.parser')
soup_list = soup.find_all("div", {"class": "sc-9d064f2d-0"})

for element in soup_list:
    print(element.text)

print(soup_list[0].findNext('span').text)
