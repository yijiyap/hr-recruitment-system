# Receives demand survey data from onedrive
# Sends demand survey data to the filtering microservice
from flask import (
    Flask,
    request,
    jsonify
)
import os
import requests
from flask_cors import CORS
import polars as pl

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/ds/all", methods=["GET"])
def all():
    """
    1. This endpoint will be called by the frontend to get all the demand survey data.
    2. DS microservice will call the SharePoint Wrapper microservice to get all the demand survey data.
    3. DS microservice will then return the DS info to the frontend.
    """
    # call the SharePoint Wrapper microservice to get the demand survey data
    # response = requests.get("http://localhost:5001/sharepoint/ds/all")

    # for now, we get the excel file of the results locally
    # only for testingg
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # go back 3 folders to get to the excel file
    for _ in range(4):
        cur_path = os.path.dirname(cur_path)
    dummy_survey = os.path.join(cur_path, "Internship Demand Survey Form for 2025(1-5).xlsx")

    df = pl.read_excel(dummy_survey)

    # change the headers to lowercase
    df.columns = [col.lower() for col in df.columns]

    # change to JSON format
    data = df.to_dicts() # to get row by row

    # group the supervisor details together
    grouped_data = []
    for row in data:
        # group sup details
        supervisor_details = {
            "supervisorEmail": row["email address"],
            "supervisorName": row["supervisor name (english)"],
            "department": row["department"],
        }

        # group internship details
        internship_details = {
            "preferredInternshipResource": row["preferred internship resource"].split(";"),
            "preferredEducationLevel": row["preferred education level"].split(";"),
            "roleId": row["id"],
            "roleName": row["department"].title() + " " + "Intern",
            "internshipPeriod": {
                "first half of the year (jan - jun)": row["first half of the year (jan - jun)"],
                "second half of the year (jul - dec)": row["second half of the year (jul - dec)"],
                "summer break (may - aug)": row["summer break (may - aug)"],
            },
            "internshipPreference": row["internship preference"].split(";"),
            "workingConditions": row["working conditions"].split(";"),
        }

        # group requirements
        responsibilities = {
            "description": row["Please provide a detailed description of the tasks and responsibilities you expect the intern to perform"],
            "experience": row["What specific experience should the ideal candidate have?"],
            "skills": row["Please choose the skills you would like your intern to possess. The options listed are derived from the Indorama Ventures competency library"].split(";"),
            "english_required": {
                "speaking": row["speaking"],
                "writing": row["writing"],
                "reading": row["reading"],
                "listening": row["listening"],
            },
            "office_tools": {
                "microsoft word": row["microsoft word"],
                "microsoft excel": row["microsoft excel"],
                "microsoft powerpoint": row["microsoft powerpoint"],
            },
        }
        mandatory_skills, good_to_have_skills = [], []
        all_skills = ["vba", "python", "tableau", "power bi", "data management", "adobe photoshop", "adobe illustrator", "adobe premiere pro", "canva", "figma"]
        
        for s in all_skills:
            if row[s] == "Mandatory":
                mandatory_skills.append(s.title())
            elif row[s] == "Good-to-have":
                good_to_have_skills.append(s.title())

        other_skills = row["others"]
        for skill_n_kind in other_skills.split(";"):
            if skill_n_kind.strip():
                skill, kind = skill_n_kind.split(":")
                skill = skill.strip()
                kind = kind.strip()
                if kind == "Mandatory":
                    mandatory_skills.append(skill)
                elif kind == "Good-to-have":
                    good_to_have_skills.append(skill)

        responsibilities["mandatorySkills"] = mandatory_skills
        responsibilities["goodToHaveSkills"] = good_to_have_skills

        extra_test = row.get("what type of assessment will it be", "")

        # compile the grouped data for each row
        row_data = {
            "supervisorDetails": supervisor_details,
            "internshipDetails": internship_details,
            "responsibilities": responsibilities,
            "extraTest": extra_test,
        }

        # append the row data to the list
        grouped_data.append(row_data)

    return jsonify(grouped_data)

@app.route("/ds/test", methods=["POST"])
def upload_excel():
    """
    To receive an excel file of the demand survey, 
    parse it, 
    and POST to the filtering microservice.
    """
    # TO RECEIVE FROM THE SHAREPOINT
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        # try: 
            # read the excel file
            df = pl.read_excel(file)
            
            # change the headers to lowercase
            df.columns = [col.lower() for col in df.columns]

            # prepare demand survey data to be sent
            data = df.to_dicts() # to get row by row
            return jsonify(data)
            # # send the data to the filtering microservice
            # response = requests.post("http://localhost:9001/upload", json=data)

            # # return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

    