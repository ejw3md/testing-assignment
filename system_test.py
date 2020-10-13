import pytest
import System

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
        print(password)
        if passed_test:
            assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem