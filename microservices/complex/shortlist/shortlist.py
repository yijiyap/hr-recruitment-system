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
        self.title = title
        self.description = description

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
    def __init__(self, name, skills, experience):
        self.email = email

        self.job_application_info = job_application_info
        self.eng_test_score = eng_test_score
        self.cv_info = cv_info

        # info from job application
        self.values_test_score = job_application_info.get(values_test_score)
        self.education_level = job_application_info.get(education_level)
        self.current_university = job_application_info.get(current_university)
        self.current_major = job_application_info.get(current_major)
        self.graduation_date = job_application_info.get(graduation_date)

        self.internship_duration = job_application_info.get(internship_duration)
        self.tentative_internship_start_date = job_application_info.get(tentative_internship_start_date)
        self.tentative_internship_end_date = job_application_info.get(tentative_internship_end_date)
        self.department_of_interest = job_application_info.get(department_of_interest)
        self.open_to_other_locations = job_application_info.get(open_to_other_locations)
        
        # info from CV
        self.skills = cv_info.get(skills)




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
        candidate = Candidate(candidate_info["name"], candidate_info["skills"], candidate_info["experience"])
        fitness_score = target_ds.calculate_fitness_score(candidate)
        shortlisted_candidates.append({'name': candidate.name, 'fitness_score': fitness_score})
    
    return jsonify(sorted(shortlisted_candidates, key=lambda x: x['fitness_score'], reverse=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
