# Date:18/09/2023
# CSC461 – Assignment1 – Web Scraping
#Name:Rabail Salman
# Registration : FA21-BSE-036
#Q2(2)
# brief description: From the britannica website (https://www.britannica.com/on-this-day/March-24), I found out importabt events
#happened on my birthday



import requests
from bs4 import BeautifulSoup

britannica_url = "https://www.britannica.com/on-this-day/March-24"
response_britannica = requests.get(britannica_url)
soup = BeautifulSoup(response_britannica.content, 'lxml')
data=[]
req = soup.find('div', class_="featured-event-card card")
year = req.find('div' , class_="date-label")
year_text = year.text
title = req.find('div' , class_="title font-18 font-weight-bold mb-10")
title_text = title.text
description= req.find('div', class_= "description font-serif")
description_text= description.text
data.append(year_text + '\n' + title_text + '\n' + description_text + '\n')

file_path = "important_info.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Important events:\n")

    for i in data:
        file.write("{}".format(i))
        


print("Data has been written to important_info.txt")

