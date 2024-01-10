from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_page_count(keyword):

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
   #options.add_argument("--headless")  # Run Chrome in headless mode (without GUI) 
    #error here
    

    browser = webdriver.Chrome(options=options)
    browser.get(f"https://ca.indeed.com/jobs?q={keyword}")
    time.sleep(12)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup)

    pagination = soup.find('nav', role_="navigation")
    pag = pagination.find('ul')
    pages = pag.find_all('li', recursive = False)
    count =len(pages)
    if count == 0:
        return 1
    else:
        return count -1
    

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("found", pages, "pages")
    results = []

    for page in range (pages):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options=options)
        final_url = (f"https://ca.indeed.com/jobs?q={keyword}&start={page*10}")
        print("Requesting", final_url)
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")

        job_lists = soup.find('div',id="mosaic-jobResults",class_="mosaic-zone")
        print(job_lists)
        j = job_lists.find('div')
        j2=j.find('ul')
        jobs = j2.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find('div', class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", attrs={"data-testid": "company-name"})
                location = job.find("div", attrs={"data-testid": "text-location"})
                job_data = {
                'link' : f"https://ca.indeed.com/{link}",
                'company' : company.string.replace(",", " "),
                'location' : location.string.replace(",", ""),
                'position' : title[16:].replace(",", "/"),
                }
                results.append(job_data)
    return results
