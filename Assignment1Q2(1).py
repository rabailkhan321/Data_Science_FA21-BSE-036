# Date:18/09/2023
# CSC461 – Assignment1 – Web Scraping
#Name:Rabail Salman
# Registration : FA21-BSE-036
#Q2(1)
# brief description: From the ‘timeanddate’ website (https://www.timeanddate.com/on-this-day/march/24), I found out who you share birthdate with me(24 March).
#Then I have written the information that I have extracted in text file shared_birthday_info.txt

import requests
from bs4 import BeautifulSoup


timeanddate_url = "https://www.timeanddate.com/on-this-day/march/24"

data =[] 
response_timeanddate = requests.get(timeanddate_url)


root = BeautifulSoup(response_timeanddate.content, 'lxml')


req = root.find("div", class_="otd-life__block")


ul1 = req.find("ul", class_="list--big")

lit = ul1.find_all('li')



for a in lit:
    name = a.h3.text.strip()
    detail = a.p.text.strip()
    data.append(name + '\n' + detail +'\n\n')


file_path = "shared_birthday_info.txt"


with open(file_path, "w", encoding="utf-8") as file:
    file.write("Shared Birthday Information:\n")
    file.write("Names of People:\n")
    for i in data:
        file.write("{}".format(i))
        


print("Data has been written to 'shared_birthday_info.txt'")


