# Shortlist microservice
This is a complex microservice as it calls on the CV microservice and DS (demand survey) microservice to shortlist the right candidate.

## Immediate rejection criteria
1. Not in internship resources
2. Not target Education level
3. Not in duration of internship
4. If "Good" is required for English proficiency, then must minimally pass the English test

## Bonus items
1. In preferred course of study
2. Words in job description and experience required match the words in the intern's resume
3. If the skills in the DS are tagged as "Good-to-have and above", then having the word in your resume will be an extra point 
4. If the "department of interest" is in line with the student's choice

## Algorithms considered
1. Keyword matching - the more matches there are between the candidate and the DS information, the higher the ranking
2. Cosine similarity - paper taken from [here](https://www.researchgate.net/publication/366706213_Evaluating_Automatic_CV_Shortlisting_Tool_For_Job_Recruitment_Based_On_Machine_Learning_Techniques)
3. TF-IDF similarity - reference to this project [here](https://github.com/harsha-chirumamilla/resume-screening)

