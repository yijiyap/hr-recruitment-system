# Shortlist microservice
This is a complex microservice as it calls on the CV microservice and DS (demand survey) microservice to shortlist the right candidate.

## Algorithms considered
1. Keyword matching - the more matches there are between the candidate and the DS information, the higher the ranking
2. Cosine similarity - paper taken from [here](https://www.researchgate.net/publication/366706213_Evaluating_Automatic_CV_Shortlisting_Tool_For_Job_Recruitment_Based_On_Machine_Learning_Techniques)
3. TF-IDF similarity - reference to this project [here](https://github.com/harsha-chirumamilla/resume-screening)

