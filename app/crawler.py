#!/usr/bin/python
# My First web Scraping with Python and BeautifulSoup
from bs4 import BeautifulSoup as bs
import pandas as pd
from urllib.request import Request, urlopen
from sqlalchemy import create_engine
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

url = "https://www.sfds.asso.fr/fr/n/506-consulter_les_offres_demploi/?jedu=MASTER&jcon=&jp=3"
page = urlopen(url)
html = bs(page, "html.parser")

allJobs = html.findAll('div', class_='job')
titre_offre = []
date_offre = []
resume_offre = []

for job in allJobs:
    for titles in job.findAll('td', {'class': 'jobLabel'}):
        titre_offre.append(titles.get_text())

    datepubs = job.findAll('td', {'class': 'jobPublished'})
    date_offre.append(datepubs[0].get_text())

    for resumes in job.findAll('td', {'class': 'jobResume'}):
        resume_offre.append(resumes.get_text())

dfJobs = pd.DataFrame({
    'TITRE_OFFRE': titre_offre,
    'DATE_PUB_OFFRE': date_offre,
    'RESUME_OFFRE': resume_offre
})

# Database connection details
user = 'crawler'
password = 'supersecret'
host = 'mysql_jobs'  # Using the container name as defined in docker-compose.yml
port = 3306
database = 'jobs_scraping'

# SQLAlchemy engine for MySQL connection
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}', echo=False)

try:
    dfJobs.to_sql('jobs', con=engine, if_exists='append', index=False, chunksize=1000)
    logging.info("Data inserted successfully into the database.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
