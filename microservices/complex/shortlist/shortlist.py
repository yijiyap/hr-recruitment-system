# gather job info from the post request
# gather candidate info from the candidate microservice
# rank the candidates based on their fitness score 

import os
import requests
from flask import (
    Flask,
    request,
    jsonify
)
from flask_cors import CORS

class DS_info:
    # Demand Survey Info, which contains the title and description of the job
    def __init__(self, title, description):
        self.name = name
        self.department = department
        self.email_address = email_address

        self.title = title
        self.description = description
        self.internship_resources = internship_resources # domestic and international
        self.education = education
        self.preferred_course_of_study = preferred_course_of_study
        self.preferreed_number_of_interns = preferreed_number_of_interns

        self.internship_preference = internship_preference
        self.jd = jd # a dictionary of the description oftasks and relevant work experience

        self.ivl_skills = ivl_skills
        self.eng_proficiency = eng_proficiency # a dictionary of the required english proficiency level
        self.office_tools = office_tools # Microsoft Word, Excel, PowerPoint
        self.programming_languages = programming_languages # VBA, Python
        self.data_analysis_tools = data_analysis_tools # Tableau, Power BI, Data Management
        self.design_tools = design_tools # Photoshop, Illustrator, Premiere Pro, Canva, Figma
        self.others = others # any other skills required

        self.additional_test = additional_test # any additional test required

    def rank_candidates(self, candidates):
        # Rank candidates based on their fitness score
        ranked_candidates = []

        for candidate in candidates:
            fitness_score = calculate_fitness_score(job_description, candidate)
            ranked_applicants.append((candidate, fitness_score))

        ranked_candidates.sort(key=lambda x: x[1], reverse=True)

        return ranked_candidates
    
    def calculate_fitness_score(self, candidate):
        # Calculate the fitness score
        job_keywords = set(word_tokenize(self.description.lower()))

        # Calculate the number of matching skills
        matching_skills = len(job_keywords.intersection(candidate.skills))

        # Calculate the number of matching experiences
        matching_experiences = len(job_keywords.intersection(candidate.experience))

        # Calculate the fitness score
        score = (matching_skills + matching_experiences) / len(job_keywords)

        return score * 100 # convert to percentage

class Candidate:
    # Candidate class, which contains the name, skills, and experience of the candidate
    def __init__(self, email, job_application_info, eng_test_score, cv_info):
        self.email = email

        self.job_application_info = job_application_info
        self.eng_test_score = eng_test_score
        self.cv_info = cv_info

        # info from job application
        self.name = job_application_info.get(name)
        self.nationality = job_application_info.get(nationality)

        self.values_test_score = job_application_info.get(values_test_score)
        self.education_level = job_application_info.get(education_level)
        self.current_university = job_application_info.get(current_university)
        self.current_university_country = job_application_info.get(current_university_country)
        self.current_major = job_application_info.get(current_major)
        self.graduation_date = job_application_info.get(graduation_date)

        self.internship_duration = job_application_info.get(internship_duration)
        self.tentative_internship_start_date = job_application_info.get(tentative_internship_start_date)
        self.tentative_internship_end_date = job_application_info.get(tentative_internship_end_date)
        self.department_of_interest = job_application_info.get(department_of_interest)
        self.open_to_other_locations = job_application_info.get(open_to_other_locations)
        
        # info from CV
        self.profile = cv_info.get(profile)
        self.educations = cv_info.get(educations)
        self.work_experiences = cv_info.get(workExperiences)
        self.projects = cv_info.get(projects)
        self.skills = cv_info.get(skills)
        self.custom = cv_info.get(custom)
        
app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/shortlist", methods=["POST"])
def shortlist():
    # get demand survey info from the post request
    target_ds = DS_info(request.json["title"], request.json["description"])

    # get all candidates info from the candidate microservice
    candidates_info = requests.get("http://localhost:9002/all").json()

    # calculate fitness score for each candidate, and rank them
    shortlisted_candidates = []
    for candidate_info in candidates_info:
        # create a candidate object
        candidate = Candidate(candidate_info["email"], candidate_info["job_application_info"], candidate_info["eng_test_score"], candidate_info["cv_info"])

        # CHECK FOR IMMEIDATE REJECTION CRITERIA
        # check if candidate is in internship resources - to confirm with P Amy
        if target_ds.internship_resources == "Domestic" and candidate.current_university_country != "Thailand":
            continue

        # check if the candidate falls within the preferred education level
        if candidate.education_level not in target_ds.education_level:
            continue

        # calculate fitness score
        fitness_score = target_ds.calculate_fitness_score(candidate)
        shortlisted_candidates.append({'name': candidate.name, 'fitness_score': fitness_score})
    
    return jsonify(sorted(shortlisted_candidates, key=lambda x: x['fitness_score'], reverse=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
