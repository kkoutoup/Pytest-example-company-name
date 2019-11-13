import pytest, re
from company import Employee, Manager, CompanyDatabaseError

# Re-usable instances
John = Manager("John", "Smith", 50000, 3)
Kristen = Manager("Kristen", "Stewart", 60000, 5, "Judy")

# Test Manager subclass
def test_manager_employee_on_instance_creation():
  '''
  Test that employees are added upon instance creation
  '''
  assert Kristen.employees == ["Judy"]

def test_manager_add_employee():
  '''
  Testing method works
  '''
  Kristen.add_employee("Jason")
  assert Kristen.employees == ["Judy", "Jason"]

def test_manager_add_employee_that_already_exists():
  '''
  Raise exception if employee has already been added
  '''
  with pytest.raises(CompanyDatabaseError) as context:
    Kristen.add_employee("Judy")
  
  # checking error message
  assert str(context.value) == f"Employee 'Judy' already in the company's database"

def test_manager_add_employee_wrong_type():
  '''
  Raise exception if name of employee passed is empty string or wrong type
  '''
  with pytest.raises(TypeError) as context:
    Kristen.add_employee(2)

  # checking error message
  assert str(context.value) == "Please make sure employee name is a valid string"

def test_manager_remove_employee_when_no_employees():
  '''
  Raise exception if employees list is empty
  '''
  with pytest.raises(CompanyDatabaseError) as context:
    John.remove_employee("James")
  
  # checking error message
  assert str(context.value) == "No employees have been added yet"

def test_manager_remove_employee_when_employee_not_there():
  '''
  Raise exception if employee hasn't been added
  '''
  with pytest.raises(CompanyDatabaseError) as context:
    Kristen.remove_employee("James")

  # checking error message
  assert str(context.value) == "Employee 'James' not found in the company's database"

def test_manager_remove_employee():
  '''
  Testing method works
  '''
  Kristen.add_employee("David")
  Kristen.remove_employee("David")
  assert Kristen.employees == ["Judy", "Jason"]

def test_manager_list_employees_when_list_is_empty():
  '''
  Raise exception if employees array is empty
  '''
  with pytest.raises(CompanyDatabaseError) as context:
    John.list_employees()

  # checking error message
  assert str(context.value) == "No employees have been added so far"

# Test inherited methods
def test_manager_fullname():
  '''
  Testing inherited fullname method works
  '''
  result = John.fullname
  assert result == "John Smith"

  result = Kristen.fullname
  assert result == "Kristen Stewart"

def test_manager_email():
  '''
  Testing inherited email method works
  '''
  result = John.email
  assert result == "SmithJ@company.uk"

  result = Kristen.email
  assert result == "StewartK@company.uk"
  
def test_manager_email_against_regex():
  '''
  Testing inherited method works agains regex
  '''
  result = John.email
  assert re.match(r"[\w]+[\w]@company\.uk", result)

  result = Kristen.email
  assert re.match(r"[\w]+[\w]@company\.uk", result)

def test_manager_apply_raise():
  '''
  Testing inherited apply_raise method works
  '''
  result = John.apply_raise()
  assert result == 90000

  result = Kristen.apply_raise()
  assert result == 108000
