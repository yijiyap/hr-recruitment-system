import os
import spacy
import re
import docx2txt
import pandas as pd
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
from pdfminer.high_level import extract_text
import io
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords 
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

def extract_text_pdf(pdf_path):
    """
    Helper function to extract plain text from .pdf files
    """
    text = extract_text(pdf_path)
    return text.lower()

def extract_text_docx(docx_path):
    """
    Helper function to extract plain text from .docx files
    """
    raw_text = docx2txt.process(docx_path)
    text = [line.replace('\t', ' ') for line in raw_text.split('\n') if line]
    return " ".join(text)

def extract_text_main(file_path, extension):
    """
    Wrapper function to detect the file extension and call text extraction functions accordingly
    """
    text = ''
    if extension == ".pdf":
        return extract_text_pdf(file_path)
    elif extension == ".docx" or extension == ".doc":
        text = extract_text_docx(file_path)
    return text

def extract_email(text):
    """
    Helper function to extract email addresses from the text
    """
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None
        
def extract_skills(nlp_text, noun_chunks):
    """
    Helper function to extract skills from the spacy nlp text
    If a word/phrase in the cv matches the skills given by the jd, then we consider that as the candidate has that skill

    :param nlp_text: object: `spacy.tokens.doc.Doc`
    :param noun_chunks: list: List of noun chunks extracted from the nlp text
    :return: list: List of skills extracted
    """
    tokens = [token.text for token in nlp_text if not token.is_stop]
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'dummy_jd_skills.csv')) # a list of skills that aligns with the JD
    skills = list(data.columns.values)    
    # normalise the skills
    skills = [skill.lower().strip() for skill in skills]

    skillset = []

    # check for one-grams
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)

    # check for bi-grams and tri-grams
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)

    return [i.capitalize() for i in set([i.lower() for i in skillset])]

# def extract_experience(text):
#     """
#     Helper function to extract experience from text

#     :param CV_text: Plain CV text
#     :return: list of experiences
#     """
#     wordnet_lemmatizer = WordNetLemmatizer()
#     stop_words = set(stopwords.words('english'))
#     word_tokens = nltk.word_tokenize(text)

#     # remove the stop words and lemmatize
#     filtered_sentence = [w for w in word_tokens if not w in stop_words and 
#     wordnet_lemmatizer.lemmatize(w) not in stop_words] 
#     sent = nltk.pos_tag(filtered_sentence)

#     # parse the sentence to get the experience
#     grammar = "P : {<NNP>+}"
#     cp = nltk.RegexpParser(grammar)
#     cs = cp.parse(sent)

#     # extract the experience
#     phrases = []
#     for vp in list(cs.subtrees(filter=lambda x: x.label() == 'P')):
#         phrases.append(" ".join([i[0] for i in vp.leaves() if len(vp.leaves()) > 1]))

#     # search the word 'experience' in the chunk and then print out the text after it
#     experience = []
#     for phrase in phrases:
#         if 'experience' in phrase.lower():
#             experience.append(phrase[phrase.lower().index('experience')+10:])
#     return experience

def extract_experience(text):
    # Use regular expressions to find all occurrences of date ranges
    date_ranges = re.findall(r'([A-Z][a-z]{2}\s\d{4})\s*-\s*([A-Z][a-z]{2}\s\d{4})', text)
    
    # Use regular expressions to find all occurrences of job titles and organizations
    experiences = re.findall(r'([A-Z][a-z]+ \d{4})\s*–\s*([A-Za-z\s]+)\s•\s([A-Za-z\s]+)\s•\s([A-Za-z\s]+)', text)
    
    # Format extracted data into a list of dictionaries
    extracted_experience = []
    for i in range(len(date_ranges)):
        start_date, end_date = date_ranges[i]
        position, organization, location, _ = experiences[i]
        experience_entry = {
            "start_date": start_date,
            "end_date": end_date,
            "position": position,
            "organization": organization,
            "location": location
        }
        extracted_experience.append(experience_entry)
    
    return extracted_experience


def extract_education(nlp_text):
    """
    Helper function to extract education from nlp text

    :param nlp_text: object: `spacy.tokens.doc.Doc`
    :return: dict where key is education degree, values is school name
    """
    edu = {}
    education_degree = ["BACHELORS", "BACHELOR'S", "MASTERS", "DOCTORATE", "PHD"]
    school_names = ["Thammasat", "Chulalongkorn", "Mahidol", "Kasetsart"]
    # Extract education degree
    doc = nlp_text
    for token in doc:
        if token.text.upper() in education_degree:
            degree_name = token.text.upper()
            # Check if the following tokens form a valid name
            for next_token in doc[token.i+1]:
                maybe_school_name = " ".join([token.text for token in doc[token.i+1:next_token.i+1]])
                if maybe_school_name.upper() in school_names:
                    edu[degree_name] = maybe_school_name
                    break
            # Check if the previous tokens form a valid name
            for prev_token in doc[token.i-1]:
                maybe_school_name = " ".join([token.text for token in doc[prev_token.i:token.i]])
                if maybe_school_name.upper() in school_names:
                    edu[degree_name] = maybe_school_name
                    break
    return edu
        
# test out the functions
if __name__ == "__main__":
    # test extract_text
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.abspath(os.path.join(script_dir, '../../sample_cv/pdf/cv5.pdf'))
    docx = extract_text_main(pdf_path, ".pdf")
    nlp = spacy.load('en_core_web_sm')
    nlp_text = nlp(docx)
    print("\ntext: \n", docx)
    print("\nemail: \n", extract_email(docx))
    print("\nskills: \n", extract_skills(nlp_text, nlp(docx).noun_chunks))
    print("\nexperience: \n", extract_experience(docx))
    print("\neducation: \n", extract_education(nlp_text))