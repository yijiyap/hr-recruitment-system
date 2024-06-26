# Shortlist microservice
This microservice helps in selecting the best candidates for internships by evaluating their resumes against the job requirements from the demand survey and the CV microservice. A scoring system is used to grade candidates on their suitability for the role.

## How it works
### Immediate rejection criteria
Candidates are autumatically rejected if they do not meet the following criteria:
1. They are not listed in the preferred internship resources (eg if the hiring manager selects "Domestic" for the 6mth internship period but the applicant is an "International" student) 
2. They are not in the target Education Level (eg if the hiring manager specifically requires a "Masters" student only, but the applicant is a "Bachelors" student)
3. They are not available during the required internship period
4. They fail the "English" test when a "Good" or above English proficiency is required, 

## Point system
Candidates can earn points if they:
1. Are studying in a preferred course of study
2. Have keywords in their resumes that match the job description and required experience
3. Mention sills in their resumes that are marked as "Good-to-have" or higher in the job requirements. (Mandatory and Good-to-have skills are weighted differently) 
4. Have a department of interest that aligns with the role

## Algorithms considered
1. Keyword matching - the more matches there are between the candidate and the DS information, the higher the ranking
2. Cosine similarity - paper taken from [here](https://www.researchgate.net/publication/366706213_Evaluating_Automatic_CV_Shortlisting_Tool_For_Job_Recruitment_Based_On_Machine_Learning_Techniques) (YET TO BE IMPLEMENTED)
3. TF-IDF similarity - reference to this project [here](https://github.com/harsha-chirumamilla/resume-screening) (YET TO BE IMPLEMENTED)

## Fitness Score Calculation Deep Dive
The `calculate_fitness_score` function calculates a fitness score for a given candidate based on several criteria derived from the job description. It uses keyword matching to assess how closely the candidate's qualifications, experiences, and interests align wth those required for the position. Here is a breakdown of how the algorithm works:
### Part 1: Preferred course of study
- If the candidate's course of study matches the preferred course of study for the position, the score is incremented by 1. This ensures that the candidate has the necessary background knowledge to do well in the role.
### Part 2: Keyword matching between the JD and Candidate's profile
- It tokenizes (breaks down into individual words) the job description's task descriptions and relevant work experience sections, removing common stop words (like "the," "is," etc.) and punctuation to focus on meaningful keywords.
- Similarly, it tokenizes and cleans the candidate's profile, work experiences, projects, skills, custom fields, and internship expectations.
- Then, it calculates the intersection of these sets of keywords (words found in both the JD and the candidate's profile). For each matching keyword, it adds 0.5 to the score. This part measures how many of the job's essential terms the candidate has demonstrated knowledge or experience in.
### Part 3: Checking for required skills
- It iterates through a list of required skills for the job, including office tools, programming languages, data analysis tools, design tools, and other skills.
- For each category of skills, if the category is applicable (not marked as "Not relevant" in the job description), it checks if the candidate has mentioned any of the skills in that category in their profile.
    - If the skill is marked as "Good-to-have and above" in the job description, it adds 0.5 to the score for each matching skill.
    - If the skill is marked as "Mandatory" in the job description, it adds 1 to the score for each matching skill.
### Part 4: Departmental Interest Alignment
- Finally, it checks if the candidate's declared department of interest matches the department associated with the job. If there's a match, it adds 1 to the score. This part ensures that the candidate has expressed interest in working within the right academic or professinoal field.
### Part 5: Final Score Calculation
- The final score is the sum of the scores from the four parts above. This score is used to rank candidates based on how well they match the job description and requirements. The higher the score, the better the candidate's fit for the position.
- Because the score is based on the number of matching keywords, it may favour candidates with longer resumes or more verbose descriptions. Therefore, a normalization step is done to account for this bias. The score is divided by the total number of keywords in the job description to get a percentage score, which is then multiplied by 100 to get a score out of 100.

