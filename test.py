import requests
from bs4 import BeautifulSoup
import csv  

url = "https://www.zaubacorp.com/company/LINKPOINT-VINTRADE-PRIVATE-LIMITED/U51909WB2010PTC155808"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
director1_details = soup.find("tr", {"id": "package1"}).find_all('p')
director1_name = director1_details[1].text

director1_companies = soup.find("div", {"id": "accordion1"}).find_all('p')
company_names = []
for i in range(0, len(director1_companies)-1, 3):
    company_names.append(director1_companies[i].text)

director1_companies = soup.find("div", {"id": "accordion1"})
links = director1_companies.find_all("a")
CINs = []
for link in links:
    URL = (link.get("href"))
    CINs.append(URL.split("/")[-1])


# For second director
director2_details = soup.find("tr", {"id": "package2"}).find_all('p')
director2_name = director2_details[1].text

director2_companies = soup.find("div", {"id": "accordion2"}).find_all('p')
company_names2 = []
for i in range(0, len(director2_companies)-1, 3):
    company_names2.append(director2_companies[i].text)

director2_companies = soup.find("div", {"id": "accordion2"})
links = director2_companies.find_all("a")
CINs2 = []
for link in links:
    URL = (link.get("href"))
    CINs2.append(URL.split("/")[-1])


# Write extracted information to a CSV file
with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Director Name", "Company Name", "CIN"])
    for company_name, CIN in zip(company_names, CINs):
        writer.writerow([director1_name, company_name, CIN])


with open("test.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # writer.writerow(["Director Name", "Company Name", "CIN"])
    for company_name, CIN in zip(company_names2, CINs2):
        writer.writerow([director2_name, company_name, CIN])