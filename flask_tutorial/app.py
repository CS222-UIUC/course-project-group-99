from flask import Flask
import urllib.parse
import pandas as pd
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
import json
import rmp_
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
global json_list
json_list = "kuch bhi nai"

# a simple page that says hello
@app.route('/', methods=["GET", "POST"])
def sast():
    return render_template('index.html')

@app.route('/final', methods=['POST'])
def final():
    global json_list
    json_list = request.get_json()
    return jsonify({'processed': 'true'})
    # return render_template('randimal.html', j=j)

@app.route('/randimal', methods=["GET"])
def randimal():
    course_info={} 
    for course in json_list: 

        code_and_name = course.split("-")
        course_code = code_and_name[0]
        name = code_and_name[1]
        first_and_last =  name.split(",")
        last_name = first_and_last[0]
        first_name = first_and_last[1].split(" ")[1]
        full_name = f"{first_name} {last_name}"
        rmp_data = {}
        rmp_data = rmp_.get_prof_info("1112", full_name)
        course_info[full_name + "-" + course_code] = rmp_data
        
    print(course_info)

        
    return render_template('randimal.html', j=json.dumps(json_list))

# @app.route("/final", methods = ["GET"])
# def final_get():
#     json_list = request.get_json()
#     return render_template('randimal.html', j = json_list)



