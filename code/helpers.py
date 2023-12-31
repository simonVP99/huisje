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

def update_yearly_status(salary, house_value, debt, annual_loan_payment, property_tax, inflation_rate, salary_growth_rate, property_appreciation_rate, expenditure_percentage):
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


def calculate_house_purchase_costs(purchase_price, loan_percentage, additional_costs_percentage, loan_interest_rate, loan_term_years):
    """
    Calculate various financial aspects related to purchasing a house.

    Parameters:
    - purchase_price (float): Purchase price of the house.
    - loan_percentage (float): Percentage of the purchase price financed through a loan.
    - additional_costs_percentage (float): Additional costs as a percentage of the purchase price.
    - loan_interest_rate (float): Annual interest rate of the loan.
    - loan_term_years (int): Loan term in years.

    Returns:
    - total_loan_cost (float): Total cost of the loan.
    - down_payment (float): Down payment including additional purchase costs.
    - monthly_loan_payment (float): Monthly loan payment.
    - total_purchase_cost (float): Total cost of purchasing the house including the loan and additional costs.
    """
    # Calculate the loan amount based on the purchase price and loan percentage
    loan_amount = purchase_price * loan_percentage

    # Calculate additional costs as a percentage of the purchase price
    additional_costs = purchase_price * additional_costs_percentage

    # Calculate the total loan cost using the loan amount, interest rate, and term
    _, total_loan_cost = calculate_loan_cost(loan_amount, loan_interest_rate, loan_term_years)

    # Calculate the initial out-of-pocket expense (down payment + additional costs)
    down_payment = purchase_price * (1 - loan_percentage) + additional_costs

    # Calculate annual and monthly loan payments
    annual_loan_payment = total_loan_cost / loan_term_years
    monthly_loan_payment = annual_loan_payment / 12

    # Calculate the total price of purchasing the house (down payment + total loan cost)
    total_purchase_cost = down_payment + total_loan_cost

    return total_loan_cost, down_payment, monthly_loan_payment, total_purchase_cost
