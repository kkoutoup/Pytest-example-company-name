import pytest, re
from company import Employee, Manager, CompanyDatabaseError

# Re-usable instances
John = Manager("John", "Smith", 50000, 3)
Kristen = Manager("Kristen", "Stewart", 60000, 5, "Judy")

# Test Manager subclass

'''
Create re-usable cases for tests that follow
'''
def test_manager_employees():
  '''
  Test that employees are added upon instance creation
  '''
  pass

def test_manager_add_employee_that_already_exists():
  '''
  Should raise exception if employee has already been added
  '''
  pass

def test_manager_add_employee_wrong_type():
  '''
  Raise exception if name of employee passed is empty string or wrong type
  '''
  pass

def test_manager_add_employee():
  '''
  Testing method works
  '''
  pass

def test_manager_remove_employee_when_no_employees():
  '''
  Raise exception if employees list is empty
  '''
  pass

def test_manager_remove_employee_when_employee_not_there():
  '''
  Raise exception if employee hasn't been added
  '''
  pass

def test_manager_remove_employee():
  '''
  Testing method works
  '''
  pass

def test_manager_list_employees_when_list_is_empty():
  '''
  Raise exception if employees array is empty
  '''
  pass

def test_manager_fullname():
  '''
  Testing inherited fullname method works
  '''
  pass

def test_manager_email():
  '''
  Testing inherited email method works
  '''
  pass

def test_manager_email_regex():
  '''
  Testing inherited method against regex
  '''
  pass

def test_manager_apply_raise():
  '''
  Testing inherited apply_raise method works
  '''
  pass