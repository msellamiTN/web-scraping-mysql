# This file defines the Docker container that will contain the Crawler app.
# From the source image #python
FROM python:3.8-slim 
# Identify maintainer
LABEL maintainer = "mokhtar.sellami@gmail.com"
# Set the default working directory
WORKDIR /app/
COPY crawler.py requirements.txt /app/
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","./crawler.py"]
# When the container starts, run this
# ENTRYPOINT python ./crawler.py

