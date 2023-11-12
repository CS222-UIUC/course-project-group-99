
import requests
import re
import json
import base64
import os
from bs4 import BeautifulSoup
from transformers import pipeline

sentiment_pipeline = pipeline('sentiment-analysis')


    
f = open('course_codes.json')
course_codes = json.load(f)
def get_prof_info(id : str, professor_name: str, course_code : str):
    url = "https://www.ratemyprofessors.com" \
          "/search/teachers?query=%s&sid=%s" % (professor_name, base64.b64encode(("School-%s" % id)
                                                                                 .encode('ascii')).decode('ascii'))
    page = requests.get(url)
    search_page = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
    tid = re.findall(r'"legacyId":(\d+)', page.text)
    if len(tid) == 0:
        return {}
    result = {}
    for i in range(len(tid)):
        url2 = f"https://www.ratemyprofessors.com/professor?tid={tid[i]}"
        # print(url2)
        teacher_page = requests.get(url2)
        soup = BeautifulSoup(teacher_page.content, 'html.parser', from_encoding="utf-8")
        uni = soup.find_all("a",{"href":"/school?sid=1112"})
        if len(uni) == 0:
            continue
        

        overall = soup.find_all("div", {"class": "RatingValue__Numerator-qw8sqy-2 liyUjw"})[0].text
        if overall != "N/A":
          
            would_take = soup.find_all("div", {"class": "FeedbackItem__FeedbackNumber-uof32n-1 kkESWs"})[0].text 
            difficulty =  soup.find_all("div", {"class": "FeedbackItem__FeedbackNumber-uof32n-1 kkESWs"})[1].text
            num_ratings =  soup.find_all('a', href="#ratingsList")[0].text.split()[0]
            name = soup.find_all("div", {"class": "NameTitle__Name-dowf0z-0 cfjPUG"})[0].text
            dept =  soup.find_all("div", {"class": "NameTitle__Title-dowf0z-1 iLYGwn"})[0].text   
            # if (dept != course_codes[course_code]):
         
            d1 = re.findall(r"(?<=Professor in the ).*$", dept)
            d2 = re.findall(r".*?(?= department)", d1[0])[0]
            d2 = d2.rstrip()
            if(course_codes[course_code] != d2):
                continue
            raw_comment_list = soup.find_all("div",{"class": "Comments__StyledComments-dzzyvm-0 gRjWel"})
            comments = []
            for raw_comment in raw_comment_list:
                comments.append(raw_comment.text)

            num_comments = 0
            pos_comments = 0
            for comment in comments:
                if sentiment_pipeline(comment)[0]['label'] == 'POSITIVE':
                    pos_comments+=1
                num_comments+=1
            score = str(int(round(pos_comments/num_comments, 3) * 100)) + "%"

            result = {"overall": overall, "would_take":would_take, "difficulty": difficulty, "num_ratings":num_ratings, "dept": d2, "comments": score}
    f.close()
    return result
   


# a = get_prof_info("1112", "Graham Evans", "CS")
# print(a)