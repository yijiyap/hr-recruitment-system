import os
import spacy
from nltk.tokenize import word_tokenize

def calculate_fitness_score(job_description, applicant_info):
    # Calculate the fitness score
    job_keywords = set(word_tokenize(job_description.lower()))

    applicant_skills = applicant_info["skills"]
    applicant_experience = applicant_info["experience"]

    # Calculate the number of matching skills
    matching_skills = len(job_keywords.intersection(applicant_skills))

    # Calculate the number of matching experiences
    matching_experiences = len(job_keywords.intersection(applicant_experience))

    # Calculate the fitness score
    score = (matching_skills + matching_experiences) / len(job_keywords)

    return score * 100  # Convert to percentage

def rank_applicants(job_description, applicants):
    # Rank the applicants based on their fitness score
    ranked_applicants = []

    for applicant in applicants:
        fitness_score = calculate_fitness_score(job_description, applicant)
        ranked_applicants.append((applicant, fitness_score))

    ranked_applicants.sort(key=lambda x: x[1], reverse=True)

    return ranked_applicants
