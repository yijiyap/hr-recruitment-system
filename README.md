# HR-recruitment-system
A web application to help recruiters analyse job applications and CVs, and shortlisting candidates that best match the job role.

## Architecture:
![alt text](architecture.png)

Given the current constraints, SharePoint has to be used as the main storage point.
The data is automatically pulled from SharePoint, so I pray it does not break 

## List of microservies
### Complex
1. Shortlist (9001)
2. Candidates (9002)

### Simple
1. SharePoint Wrapper (5001)
2. CV Parser (5002)
3. Demand Survey (5003)

## Disclaimer
Because we have no access to any AI models (privacy and time limitations), we are limited to keyword-based filtering.
 