import pytest
import System

### System.py tests
#fail
def test_login(grading_system):
    username = "newUser"
    password = "password"
    grading_system.login(username,password)
    users = grading_system.users
    
    assert(username in users.keys())

#pass
def test_check_password(grading_system):
    username = 'goggins'
    correct_password = 'augurrox'
    bad_passwords = ["", "\n", "AugOrRox", "augorrox2"]
    passed_test = grading_system.check_password(username, correct_password)
    if not passed_test:
        assert False
    
    for password in bad_passwords:
        passed_test = grading_system.check_password(username, password)
        if passed_test:
            assert False

### Staff.py Tests
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

### Professor.py Tests
#pass
def test_add_student(grading_system):
    student = "akend3"
    course = "software_engineering"

    users = grading_system.users
    grading_system.login("goggins", "augurrox")

    user = grading_system.usr
    user.add_student(student, course)

    assert(course not in users[student]["courses"])

#fail
def test_drop_student(grading_system):
    student = "yted91"
    course = "software_engineering"

    users = grading_system.users
    grading_system.login("goggins", "augurrox")

    user = grading_system.usr
    user.drop_student(student, course)

    assert(course not in users[student]["courses"])

### Student.py Tests
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


### Custom Tests
#fail
def test_drop_student_custom(grading_system): # professor does not teach course
    student = "yted91"
    course = "cloud_computing"

    users = grading_system.users
    grading_system.login("goggins", "augurrox")

    user = grading_system.usr
    user.drop_student(student, course)

    assert(course in users[student]["courses"].keys())

#fail
def test_view_assignments_custom(grading_system): # student not in class
    student = "yted91"
    password = "imoutofpasswordnames"
    course = "cloud_computing"

    grading_system.login(student, password)
    user = grading_system.usr

    assignments = user.view_assignments(course)

    assert(assignments == None)

#fail
def test_add_student_custom(grading_system): # professor does not teach class
    student = "akend3"
    course = "cloud_computing"

    users = grading_system.users
    grading_system.login("goggins", "augurrox")

    user = grading_system.usr
    user.add_student(student, course)

    assert(course in users[student]["courses"])

#fail
def test_create_assignment_custom(grading_system): # staff is not in class
    assignment_name = "testing-assignment"
    assignment_date = "10/13/20"
    assignment_course = "cloud_computing"

    grading_system.login("goggins", "augurrox")
    staff = grading_system.usr

    staff.create_assignment(assignment_name, assignment_date, assignment_course)
    assignments = grading_system.courses[assignment_course]["assignments"]

    assert(assignment_name not in assignments.keys())

#fail
def test_check_grades_custom(grading_system): # staff is not in class
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