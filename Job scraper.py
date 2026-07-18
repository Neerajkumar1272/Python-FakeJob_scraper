import requests
from bs4 import BeautifulSoup
import sys
import csv

def main():


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }
    print("Connecting to the sever...")
    url = f"https://realpython.github.io/fake-jobs/"

    try:    
        response = requests.get(url, timeout=10, headers=headers).text
        print(f"Connected to server successfully")
    except:
        print(f"[ERROR] Server is not responding")

    soup = BeautifulSoup(response, 'lxml')
    job_lst, com_lst, location_lst, date_lst, apply_lst= scraping(soup)
    csv_data(job_lst, com_lst, location_lst, date_lst, apply_lst)

def scraping(soup):
    '''extracting all jobs from website '''
    job_card = soup.find_all(class_='column is-half')   
    job_lst= []                                         #creating new list(empty)
    com_lst = []
    location_lst = []
    date_lst = []
    apply_lst  = []
    
    print("Scraping start...")
    '''using for loop to iterate over job_card'''
    for job in job_card:
        job_title = job.find('h2', class_="title is-5").text.strip()
        com_name = job.find('h3', class_='subtitle is-6 company').text.strip()
        location = job.find(class_='location').text.strip()
        date_posted = job.find('p', class_='is-small has-text-grey').text.strip()
        apply_link = job.find('a',string='Apply').get('href')
    
        #appending elements in list
        job_lst.append(job_title)
        com_lst.append(com_name)
        location_lst.append(location)
        date_lst.append(date_posted)
        apply_lst.append(apply_link)

    print(f"Scrapping completed...")
    return job_lst, com_lst, location_lst, date_lst, apply_lst
      
def csv_data(job_lst, com_lst, location_lst, date_lst, apply_lst):
    
    print("Saving Data in CSV...")

    '''using csv to store scrapped data'''
    with open("job.7_18_2026.csv", "w", newline="", encoding='utf-8')  as file:
        writer = csv.writer(file)       #creating a writer object
        writer.writerow(["Job Title","Company Name", "Location", "Date Posted", "Apply link"])
        for job, com_name, location, date_posted, apply_link  in zip(job_lst, com_lst, location_lst, date_lst, apply_lst):
            writer.writerow([job, com_name, location, date_posted, apply_link])

    print("Completed Successfully")
if __name__ == "__main__":
    main()
