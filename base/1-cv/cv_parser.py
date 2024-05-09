import os
import spacy
import pprint
from spacy.matcher import Matcher
from . import utils

class CvParser(object):
    def __init__(self, cv):
        nlp = spacy.load('en_core_web_sm') # Load the english model
        self.__matcher = Matcher(nlp.vocab) # Matcher object for efficient matching of tokens
        self.__details = {
            'email': None,
            'skills': None,
            'experience': None,
            'education': None,
        }
        self.__cv = cv
        self.__text_raw = utils.extract_text(self.__cv)
        self.__text = nlp(self.__text_raw)
        self.__noun_chunks = list(self.__text.noun_chunks)
        self.__get_basic_details()
        return
    
    def get_extracted_details(self):
        return self.__details
    
    def __get_basic_details(self):
        email = utils.extract_email(self.__text)
        skills = utils.extract_skills(self.__nlp, self.__noun_chunks)
        experience = utils.extract_experience(self.__text)
        education = utils.extract_education([sentence.string.strip() for sentence in self.__nlp.sentence])
        self.__details['email'] = email
        self.__details['skills'] = skills
        self.__details['experience'] = experience
        self.__details['education'] = education
        return
    
def cv_result_wrapper(cv):
    parser = CvParser(cv)
    return parser.get_extracted_details()

if __name__ == "__main__":
    cvs = []
    results = []
    for root,directories, filenames in os.walk('cvs'):
        for filename in filenames:
            file = os.path.join(root, filename)
            cvs.append(file)

    for cv in cvs:
        results.append(cv_result_wrapper(cv))

    pprint.pprint(results)