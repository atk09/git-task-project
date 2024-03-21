import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
 # Convert user_input to lowercase for case-insensitivity
try:
    user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() 

    # Check if the user entered 'investment' or 'bond'
    if user_input == 'investment':
        print("Processing investment interest...")
    elif user_input == 'bond':
        print("Processing bond interest...")
    else:
        # If the user enters invalid input values
        raise ValueError("Invalid input. Please enter 'investment' or 'bond' as valid values.")
# return error msg
except ValueError as ve:
    print(f"Error: {ve}")

# if user enters 'investment' then calculate investment interest     
if user_input == 'investment':
# Ask user to enter money to get deposited    
 P = int(input("Enter amount of money to be deposited: "))
# Ask user to enter interest rate and then divided by 100 and save as r_newRate
 r = int(input("Enter interest rate (as percentage, i.e: 8): "))
 r_newRate = r/100
# Ask user to enter no. of years being planned for investing 
 t = int(input("Number of years being planned on investing: "))
# check if the user enters values other than simple or compound and then calculate values accordingly
# verify the inputs as Simple or Compound and converting to lowercase for case-insensitivity
 try:
     
  user_invest = input("Please specify if you want 'Simple' or 'Compound' interest: ")
  # if the user enters 'simple' then calculate values accordingly
  if(user_invest.lower()=="simple"):
   A = P *(1 + r_newRate*t)
   print("Your total amound as a 'Simple' interest: "+ str(A))
  # if the user enters 'compound' then calculate values accordingly 
  elif(user_invest.lower()=="compound"):
   A = P * math.pow((1+r_newRate), t) 
   print("Your total amound as a 'Compound' interest: "+ str(A))
  else:
  # If the user enters values other than 'simple' or 'compound'
   raise ValueError("Invalid input. Please enter 'simple' or 'compound'.")   
 # throws error value
 except ValueError as ve:
  print(f"Error: {ve}")    
# if user enters 'bond' then calculates values accordingly      
if user_input == 'bond':
  # Ask user to enter present value of the house  
  P = int(input("Enter present value of the house: "))
  # Ask user to enter interest rate and divided by 100 before dividing by 12 for monthly interest and save as i_new
  i = int(input("Enter interest rate: "))
  i_new = (i/100)/12
  # Ask user to enter no. of months being planned to repay the bond
  n = int(input("Enter number of months being planned to take to repay the bond: "))
  repayment = (i_new * P)/(1 - (1 + i_new)**(-n))
  print("The total amount that you'll have to repay each month as a 'Bond' interest: "+ str(repayment))