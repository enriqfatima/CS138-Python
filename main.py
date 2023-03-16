'''
DEVELOPER: Fatima Enriquez
COLLABORATOR(S): name(s) of anyone who helped you
'''
""" This program can be used to create an amortization schedule for a loan.
"""

##### FUNCTION DEFINITIONS #####
def introduction():
  '''introduction message of this particular program'''
  print("Hello, this program will take in information about your paricular loan, rate, and term variables to then create a schedule for payments.\n")
  rate = input("What is your monthly loan rate?: ")
  priniple = input("What is your principle?: ")
  return ''
  
  

def create_schedule (principle, month_interest_rate, term):
  '''This function calculates the monthly payment, interest payment each month, principle payment each month, and remaining balance after payment'''
  num_payments = 12 * term
  monthly_payment = principle * ((month_interest_rate*((1+month_interest_rate)**(num_payments)))/((1+month_interest_rate)**(num_payments)) - 1)
  
  
##### MAIN PROGRAM #####
print(introduction())

