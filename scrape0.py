#scrape.py
#gets job information from Monster jobs

import requests
from bs4 import BeautifulSoup

pageNo = 10
URL = 'https://www.monster.com/jobs/search/Full-Time_8?q=Software-Developer&pg=10&stpage=1&where=San-Francisco__2c-CA&rad=20&tm=30&page='
page = requests.get(URL+str(pageNo))

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
count = 0

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    time_posted = job_elem.find('div', class_='meta flex-col')
    count += 1

    if None in (title_elem, company_elem, location_elem, time_posted):
		continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print("Posted " + time_posted.text.split()[0] + " days ago")
    print(" ")

print count
