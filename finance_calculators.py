#Import the math module
import math

#Display and explain the options that the user can select
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("\ninvestment \t- to calculate the amount of interest you'll earn on interest")
print("bond \t \t- to calculate the amount you'll have to pay on a home loan")

#Assign user input to variable and format input to lowercase
user_choice = input("Please make your selection: ").lower()

#If user selects 'investment', proceed with the investment calculator:
if user_choice == "investment":
    #Ask for user input:
    deposit = float(input("How much are you depositing? "))
    invest_rate = int(input("What is the current interest rate (in percentage)? "))/100
    invest_period = int(input("For how long are you planning to invest the money (in years)? "))
    interest = input("Do you prefer 'simple' or 'compound' interest? ").lower()

    #Determine how investment should be calculated, depending on user's choice of either 'simple' or 'compound'
    if interest == "simple":
        total_investment = deposit * (1 + invest_rate * invest_period)
        print(f"In {invest_period} years, you're investment will be R{'{:,.2f}'.format(total_investment)}")

    else:
        total_investment = deposit * math.pow((1 + invest_rate),invest_period)
        print(f"In {invest_period} years, you're investment will be R{'{:,.2f}'.format(total_investment)}")

#If user selects 'bond', proceed with the bond calculator:
elif user_choice == "bond":
    #Ask user for input and assign input to variables
    present_value = float(input("What is the present value of the house? "))
    bond_rate = int(input("What is the current interest rate (in percentage)? "))/100
    bond_interest = bond_rate / 12 #change yearly interest to monthly interest
    repayment_period = int(input("Duration of loan (in months): "))


    #Calculate monthly repayment for bond
    monthly_repayment = (bond_interest * present_value) / (1 - math.pow((1 + bond_interest),(repayment_period * -1)))

    #Print the results
    print(f"The total monthly repayment of your bond will be R{'{:,.2f}'.format(monthly_repayment)}")

#If user did not make a valid selection, print error message.
else:
    print("You have not made a valid selection. Please restart this application.")



