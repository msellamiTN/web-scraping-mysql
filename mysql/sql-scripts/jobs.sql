Create Database IF NOT EXISTS jobs_scraping;
use jobs_scraping;
CREATE TABLE IF NOT EXISTS jobs_scraping.jobs (
TITRE_OFFRE varchar(100),
DATE_PUB_OFFRE  varchar(100),
RESUME_OFFRE TEXT 
);
