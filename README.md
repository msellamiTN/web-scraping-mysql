# Web Scraping Project

This project is designed to scrape job offers from a specified website and store the data in a MySQL database. It consists of two main services:

- `crawler`: A Python application that scrapes the website and inserts the data into the database.
- `mysql_jobs`: A MySQL database where the scraped data is stored.

## Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your system. You can download them from the following links:

- Docker: [https://www.docker.com/get-started](https://www.docker.com/get-started)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Project Structure

```
project-directory/
├── app/
│   ├── Dockerfile
│   └── crawler.py
├── mysql/
│   ├── Dockerfile
│   ├── sql-scripts/
│   │   └── jobs.sql
│   └── my.cnf
├── docker-compose.yml
└── README.md
```

- `app/`: Contains the Dockerfile for building the crawler service and the Python script (`crawler.py`) for web scraping.
- `mysql/`: Contains the Dockerfile for the MySQL database, initialization SQL scripts, and MySQL configuration file (`my.cnf`).
- `docker-compose.yml`: Defines the services, networks, and volumes for running the project with Docker Compose.

## Setup and Running

1. **Build and Start Services**

   Navigate to the project directory and run the following command to build and start the services defined in `docker-compose.yml`:

   ```bash
   docker-compose up --build
   ```

   The `--build` flag ensures that Docker images for both services are built before starting. Docker Compose automatically pulls the required base images, builds the custom images, and starts the services based on the configurations.

2. **Verify Services**

   You can check the status of the running services by executing:

   ```bash
   docker-compose ps
   ```

   Ensure both `crawler` and `mysql_jobs` services are up and running.

3. **View Logs**

   To view the logs and verify the crawler service's output, use:

   ```bash
   docker-compose logs crawler
   ```

   This command shows the logs for the `crawler` service, including any errors or the successful data scraping and insertion messages.

## Stopping Services

To stop and remove the containers, networks, and volumes created by Docker Compose, run:

```bash
docker-compose down -v
```

The `-v` flag ensures that the created volumes, including the persistent database storage, are also removed.

## Customization

- You can customize the scraping logic by modifying `crawler.py` in the `app/` directory.
- Database initialization scripts can be added or modified in the `mysql/sql-scripts/` directory.

For detailed documentation on Docker and Docker Compose commands, visit the official Docker documentation.