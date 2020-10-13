import pytest
import System

def test_drop_student(grading_system): # professor does not teach course
    student = "yted91"
    course = "cloud_computing"

    users = grading_system.users
    grading_system.login("goggins", "augurrox")

    user = grading_system.usr
    user.drop_student(student, course)

    assert(course in users[student]["courses"].keys())

def test_view_assignments(grading_system): # student not in class
    student = "yted91"
    password = "imoutofpasswordnames"
    course = "cloud_computing"

    grading_system.login(student, password)
    user = grading_system.usr

    assignments = user.view_assignments(course)

    assert(assignments == None)


def test_add_student(grading_system): # professor does not teach class
    student = "akend3"
    course = "cloud_computing"

    users = grading_system.users
    grading_system.login("goggins", "augurrox")

    user = grading_system.usr
    user.add_student(student, course)

    assert(course in users[student]["courses"])

def test_create_assignment(grading_system): # staff is not in class
    assignment_name = "testing-assignment"
    assignment_date = "10/13/20"
    assignment_course = "cloud_computing"

    grading_system.login("goggins", "augurrox")
    staff = grading_system.usr

    staff.create_assignment(assignment_name, assignment_date, assignment_course)
    assignments = grading_system.courses[assignment_course]["assignments"]

    assert(assignment_name not in assignments.keys())

def test_check_grades(grading_system): # staff is not in class
    student = "akend3"
    course = "comp_sci"

    grading_system.login("goggins", "augurrox")
    staff = grading_system.usr

    grades = staff.check_grades(student, course)
    
    assert(grades == None)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem