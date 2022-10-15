from flask import Flask, request, render_template
import pandas as pd
import xmltodict
import requests



app = Flask(__name__)
 
@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    global text
    text = request.form['text']
    return get_course_data(text)
 

def getCourse(year, semester, subject, num):
    r = requests.get(f'http://courses.illinois.edu/cisapp/explorer/catalog/{year}/{semester}/{subject}/{num}.xml')
    dict_data = xmltodict.parse(r.text) #parses xml file into dictionary
    #print(dict_data)
    label, desc, credit, attributes = (dict_data['ns2:course']['label'], dict_data['ns2:course']['description'], dict_data['ns2:course']['creditHours'], dict_data['ns2:course']['sectionDegreeAttributes'])
    return(f'{label}\n{desc}\n{credit}\n{attributes}\n')

def get_course_data(course_name):
    text_arr = [text.rstrip() for text in course_name.split(',')]

    return getCourse(2022, 'fall', text_arr[0],text_arr[1])
    #assumption is that the data passed is correct / cleaned up





# if __name__ == '__main__':
#     app.debug = True
#     app.run()