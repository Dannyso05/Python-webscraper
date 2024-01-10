from bs4 import BeautifulSoup
import requests

def extrmtokjobs(term):
  website = f"https://remoteok.com/remote-{term}-jobs"
  response = requests.get(website, headers={"User-Agent": "dan"})
  results = []
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
        link = job.find("a", itemprop="url")
        company = job.find("h3", itemprop="name")
        position = job.find("h2", itemprop="title")
        location = job.find("div", class_="location")
        job_data = {
            'link': f"https://remoteok.com{link['href']}",
            'company': company.string.strip().replace(",", " "),
            'position': position.string.strip().replace(",", "/"),
            'location': location.string.strip().replace(",", "")
        }
        results.append(job_data)
  return results