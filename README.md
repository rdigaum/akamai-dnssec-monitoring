Getting Started
---------------
# akamai-dnssec-monitoring
# Monitoring the Expiration data of the DNSSEC

### Introduction

### Running it locally


Make sure you have Python installed on your system. The script was developed using Python 3, so it is recommended to have version 3.x installed. You can check the Python version by typing the following command in the terminal

- `$ python --version`

Install the required dependencies. The script uses the dnspython and python-dateutil libraries. To install the dependencies, run the following command in the terminal:

- `$ pip install requirements.txt`

Run the Python script by typing the following command:

- `$ python dnssec_monitoring.py`
- `output: akamai.com     will expire in 2 days, 18:09:27.280616`

### Running using Docker

Make sure you have Docker installed on your system. You can check the Docker is installed by typing the following command in the terminal:

- `$ docker --version`

Make a copy of the project using git clone

- `$ git clone https://github.com/rdigaum/akamai-dnssec-monitoring.git`

Build the image using the Dockerfile

- `$ docker build -t dnssec-monitoring .`

Run the container image by typing the following command:

- `$ docker run -d --name dnssec-monitoring-container dnssec-monitoring`

