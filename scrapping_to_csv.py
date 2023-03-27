import requests
from bs4 import BeautifulSoup
import csv  

# url = "https://www.zaubacorp.com/company/IDEAL-DEALCOMM-PRIVATE-LIMITED/U51909WB2010PTC141463"
url = "https://www.zaubacorp.com/company/LINKPOINT-VINTRADE-PRIVATE-LIMITED/U51909WB2010PTC155808"
# url = "https://www.zaubacorp.com/company/ECSTATIC-MERCHANDISE-PRIVATE-LIMITED/U51909WB2010PTC155811" #no directors

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_details = soup.find_all("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12"})
company_details = soup.find("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12"}).find_all('p')
Share_Capital_Number_of_Employees = (all_details[3].find_all('p'))
email_id = soup.find("div", {"class": "col-12"}).find_all('p')
try:
    director1_details = soup.find("tr", {"id": "package1"}).find_all('p')
    director1_name = director1_details[1].text
except (AttributeError, TypeError):
    director1_name = "Not available"

try:
    director2_details = soup.find("tr", {"id": "package2"}).find_all('p')
    director2_name = director2_details[1].text
except (AttributeError, TypeError):
    director2_name = "Not available"


# Write extracted information to a CSV file
with open("company_details.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # writer.writerow(["Company Name", "CIN", "Company Status", "RoC", "Authorized Capital", "Email ID", "Director 1", "Director 2"])
    writer.writerow([company_details[3].text, company_details[1].text, company_details[5].text, company_details[7].text, Share_Capital_Number_of_Employees[1].text, (email_id[0].text)[11:].strip(), director1_name, director2_name])





# For first director
try:
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

    # Write extracted information to a CSV file
    with open("director_companies.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Director Name", "Company Name", "CIN"])
        for company_name, CIN in zip(company_names, CINs):
            writer.writerow([director1_name, company_name, CIN])
except (AttributeError, TypeError):
    pass




# For second director
try:
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

    with open("director_companies.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # writer.writerow(["Director Name", "Company Name", "CIN"])
        for company_name, CIN in zip(company_names2, CINs2):
            writer.writerow([director2_name, company_name, CIN])
except (AttributeError, TypeError):
    pass