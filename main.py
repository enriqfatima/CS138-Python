'''
DEVELOPER: Fatima Enriquez
COLLABORATOR(S): name(s) of anyone who helped you
'''
""" This program can be used to create an amortization schedule for a loan.
"""

##### FUNCTION DEFINITIONS #####
def create_schedule (loan, rate, term):
  #specific formaitng for the output schedule
  # ^ # of spaces 
  output = str.format(f"{'Payment Number':^15}{'Payment':>10}{'':5}{'Interest':>13} {'':5}{'Principle':>13}{'':5}{'Balance':>13}\n")

  n = term * 12
  payment = loan * ((rate*((1+rate)**n))/(((1+rate)**n) -1))
  balance = loan 

  for i in range(1,(term*12) + 1): 
    interest_payment = balance * rate 
    principle_payment = payment - interest_payment
    balance = balance - principle_payment  

    output += str.format(f"{i:^15}(${payment:10,.2f}){'':5}(${interest_payment:10,.2f}){'':5}(${principle_payment:10,.2f}){'':5}${balance:10,.2f}\n")

  return output

  
##### MAIN PROGRAM #####
def main():
  print(create_schedule(20000,(0.05/12), 2))

main()