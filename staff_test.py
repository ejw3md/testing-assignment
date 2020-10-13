import pytest
import System

#fail
def test_change_grade(grading_system):
    student = "hdjsr7"
    course = "software_engineering"
    assignment = "assignment1"
    grade = 80

    users = grading_system.users
    grading_system.login("goggins", "augurrox")
    staff = grading_system.usr

    staff.change_grade(student, course, assignment, grade)

    assert(users[student]['courses'][course][assignment]['grade'] == 80)

#pass
def test_create_assignment(grading_system):
    assignment_name = "testing-assignment"
    assignment_date = "10/13/20"
    assignment_course = "software_engineering"

    grading_system.login("goggins", "augurrox")
    staff = grading_system.usr

    staff.create_assignment(assignment_name, assignment_date, assignment_course)
    assignments = grading_system.courses[assignment_course]["assignments"]

    assert(assignment_name in assignments)
    assert(assignment_date == assignments[assignment_name]['due_date'])

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
