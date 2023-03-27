import requests
from bs4 import BeautifulSoup

url = "https://leetcode.com/indrajit10/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())

profile_name = soup.find("div", {"class": "text-label-1 dark:text-dark-label-1 break-all text-base font-semibold"})
profile_name_text = profile_name.text
print("Name: ", profile_name_text)


rank = soup.find("span", {"class": "ttext-label-1 dark:text-dark-label-1 font-medium"})
rank_text = rank.text
print("Rank: ", rank.text)

region = soup.find("div", {"class": "flex items-start space-x-[9px]"})
region_text = region.text
print("Region: ", region.text)


elements = soup.find_all("div", {"class": "text-label-1 dark:text-dark-label-1 font-medium leading-[22px]"})

Contest_attended = elements[-1]
print("Contest attended: ", Contest_attended.text)

total_problem_solved = soup.find("div", {"class": "text-[24px] font-medium text-label-1 dark:text-dark-label-1"})
print("Total problem solved: ", total_problem_solved.text)

problems_difficulty = soup.find_all("div", {"class" : "w-[53px] text-label-3 dark:text-dark-label-3"})
problems_solved = soup.find_all("span", {"class" : "mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1"})
outOf = soup.find_all("span", {"class" : "text-xs font-medium text-label-4 dark:text-dark-label-4"})
beats = soup.find_all("span", {"class" : "font-medium text-label-2 dark:text-dark-label-2"})

for i in range(0, len(problems_difficulty)):
    print("Solved {} outof {} problems in {} category, Beats {}".format(problems_solved[i].text, outOf[i].text[1:], problems_difficulty[i].text, beats[i].text))


badges_count = soup.find("div", {"class" : "text-label-1 dark:text-dark-label-1 mt-1.5 text-2xl leading-[18px]"})
print("Badges count: ", badges_count.text)

submissions_in_last_year = soup.find("span", {"class" : "mr-[5px] text-base font-medium lc-md:text-xl"})
print("Submissions in last year: ", submissions_in_last_year.text)

total_active_days, max_streak = beats[3].text, beats[4].text
print("Total active days: {}, Max streak: {}".format(total_active_days, max_streak))


last_submission = soup.find_all("span", {'class': "text-label-1 dark:text-dark-label-1 font-medium line-clamp-1"})
hours_ago = soup.find_all("span", {"class", "text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline"})

print("Last 6 submissions: ")
for i in range(6):
    print("\tSolved", last_submission[i].text, hours_ago[i].text)

top_three_languages_used = soup.find_all("span", {"class" : "inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3"})

try:
    print("Top 3 languages used: ")
    for i in range(3):
        print("\t", top_three_languages_used[i].text)
except:
    # print("\tMost language used:", top_three_languages_used[0].text)
    pass
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold green")
table.add_column("Attributes")
table.add_column("Value")

table.add_row("Name", profile_name_text)
table.add_row("Rank", rank_text)
table.add_row("Region", region_text)
table.add_row("Contest attended", Contest_attended.text)
table.add_row("Total problem solved", total_problem_solved.text)
table.add_row("Badges count", badges_count.text)
table.add_row("Submissions in last year", submissions_in_last_year.text)
table.add_row("Total active days", total_active_days)
table.add_row("Max streak", max_streak)

console.print(table)
