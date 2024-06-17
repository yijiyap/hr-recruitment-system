To consolidate all the candidates' information before sending it to the `shortlist` microservice

The information that has to be consolidated before sending to the `shortlist` microservice:
1. CV
2. Job application
3. English test score

### The orchestration of the candidates flow (on the last step):
1. The `candidate` microservice initiates the process by sending a GET request to the `cv_parser` microservice requesting all CVS
2. When the `cv_parser` microservice receives the response, it calls the `sharepoint` wrapper to retrieve the list of CVs stored in SharePoint.
3. `sharepoint` wrapper then downloads the requested CVs.
4. `sharepoint` wrapper will send the CVs to the `cv_parser` microservice using the `upload_cv` POST endpoint.
5. `cv_parser` microservice parses the CVs and parses them into JSON format. 
6. `cv_parser` microservice will send the JSON data to the `candidate` microservice 
7. `candidate` microservice will consolidate the CV JSON data, the English test score, and the application form
8. `candidate` microservice will send the consolidated data to `shortlist` microservice.