from requests import get 
from bs4 import BeautifulSoup

def extwwrjobs (key):
    website = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    response = get(f"{website}{key}")
    if response.status_code != 200:
        print("Website not responding")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs =soup.find_all('section',class_="jobs")
        for job in jobs:
            job_posts = job.find_all('li')
            job_posts.pop(-1) #removing the find more button
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, time, region = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_='title')
                job_data = {
                    'company':company.string.replace(",", " "),
                    'link':f"https://weworkremotely.com/{link}",
                    'location':region.string.replace(",", ""),
                    'position':title.string.replace(",", "/"),
                }
                results.append(job_data)
        return results 

