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
        for page in extract_text_pdf(file_path):
            text += " " + page
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

    :param nlp_text: object: `spacy.tokens.doc.Doc`
    :param noun_chunks: list: List of noun chunks extracted from the nlp text
    :return: list: List of skills extracted
    """
    tokens = [token.text for token in nlp_text if not token.is_stop]
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'skills.csv')) # a simple skills dataset
    skills = list(data.columns.values)
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

def extract_experience(text):
    """
    Helper function to extract experience from text

    :param resume_text: Plain resume text
    :return: list of experiences
    """
    wordnet_lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)

    # remove the stop words and lemmatize
    filtered_sentence = [w for w in word_tokens if not w in stop_words and 
    wordnet_lemmatizer.lemmatize(w) not in stop_words] 
    sent = nltk.pos_tag(filtered_sentence)

    # parse the sentence to get the experience
    grammar = "P : {<NNP>+}"
    cp = nltk.RegexpParser(grammar)
    cs = cp.parse(sent)

    # extract the experience
    phrases = []
    for vp in list(cs.subtrees(filter=lambda x: x.label() == 'P')):
        phrases.append(" ".join([i[0] for i in vp.leaves() if len(vp.leaves()) > 1]))

    # search the word 'experience' in the chunk and then print out the text after it
    experience = []
    for phrase in phrases:
        if 'experience' in phrase.lower():
            experience.append(phrase[phrase.lower().index('experience')+10:])
    return experience

def extract_education(nlp_text):
    """
    Helper function to extract education from nlp text

    :param nlp_text: object: `spacy.tokens.doc.Doc`
    :return: dict where key is education degree, values is school name
    """
    edu = {}
    education_degree = ["BACHELORS", "MASTERS", "DOCTORATE", "PHD"]
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
    return edu
        
# test out the functions
if __name__ == "__main__":
    # test extract_text
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.abspath(os.path.join(script_dir, '../../sample_cv/doc/cv2.docx'))
    print(extract_text_main(pdf_path, ".docx"))