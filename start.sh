#!/bin/bash
python3 ./crawler.py
echo "Press [CTRL+C] to stop ..."
while true
do
  sleep(200)
  echo "Job is done"

done 
 
docker run --name mysql -e MYSQL_ROOT_PASSWORD=supersecret   -e MYSQL_DATABASE=jobs_scraping   -v database:/var/lib/mysql -v ~/mysql/sql-scripts:/docker-entrypoint-initdb.d/  -p 3306:3306 -d mysql