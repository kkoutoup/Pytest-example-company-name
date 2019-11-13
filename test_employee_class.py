import re, pytest
from company import Employee, CompanyDatabaseError

# Re-usable instances
Kostas = Employee("Kostas", "Koutoupis", 30000, 3)
Sue = Employee("Sue", "Weatherspoon", 20000, 2)

# Test Employee class
def test_employee_first_and_last_name_type():
  '''
  Test first and last name attributes are of type string
  '''
  result = Kostas.first
  assert type(result) is str

  result = Kostas.last
  assert type(result) is str

  result = Sue.first
  assert type(result) is str

  result = Sue.last
  assert type(result) is str

def test_employee_years_in_company_type():
  '''
  Test years_in_company attribute is of type int
  '''
  result = Kostas.years_in_company
  assert type(result) != float
  assert type(result) != str
  assert type(result) is int

  result = Sue.years_in_company
  assert type(result) != float
  assert type(result) != str
  assert type(result) is int


def test_employee_salary_type():
  '''
  Test pay attribute is int
  '''
  result = Kostas.pay
  assert type(result) is int

def test_employee_fullname():
  '''
  Test fullname method is working
  '''
  result = Kostas.fullname
  assert result == "Kostas Koutoupis"

  result = Sue.fullname
  assert result == "Sue Weatherspoon"

def test_employee_email():
  '''
  Test employee method is working
  '''
  result = Kostas.email
  assert result == "KoutoupisK@company.uk"

  result = Sue.email
  assert result == "WeatherspoonS@company.uk"

def test_employee_email_regex():
  '''
  Test email against regex
  '''
  result = Kostas.email
  assert re.match(r"[\w]+[\w]@company\.uk", result)

  result = Sue.email
  assert re.match(r"[\w]+[\w]@company\.uk", result)

def test_employee_apply_raise():
  '''
  Test apply raise method is working
  '''
  result = Kostas.apply_raise()
  assert result == 45000

  result = Sue.apply_raise()
  assert result == 30000

def test_employee_can_be_promoted():
  '''
  Test method works
  '''
  result = Kostas.can_be_promoted()
  assert result == True

  result = Sue.can_be_promoted()
  assert result == False
