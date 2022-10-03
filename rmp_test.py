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

