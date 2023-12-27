import math
"""
- A finance calculator to determine users choice of investment 
    or bond calculators.
- If the user chooses investment, they get a choice of interest type "simple or compound"
    Depending on their choice, they will be asked to input relevent information 
    .to perform the calculation
The program will run if-elif-else statements to filter through the users inputs,
    to output the calculation chosen.
"""


print('''Investment - to calculate the amount of interest you'll earn on your investment
      Bond - to calculate the amount you'll have to pay on a home loan''')
interest_type = ""
# Initial menu choice to start the program
while interest_type != "investment" and interest_type != "bond":
    interest_type = input(
        "Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If statement to take user to the investment inputs and calculations
if interest_type == "investment":

    while True:
        try:
            deposit = float(input(
                """Please enter the amount of money you would like to deposit: """))
            if deposit < 1:
                print("Value must be greater than 0")
                continue
        except ValueError:
            print("Input must be a number ")
            continue
        break

    while True:
        try:
            interest_rate = float(input(
                "Please enter the interest rate percentage (Do not enter the '%' sign): "))
            if interest_rate < 1:
                print("Value must be greater than 0")
                continue
        except ValueError:
            print("Input must be a number, please enter again")
            continue
        # dividing by 100 here to be used in the end calculation
        interest_rate = interest_rate / 100
        break

    while True:
        try:
            investment_years = float(
                input("How many years do you plan on investing for?: "))
            if investment_years < 1:
                print("Value must be greater than 0")
                continue
        except ValueError:
            print("Number of years must be enterered as a number")
            continue
        break
    # Asking for user input here to determine if the simple or compound interest calculation is used
    interest = ""
    while interest != "simple" and interest != "compound":
        interest = input(
            "Please choose an interest type 'Simple' or 'Compound': ").lower()

    if interest == "simple":
        # Simple interest calculation for investment choice
        total_simple = deposit * (1 + interest_rate * investment_years)
        print(f"You will have £{round(total_simple, 2)} in your account")

        # Compound interest calculation for investment choice
    else:
        total_compound = deposit * \
            math.pow((1 + interest_rate), investment_years)
        print(f"You will have £{round(total_compound, 2)} in your account")

# Elif statement to ask the user for inputs for the bond calculation
elif interest_type == "bond":
    while True:
        try:
            house_value = int(
                input("Please enter the current value of your house: "))
            if house_value < 1:
                print("Houes Value must be greater than 0")
                continue
        except ValueError:
            print("House value must be entered as a whole number")
            continue
        break

    while True:
        try:
            bond_interest = float(
                input("What is the interest rate? (Do not enter the '%' sign): "))
            if bond_interest < 1:
                print("Value must be greater than 0")
                continue
        except ValueError:
            print("Input must be a number, please enter again")
            continue
        # dividing these variables so they can be used in the calculation at the end
        bond_interest = bond_interest / 100
        monthly_interest = bond_interest / 12
        break

    while True:
        try:
            bond_months = int(
                input("How many months do you plan to repay the bond in?: "))
            if bond_months < 1:
                print("Value must be greater than 0")
                continue
        except ValueError:
            print("Value must be greater than 0")
            continue
        break
    # Bond calculation to output the users monthly payments
    try:
        repayment = (monthly_interest * house_value) / \
            (1-(1 + monthly_interest) ** (- bond_months))
        print(f"Your monthly payment would be £{round(repayment, 2)} ")
    except ValueError:
        print("Error, you cannot divide by Zero, please check your inputs")
    except ZeroDivisionError:
        print("An error has occured, you cannot divide by Zero")

else:
    print("Incorrect option, please try again")
