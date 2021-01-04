#scrape2.py
#gets job information from Indeed

import requests
from bs4 import BeautifulSoup

pageNo = 0
URL = 'https://www.indeed.com/jobs?q=Software+Developer&l=San+Francisco,+CA&radius=50&start='

s = requests.session()

while(pageNo < 1000):
    page = requests.get(URL+str(pageNo))
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='pageContent')

    jobs = results.find_all('div', class_='jobsearch-SerpJobCard')
    for job in jobs:
        title = job.find('h2', class_='title')
        company = job.find('span', class_='company')

        #visit the links of each posting
        url2 = title.find("a").get("href")
        page2 = requests.get('http://indeed.com' + url2)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        results2 = soup2.find(id='jobDescriptionText')
        if results2 == None:
            continue
        res = results2.text.strip()
        if "java" in res:
           print company.text.strip() + " --> " + title.text.strip()

    pageNo += 10
