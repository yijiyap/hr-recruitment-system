# gather job info from the demand survey microservice
# gather applicant info from the cv microservice
# rank the applicants 

import os
import requests
from flask import (
    Flask,
    request,
    jsonify
)
