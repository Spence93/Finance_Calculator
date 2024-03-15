import math


class Calculator:

    def __init__(self, deposit: float, interest_rate: float, years: float = None, months: float = None) -> float:
        self.deposit = deposit
        self.interest_rate = interest_rate
        self.years = years
        self.months = months



class InvestmentCalculator(Calculator):
    def __init__(self, deposit: float, interest_rate: float, years: float = None, months: float = None) -> float:
        super().__init__(deposit, interest_rate, years, months)

    def investment_simple(self):
        """
        The function calculates the total amount in an investment account using a simple interest
        formula.
        """
        total_simple = self.deposit * \
            (1 + (self.interest_rate / 100) * self.years)
        print("-" * 35)
        print(f"You will have £{round(total_simple, 2)} in your account")
        print("-" * 35)

    def investment_compound(self):
        """
        The function calculates the total amount in an investment account after a certain number of
        years with compound interest.
        """
        total_compound = self.deposit * \
            math.pow((1 + (self.interest_rate / 100)), self.years)
        print("-" * 35)
        print(f"You will have £{round(total_compound, 2)} in your account")
        print("-" * 35)


class BondCalculator(Calculator):

    def __init__(self, deposit: float, interest_rate: float, years: float = None, months: float = None) -> float:
        super().__init__(deposit, interest_rate, years, months)

    def bond_calculation(self):
        """
        This Python function calculates the monthly payment for a bond based on the interest rate,
        deposit amount, and number of months.
        """
        interest = self.interest_rate / 100
        monthly_interest = interest / 12
        repayment = (monthly_interest * self.deposit) / \
            (1-(1 + monthly_interest) ** (- self.months))
        print("-" * 35)
        print(f"Your monthly payment would be £{round(repayment, 2)} ")
        print("-" * 35)
