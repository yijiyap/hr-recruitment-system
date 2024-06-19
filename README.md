# HR-recruitment-system
A web application to help recruiters analyse job applications and CVs, and shortlisting candidates that best match the job role.

## Project Overview:
This application is designed to streamline the recruitment process by providing tools to automatically pull data from SharePoint, parse CVs, conduct English tests, and match candidates to job descriptions based on keyword filtering.

## Architecture:
![alt text](architecture.png)

Given the current constraints, SharePoint is used as the main storage point.
The data is automatically pulled from SharePoint, so I pray it does not break 

## List of microservices
### Complex microservices
1. **Shortlist (9001)** - Python, Flask
2. **Candidates (9002)** - Python, Quart

### Simple microservices
1. **SharePoint Wrapper (5001)** - Python, Flask
2. **CV Parser (5002)** - Typescript, NextJS
3. **Demand Survey (5003)** - Python, Flask
4. **English test (5004)** - Python, Flask

## Frontend
Nuxt - v3.12

## Installing the HR-recruitment-system
Generally, you should install the HR-recruitment-system by building and running the Dockerfile, which contains all the dependencies you need. 
1. **Launch Docker Desktop**

2. **Clone the repository**
clone the repository by running the following command in your terminal:
```bash
git clone https://github.com/yijiyap/hr-recruitment-system.git
cd hr-recruitment-system
```

3. **Build the Dockerfile**
```bash
docker compose up --build -d
```

4. **Access the application**
The application should be running on `http://localhost:3000`

5. **Stop the application**
```bash
docker compose down
```

## Disclaimer
Because we have no access to any AI models (privacy and time limitations), we are limited to keyword-based filtering.

