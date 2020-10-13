import pytest
import System

#pass
def test_submit_assignment(grading_system):
    student = "akend3"
    password = "123454321"
    course = "databases"
    assignment = "assignment1"
    submission = "Test submission"
    submission_date = "10/12/20"

    users = grading_system.users
    grading_system.login(student, password)
    user = grading_system.usr
    user.submit_assignment(course, assignment, submission, submission_date)

    course = users[student]['courses'][course]

    assert(assignment in course)
    assert(submission == course[assignment]["submission"])
    assert(submission_date == course[assignment]["submission_date"])

#fail
def test_check_ontime(grading_system):
    student = "akend3"
    password = "123454321"

    grading_system.login(student, password)
    user = grading_system.usr

    assert(user.check_ontime("10/13/20", "10/13/20"))
    assert(not user.check_ontime("10/12/20", "10/10/20"))
    assert(not user.check_ontime("10/12/20", "10/13/19"))

#pass
def test_check_grades(grading_system):
    student = "hdjsr7"
    password = "pass1234"
    course = "cloud_computing"

    grading_system.login(student, password)
    user = grading_system.usr

    grades = user.check_grades(course)

    assert(grades == [["assignment1", 100], ["assignment2", 100]])

#fail
def test_view_assignments(grading_system):
    student = "hdjsr7"
    password = "pass1234"
    course = "cloud_computing"

    grading_system.login(student, password)
    user = grading_system.usr

    assignments = user.view_assignments(course)

    assert(assignments == [['assignment1', '2/2/20'], ['assignment2', '2/10/20']])


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem