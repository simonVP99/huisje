def calculate_loan_cost(loan_amount, annual_interest_rate, loan_term):
    """
    Calculate the monthly payment and total cost of a loan.

    Parameters:
    - loan_amount: The total amount of the loan.
    - annual_interest_rate: The annual interest rate of the loan (as a decimal).
    - loan_term: The term of the loan in years.

    Returns:
    - monthly_payment: The monthly payment amount for the loan.
    - total_cost: The total cost of the loan over its entire term.
    """
    # Convert the annual interest rate to a monthly rate (decimal)
    monthly_interest_rate = annual_interest_rate / 12

    # Convert the loan term from years to months
    total_number_of_payments = loan_term * 12

    # Calculate the monthly payment using the formula for an annuity
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_number_of_payments) / ((1 + monthly_interest_rate) ** total_number_of_payments - 1)

    # Calculate the total cost of the loan over its term
    total_cost = monthly_payment * total_number_of_payments

    return monthly_payment, total_cost


def update_salary(current_salary, inflation_rate, salary_growth_rate):
    """
    Calculate the new salary by applying inflation and salary growth rates.

    Parameters:
    - current_salary: The current salary amount.
    - inflation_rate: Annual inflation rate.
    - salary_growth_rate: Annual salary growth rate.

    Returns:
    - Updated salary considering both inflation and salary growth.
    """
    return current_salary * (1 + inflation_rate) * (1 + salary_growth_rate)


def calculate_net_value_addition(salary, outstanding_capital, expenditure_percentage):
    """
    Calculate the net value addition after accounting for expenditures.

    Parameters:
    - salary: The person's salary.
    - outstanding_capital: The current outstanding capital or debt.
    - expenditure_percentage: The percentage of the salary spent on expenditures.

    Returns:
    - Net value addition to the person's finances.
    - Net salary after accounting for the outstanding capital.
    """
    net_salary = salary / 2  # Assuming some form of taxation or other deductions
    net_value_addition = net_salary * (1 - expenditure_percentage)
    return net_value_addition, net_salary

def update_yearly_status(salary, house_value, debt, annual_loan_payment, property_tax, inflation_rate, salary_growth_rate, property_appreciation_rate):
    """
    Update the financial status for the year, including salary, house value, and debt.

    Parameters:
    - salary: Current annual salary.
    - house_value: Current value of the house.
    - debt: Current outstanding debt.
    - annual_loan_payment: The annual payment for the loan.
    - property_tax: Annual property tax.
    - inflation_rate: Annual inflation rate.
    - salary_growth_rate: Annual salary growth rate.
    - property_appreciation_rate: Annual rate at which the property value appreciates.

    Returns:
    - Updated salary, house value, and debt after a year.
    - The net cash gain or loss for the year.
    """
    # Calculate the cash gain or loss for the year
    cash_gain = salary / 2 * (1 - expenditure_percentage) - annual_loan_payment - property_tax

    # Update salary, house value, and debt
    updated_salary = salary * (1 + inflation_rate) * (1 + salary_growth_rate)
    updated_house_value = house_value * (1 + inflation_rate) * (1 + property_appreciation_rate)
    updated_debt = debt - annual_loan_payment

    return updated_salary, cash_gain, updated_house_value, updated_debt
