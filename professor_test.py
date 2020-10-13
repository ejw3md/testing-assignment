import pytest
import System

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


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
