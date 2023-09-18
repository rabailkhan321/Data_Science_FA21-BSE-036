# Date:18/09/2023
# CSC461 – Assignment1 – Web Scraping
#Name:Rabail Salman
# Registration : FA21-BSE-036
# brief description: I have created a web scraper to extract the ‘title’ and ‘rating’ for my
# favorite movies from the IMDB website and placed it in movie_urls list
#and iterated through the list to get title and rating
#for each movie.Then I have exported the data to an excel file favorite_movie.xlsx.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


movie_urls = [
    "https://www.imdb.com/title/tt1587310/",  
    "https://www.imdb.com/title/tt0169102/",  
    "https://www.imdb.com/title/tt0398286/",
    "https://www.imdb.com/title/tt2294629/",  
    "https://www.imdb.com/title/tt0120338/"   
]


titles = []
ratings = []


for movie_url in movie_urls:
    response = requests.get(movie_url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    
    title = soup.find("span", class_="sc-afe43def-1 fDTGTb")
    
    
    
    rating = soup.find("span", class_="sc-bde20123-1 iZlgcd")
    
   
    titles.append(title)
    ratings.append(rating)
    
   
    time.sleep(1)


data = pd.DataFrame({'Title': titles, 'Rating': ratings})


data.to_excel('favorite_movie.xlsx', index=False)

print("Data has been exported to 'favorite_movie.xlsx'")
