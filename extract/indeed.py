from requests import get 
from bs4 import BeautifulSoup

website = "https://www.linkedin.com/jobs/search/?currentJobId=3586717182&keywords="

key = str(input())
response = get(f"{website}{key}")


soup = BeautifulSoup(response.text, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
print(len(jobs))



for job in jobs:
    print(job)