from flask import Flask
import pandas as pd
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json
#process data
# i=0
# df = pd.read_csv('all_courses_gpa.csv')
# df_final = df[['Index','Subject', 'Number','Primary Instructor','YearTerm','Sched Type']]
# df_final = df_final.astype(str)
# course_list = df_final.values.tolist()
# # empty_s = set()
# set = set()
# courses = {}    
# for x in course_list:
#         if (x[0] not in set):
#             if((x[5]=="DIS"  or x[5]=="LCD" or x[5]=="ONL" or x[5]=="OLC")):
#                 courses[i] = {"year_term":x[4], "instructor": x[3], "subject":x[1], "number":x[2]}
#                 set.add(x[0])
#                 i+=1

# json_courses = json.dumps(courses)
# with open("courses.json", "w") as outfile:
    #outfile.write(json_object)

app = Flask(__name__)
# def create_app(test_config=None):
    # create and configure the app
    
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

# a simple page that says hello
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')
   




