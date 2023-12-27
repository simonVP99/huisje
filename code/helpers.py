def calculate_loan_cost(loan_amount, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12  # Convert annual rate to monthly and decimal
    total_number_of_payments = loan_term * 12  # Convert years to months

    # Monthly Payment Calculation using the formula
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_number_of_payments) / ((1 + monthly_interest_rate) ** total_number_of_payments - 1)

    total_cost = monthly_payment * total_number_of_payments  # Total cost of the loan

    return monthly_payment, total_cost

