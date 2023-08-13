import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Selenium with Chrome in headless mode
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Define job search parameters
job_title = "python developer"
location = "New York"

# Build the Indeed search URL
search_url = f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}&l={location.replace(' ', '+')}"

# Use Requests and Beautiful Soup to fetch job links from search results
response = requests.get(search_url)
soup = BeautifulSoup(response.content, "html.parser")

job_links = []
for link in soup.find_all("a", {"class": "jobtitle"}):
    job_links.append(link.get("href"))

# Loop through job links using Selenium and extract job details
for link in job_links:
    job_url = f"https://www.indeed.com{link}"
    driver.get(job_url)
    time.sleep(2)  # Give the page some time to load

    job_title = driver.find_element(By.CLASS_NAME, "jobsearch-JobInfoHeader-title").text
    company_name = driver.find_element(By.CLASS_NAME, "jobsearch-CompanyAvatar-companyLink").text
    job_description = driver.find_element(By.ID, "jobDescriptionText").text

    print("Job Title:", job_title)
    print("Company:", company_name)
    print("Job Description:", job_description)
    print("=" * 50)

# Clean up
driver.quit()
