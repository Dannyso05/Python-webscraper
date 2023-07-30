from requests import get 
from bs4 import BeautifulSoup
sdsd
websites = (
    "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=",
    "https://www.linkedin.com/jobs/search/?currentJobId=3586717182&keywords=",
    "https://ca.indeed.com/jobs?q="
)

website = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

key = str(input())
response = get(f"{website}{key}")

if response.status_code != 200:
    print("Can't request website")
else:
    result = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs =soup.find_all('section',class_="jobs")
    for job in jobs:
        job_posts = job.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            company, time, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
        
            job_data = {
                "company": company.string,
                "time":time.string,
                "region":region.string,
                "title":title.string
            }

            result.append(job_data)
        print(job_data)
