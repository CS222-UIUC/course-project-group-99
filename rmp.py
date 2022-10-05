import ratemyprofessor


def get_prof_credentials(professor_name, uni):
    professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name(uni), professor_name)
    professor_credentials = {}
    if professor is None:
        return professor_credentials
        ##if the professor is None, alternatively, we could try looking up their name in a database of universities, get the
        #corresponding uni name and run rmp function on the given uni name
    else:
        return {"Uni": professor.school.name, "Name": professor.name, "Dept": professor.department, "Difficulty":professor.difficulty,
                "Rating":professor.rating, "Num_Rating": professor.num_ratings, "Take_Again": professor.would_take_again
               }

creds = get_prof_credentials("Hongye Liu", "University of Illinois at Urbana-Champaign")
print(creds["Name"])