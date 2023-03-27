import requests
from bs4 import BeautifulSoup

# url = "https://www.zaubacorp.com/company/IDEAL-DEALCOMM-PRIVATE-LIMITED/U51909WB2010PTC141463"
url = "https://www.zaubacorp.com/company/LINKPOINT-VINTRADE-PRIVATE-LIMITED/U51909WB2010PTC155808"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


all_details = soup.find_all("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12"})
# print(len(all_details))
# for i in all_details:
#     print(i)
#     print("-------------------------------------------------------------------------")


company_details = soup.find("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12"}).find_all('p')
# for i in company_details:
#     print(i.text)

# print company name
# print("Company name: ", company_details[3].text)
# print("CIN: ", company_details[1].text)
# print("Company status: ", company_details[5].text)
# print("RoC: ", company_details[7].text)



Share_Capital_Number_of_Employees = (all_details[3].find_all('p'))
# print(Share_Capital_Number_of_Employees)
# print("Authorized capital: ", Share_Capital_Number_of_Employees[1].text)

email_id = soup.find("div", {"class": "col-12"}).find_all('p')
# print("Email id:", (email_id[0].text)[11: ].strip())


# director_details = soup.find_all("tr", {"id": ["package1", "package2"]})
director1_details = soup.find("tr", {"id": "package1"}).find_all('p')
director2_details = soup.find("tr", {"id": "package2"}).find_all('p')
# for i in director1_details:
#     print(i.text)
# print("Director 1:", director1_details[1].text)
# print("Director 2:", director2_details[1].text)


director1_companies = soup.find("div", {"id": "accordion1"}).find_all('p')
for i in range(0, len(director1_companies)-1, 3):
    print(director1_companies[i].text)


director1_companies = soup.find("div", {"id": "accordion1"})
# Extract all the links
links = director1_companies.find_all("a")
for link in links:
    URL = (link.get("href"))
    CIN = URL.split("/")[-1]
    print(CIN)


# director1_companies = soup.find("div", {"id": "accordion2"}).find_all('p')
# for i in range(0, len(director1_companies)-1, 3):
#     print(director1_companies[i].text)