from bs4 import BeautifulSoup
from extract import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    

    browser = webdriver.Chrome(options=options)
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find('nav',attrs={"aria-label": "pagination"})
    pages = pagination.find_all('div',recursive = False)
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
        final_url = (f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}")
        print("Requesting", final_url)
        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_lists = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_lists.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find('div', class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                'link' : f"https://kr.indeed.com/{link}",
                'company' : company.string,
                'location' : location.string,
                'positon' : title
                }
                results.append(job_data)
    return results


jobs = extract_indeed_jobs("python")
print((jobs))