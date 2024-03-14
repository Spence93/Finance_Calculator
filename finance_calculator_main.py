# Imports
from Investment_class import Calculator

# Global Variables
menu = "\nPlease select from the following options:\n"
menu += "\n1. Investment"
menu += " - Calculate the amount of interest you'll earn on your investment"
menu += "\n2. Bond"
menu += " - Calculate the amount you'll have to pay on a home loan"
menu += "\n3. Exit program"


# ------------ Functions ------------#
def investment_inputs():
    """
    The function `investment_inputs` takes user inputs for deposit amount, interest rate, and investment
    period, validates the inputs, and returns a `Calculator` object with the input data.
    :return: The `investment_inputs` function is returning an instance of the `Calculator` class with
    the investment data provided by the user (deposit amount, interest rate, and number of years).
    """
    prompts = ["\nPlease enter the amount of money you would like to deposit: ",
               "\nPlease enter the interest rate percentage (Do not enter the '%' sign): ",
               "\nHow many years do you plan on investing for?: "]
    deposit = 0
    interest_rate = 0
    years = 0
    calc_data = [deposit, interest_rate, years]
    counter = 0

    while counter < len(prompts):
        data = (input(prompts[counter]))

        if float(data.isdigit()) and float(data) > 0:
            data = float(data)
            calc_data[counter] = data
            counter += 1

        elif counter == 1 and float(data.replace(".", "").isnumeric()) and float(data) > 0:
            data = float(data)
            calc_data[counter] = data
            counter += 1

        else:
            print("Your input must be a number and greater than 0")
            continue

    return Calculator(calc_data[0], calc_data[1], calc_data[2])


def bond_inputs():
    """
    The function `bond_inputs` takes user inputs for house value, interest rate, and repayment period,
    validates the inputs, and returns a `Calculator` object with the provided data.
    :return: The function `bond_inputs()` is returning an instance of a `Calculator` class with the
    input values provided by the user for the current value of the house, interest rate, and number of
    months to repay the bond.
    """

    prompts = ["\nPlease enter the current value of your house: ",
               "\nPlease enter the interest rate percentage (Do not enter the '%' sign): ",
               "\nHow many months do you plan to repay the bond in?: "]
    house_value = 0
    interest_rate = 0
    months = 0
    calc_data = [house_value, interest_rate, months]
    counter = 0

    while counter < len(prompts):
        data = (input(prompts[counter]))

        if float(data.isdigit()) and float(data) > 0:
            data = float(data)
            calc_data[counter] = data
            counter += 1

        elif counter == 1 and data.replace(".", "").isnumeric() > 0:
            data = float(data)
            calc_data[counter] = data
            counter += 1

        else:
            print("Your input must be a number and greater than 0")
            continue

    return Calculator(calc_data[0], calc_data[1], months=calc_data[2])


# ------------ Main ------------#
def main():
    print("-" * 35)
    print("Welcome to your Finance Calculator")
    print("-" * 35)

    while True:
        print(menu)
        user_input = input("-> ")

        # Investment section
        if user_input == "1":
            investment_calc = investment_inputs()

            interest_input = input(
                "\nPlease choose:\n1. Simple Interest\n2. Compound Interest\n-> ")

            if interest_input == "1":
                investment_calc.investment_simple()
                input("Press enter to return to main menu ")

            elif interest_input == "2":
                investment_calc.investment_compound()
                input("Press enter to return to main menu ")

        # Bond section
        elif user_input == "2":
            bond_calc = bond_inputs()
            bond_calc.bond_calculation()
            input("Press enter to return to main menu ")

        elif user_input == "3":
            print("Goodbye")
            break

        else:
            print("Incorrect option, please choose again")


if __name__ == "__main__":
    main()
