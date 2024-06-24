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
    def __init__(self, name, department, email_address, internship_resources, preferred_education_level, preferred_course_of_study, preferred_number_of_interns, internship_preference, jd, ivl_skills, eng_proficiency, office_tools, programming_languages, data_analysis_tools, design_tools, others, additional_test):
        self.name = name
        self.department = department
        self.email_address = email_address

        self.internship_resources = internship_resources # domestic and international
        self.preferred_education_level = preferred_education_level # Bachelor's, Master's, Vocational
        self.preferred_course_of_study = preferred_course_of_study
        self.preferred_number_of_interns = preferred_number_of_interns

        self.internship_preference = internship_preference
        self.jd = jd # a dictionary of the "description of tasks" and "relevant work experience"

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
        score = 0

        ###### START OF CALCULATE SCORE PART 1 ######
        # Check if candidate is in preferred course of study
        if candidate.current_major in self.preferred_course_of_study:
            score += 1
        ###### END OF CALCULATE SCORE PART 1 ######

        ###### START OF CALCULATE SCORE PART 2 ######
        # Check if candidate's CV and expectations matches the words in the job description in the intern's resume
        jd_words = set(word_tokenize(self.jd.get("description of tasks").lower())) | set(word_tokenize(self.jd.get("relevant work experience").lower()))

        # Tokenize and clean words
        jd_words = {word for word in jd_words if word not in stopwords.words('english') and word not in string.punctuation}

        # Combine all candidate info into one text
        candidate_text = " ".join([
            candidate.profile or "",
            " ".join(candidate.work_experiences) or "",
            " ".join(candidate.projects) or "",
            " ".join(candidate.skills) or "",
            " ".join(candidate.custom) or "",
            " ".join(candidate.internship_expectations) or ""
        ]).lower()

        candidate_words = set(word_tokenize(candidate_text))
        candidate_words = {word for word in candidate_words if word not in stopwords.words('english') and word not in string.punctuation}

        # Calculate the number of words that match. Each match adds 0.5 to the score (can be adjusted)
        score += 0.5 * len(jd_words & candidate_words)
        ###### END OF CALCULATE SCORE PART 2 ######

        ###### START OF CALCULATE SCORE PART 3 ######
        # Check if candidate has the required skills
        skills_to_check = [
            self.office_tools,
            self.programming_languages,
            self.data_analysis_tools,
            self.design_tools,
            self.others
        ]
        # Check for "Good-to-have" and "Mandatory"
        for skill_to_check in skills_to_check:
            if skill_to_check and skill_to_check != "Not relevant":
                for skill in skill_to_check:
                    if skill in candidate.skills:
                        score += 1
        ###### END OF CALCULATE SCORE PART 3 ######

        ###### START OF CALCULATE SCORE PART 4 ######
        # Check if the "department of interest" is in line with that of the role.
        if self.department in candidate.department_of_interest:
            score += 1
        return score

class Candidate:
    # Candidate class, which contains the name, skills, and experience of the candidate
    def __init__(self, email, job_application_info, eng_test_score, cv_info):
        self.email = email

        self.job_application_info = job_application_info
        self.eng_test_score = eng_test_score
        self.cv_info = cv_info

        # info from job application
        self.name = job_application_info.get("name")
        self.nationality = job_application_info.get("nationality")

        self.values_test_score = job_application_info.get("values_test_score")
        self.education_level = job_application_info.get("education_level")
        self.current_university = job_application_info.get("current_university")
        self.current_university_country = job_application_info.get("current_university_country")
        self.current_major = job_application_info.get("current_major")
        self.graduation_date = job_application_info.get("graduation_date")

        self.internship_expectations = job_application_info.get("internship_expectations")
        self.internship_duration = job_application_info.get("internship_duration")
        self.tentative_internship_start_date = job_application_info.get("tentative_internship_start_date")
        self.tentative_internship_end_date = job_application_info.get("tentative_internship_end_date")
        self.department_of_interest = job_application_info.get("department_of_interest") # list of departments
        self.open_to_other_locations = job_application_info.get("open_to_other_locations")
        
        # info from CV
        self.profile = cv_info.get("profile")
        self.educations = cv_info.get("educations")
        self.work_experiences = cv_info.get("workExperiences")
        self.projects = cv_info.get("projects")
        self.skills = cv_info.get("skills")
        self.custom = cv_info.get("custom")
        
app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/shortlist", methods=["POST"])
def shortlist():
    # get demand survey info from the post request
    target_ds = DS_info(
        request.json["name"],
        request.json["department"],
        request.json["email_address"],
        request.json["internship_resources"],
        request.json["preferred_education_level"],
        request.json["preferred_course_of_study"],
        request.json["preferred_number_of_interns"],
        request.json["internship_preference"],
        request.json["jd"],
        request.json["ivl_skills"],
        request.json["eng_proficiency"],
        request.json["office_tools"],
        request.json["programming_languages"],
        request.json["data_analysis_tools"],
        request.json["design_tools"],
        request.json["others"],
        request.json["additional_test"]
    )

    # get all candidates info from the candidate microservice
    candidates_info = requests.get("http://localhost:9002/all").json()

    # calculate fitness score for each candidate, and rank them
    shortlisted_candidates = []

    for candidate_info in candidates_info:
        # create a candidate object
        candidate = Candidate(candidate_info["email"], candidate_info["job_application_info"], candidate_info["eng_test_score"], candidate_info["cv_info"])

        # CHECK FOR IMMEDIATE REJECTION CRITERIA
        # check if candidate is in internship resources
        if not is_candidate_in_internship_resources(target_ds, candidate): 
            continue

        # check if the candidate falls within the preferred education level
        if not is_education_level_preferred(target_ds, candidate):
            continue
            
        # check if duration of internship is within the preferred duration
        if not is_internship_duration_eligible(target_ds, candidate):
            continue
            
        # check if english proficiency is within the required level
        if not is_english_test_eligible(target_ds, candidate):
            continue
        
        # CALCULATE SCORE
        fitness_score = target_ds.calculate_fitness_score(candidate)
        shortlisted_candidates.append({'name': candidate.name, 'fitness_score': fitness_score})
    
    return jsonify(sorted(shortlisted_candidates, key=lambda x: x['fitness_score'], reverse=True))

def is_candidate_in_internship_resources(target_ds, candidate):
    # check if candidate is in internship resources
    # if the internship resources is "Domestic", then there are 2 scenarios where the candidate is accepted:
        # 1. The candidate is of Thai nationality
        # 2. The candidate studies in a university in Thailand
    if target_ds.internship_resources == "Domestic":
        if candidate.current_university_country != "Thailand" and candidate.nationality != "Thai":
            return False
    return True

def is_education_level_preferred(target_ds, candidate):
    # check if the candidate falls within the preferred education level
    if candidate.education_level not in target_ds.preferred_education_level:
        return False
    return True

def is_internship_duration_eligible(target_ds, candidate):
    # convert candidate's dates from string to datetime
    candidate_start_date = datetime.strptime(candidate.tentative_internship_start_date, "%Y-%m-%d")
    candidate_end_date = datetime.strptime(candidate.tentative_internship_end_date, "%Y-%m-%d")
    
    # define internship periods
    internship_periods = {
        "First half of the year (Jan - Jun)" : (datetime(2025, 1, 1), datetime(2025, 6, 30)),
        "Summer Break (May - Aug)" : (datetime(2025, 5, 1), datetime(2025, 8, 31)),
        "Second half of the year (Jul - Dec)" : (datetime(2025, 7, 1), datetime(2025, 12, 31))
    }

    # Check if applicant's dates fall within any of the internship periods
    for period, (period_start, period_end) in internship_periods.items():
        if start_date <= period_end or end_date >= period_start: # made it more lenient to allow for some overlap. For strictly, change to "and"
            return True
    return False

def is_english_test_eligible(target_ds, candidate):
    # check if the candidate's english proficiency is within the required level
    if target_ds.eng_proficiency["Reading"] == ["Good", "Excellent"] and candidate.eng_test_score < 80:
        return False
    return True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
