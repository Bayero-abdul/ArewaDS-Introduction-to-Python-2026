"""
TODO: This program calculates a user's income tax based on their gross income 
and number of dependents.
"""

# TODO: constants
TAX_RATE = 0.20
EXEMPTION_PER_DEPENDENT = 10000.0

# input
grossIncome = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

# processing
taxableIncome = grossIncome - (dependents * EXEMPTION_PER_DEPENDENT)
tax = max(0.0, taxableIncome * TAX_RATE)

# output
print("The income tax is $" + str(tax))