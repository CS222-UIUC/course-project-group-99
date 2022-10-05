import pytest
import rmp

def test_blank_input():
    credentials = rmp.get_prof_credentials("Daniel Berwik Evans", "University of Illinois at Urbana-Champaign")
    assert (credentials == {})

def test_correct_values():
	credentials = rmp.get_prof_credentials("Graham Evans", "University of Illinois at Urbana-Champaign")
	assert(credentials["Name"] == "Graham Evans")
	print(credentials)
	assert(int(credentials["Take_Again"]) == 42)

def bad_input_is_read():
    credentials = rmp.get_prof_credentials("Daniel Berwik Evans", "University of Illinois at Urbana-Champaign")
    assert(credentials == {})

def test_incorrect_input_is_not_recognized():
    credentials = rmp.get_prof_credentials("Daniel Berwik Evans", "University of Illinois at Urbana-Champaign")
    assert(credentials == {})

def test_bad_input_is_corrected():
    credentials = rmp.get_prof_credentials("DaniEl BeRwick Evans   ", "University of Illinois at Urbana-Champaign")
    assert(credentials["Name"] == "Daniel Berwick-Evans")
    assert(int(credentials["Rating"]) == 4)
   




