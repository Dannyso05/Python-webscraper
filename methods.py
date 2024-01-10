from extract.weworkremote import *
from extract.indeed import *
from extract.remoteok import *

def get_jobs(keyword):
    wwrjobs = extwwrjobs(keyword)
    #indjobs = extract_indeed_jobs(keyword)
    rmtokjobs = extrmtokjobs(keyword)
    jobs=wwrjobs+rmtokjobs
    return jobs

def csvfile(filename, jobs):
    file= open(f"{filename}.csv", "w", encoding="utf-8-sig") 
    file.write ("Position,Company,Location,URL\n")
    for job in jobs:
        file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")
    file.close()

