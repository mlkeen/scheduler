



class Employee(object):
  def __init__(self,  employee_ID, first_name, middle_name='', last_name=''):
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.employee_ID = employee_ID    
  def __str__(self):
    to_print='Employee ID: {id}\n{last}, {first}\n'.format(id=self.employee_ID, last=self.last_name, first=self.first_name)
    return to_print
  def __repr__(self):
    to_print='Employee ID: {id}\n{last}, {first}\n'.format(id=self.employee_ID, last=self.last_name, first=self.first_name)
    return to_print
 
 
    
def create_employee():
  print "Enter employee data\n"
  employee_first=raw_input("Employee First Name:")
  employee_middle=raw_input("Employee Middle Name:")
  employee_last=raw_input("Employee Last Name:")
  employee_payrate=raw_input("Hourly Payrate(e if exempt):")
  employee_hours_approved=raw_input("Hours approved per week:")
  employee_ID=raw_input("ID number:")
  print "{name} is approved for {hours} hours per week at ${payrate} per hour".format(name=employee_first, hours=employee_hours_approved, payrate=employee_payrate) 
  return Employee(employee_ID, employee_first, employee_middle, employee_last)
  
def save_employees(employees)
  filename=raw_input("filename:")
  #need to save data
  

employees=[]
quit_check='r'

while quit_check.lower() != 'q':
  quit_check=raw_input("q to quit, a to add employee, p to print, s to save:")
  if quit_check.lower() == 'a':
    employees.append(create_employee())
  if quit_check.lower() == 'p':
    print employees
  if quit_check.lower() == 's':
    save_employees(employees)

