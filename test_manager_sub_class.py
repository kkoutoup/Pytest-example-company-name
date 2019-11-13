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