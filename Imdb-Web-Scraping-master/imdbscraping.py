from time import time, sleep
from warnings import warn
import pandas as pd
from bs4 import BeautifulSoup
from requests import get


headers = {"Accept-Language": "en-US, en;q=0.5"}

sYear = int(input("Enter the starting year: "))
eYear = int(input("Enter the End year: "))

n = []   #names
y = []   #years
imdb_ratings = []
metascores = []
votes = []
d = []   # Director
s = []   # Stars

pages = [str(i) for i in range(1, 5)]
y_url = [str(i) for i in range(sYear, eYear)]

requests = 0

for year_url in y_url:
    for page in pages:
        response = get('http://www.imdb.com/search/title?release_date=' + year_url + '&sort=num_votes,desc&page=' + page, headers = headers)
        sleep(15)
        requests += 1
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        if requests>72:
            warn('Number of requests was greater than expected.')
            break

        html_page = BeautifulSoup(response.text, 'html.parser')
        movie_containers = html_page.find_all('div', class_ = 'lister-item mode-advanced')
        
        for containers in movie_containers:
                name = containers.h3.a.text
                n.append(name)
                year = containers.h3.find('span', class_ ='lister-item-year').text
                y.append(year)

                imdb = float(containers.strong.text)
                imdb_ratings.append(imdb)

                #m_score = containers.find('span', class_ = 'metascore mixed').text
                #metascores.append(int(m_score))

                # Scrape the number of votes
                vote = containers.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))
                
                director = containers.find('p', class_='')
                d.append(director.a.text)


movie_ratings = pd.DataFrame({ 'movie': n,
                              'year': y,
                              'imdb_ratings': imdb_ratings,
                              'votes':votes,
                              'Director':d
    
    
    })

print(movie_ratings.info())
movie_ratings.head(10)

movie_ratings.to_csv('moviedata.csv', index=False)
