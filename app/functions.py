def calculate_grades(grades):

    if not grades:
        return "No grades provided."

    # Calculate the average grade
    average = sum(grades) / len(grades)

    # Determine the letter grade based on standard grading logic
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Example usage
grades_list = [85, 90, 78, 92, 88]
letter_grade = calculate_grades(grades_list)
print("The letter grade is:", letter_grade)


def loan_amortization(loan_amount, interest_rate, loan_term_years):
    # Input validation
    if loan_amount <= 0 or loan_term_years <= 0:
        raise ValueError("Loan amount and loan term must be greater than zero.")

    loan_term_months = loan_term_years * 12  # Convert loan term to months
    monthly_interest_rate = interest_rate / 12 / 100  # Calculate monthly interest rate

    # Calculate the monthly payment
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months))
    else:
        monthly_payment = loan_amount / loan_term_months  # Handle no interest case

    return monthly_payment


# Example usage
loan_amount = 100000  # Loan amount in dollars
interest_rate = 5  # Annual interest rate in percentage
loan_term_years = 15  # Loan term in years

monthly_payment = loan_amortization(loan_amount, interest_rate, loan_term_years)
print(f"Monthly Payment: ${monthly_payment:.2f}")
