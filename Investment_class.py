import math


class Calculator:

    def __init__(self, deposit: float, interest_rate: float, years: float = None, months: float = None) -> float:
        self.deposit = deposit
        self.interest_rate = interest_rate
        self.years = years
        self.months = months

    def investment_simple(self):
        """
        The function calculates the total amount in an investment account using a simple interest
        formula.
        """
        total_simple = self.deposit * \
            (1 + (self.interest_rate / 100) * self.years)
        print(f"You will have £{round(total_simple, 2)} in your account")

    def investment_compound(self):
        """
        The function calculates the total amount in an investment account after a certain number of
        years with compound interest.
        """
        total_compound = self.deposit * \
            math.pow((1 + (self.interest_rate / 100)), self.years)
        print(f"\nYou will have £{round(total_compound, 2)} in your account")

    def bond_calculation(self):
        """
        This Python function calculates the monthly payment for a bond based on the interest rate,
        deposit amount, and number of months.
        """
        interest = self.interest_rate / 100
        monthly_interest = interest / 12
        repayment = (monthly_interest * self.deposit) / \
            (1-(1 + monthly_interest) ** (- self.months))
        print(f"\nYour monthly payment would be £{round(repayment, 2)} ")
