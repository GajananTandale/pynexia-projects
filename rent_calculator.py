def get_positive_float(prompt):
    """Safely gets a non-negative float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_roommate_count(prompt):
    """Safely gets a positive integer for the number of roommates."""
    while True:
        try:
            count = int(input(prompt))
            if count <= 0:
                print("Number of people must be at least 1.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_rent_split(rent, food, electricity_units, rate_per_unit, internet, people):
    """Calculates total expenses and the per-person share."""
    electricity_bill = electricity_units * rate_per_unit
    total_expense = rent + food + electricity_bill + internet
    per_person = total_expense / people
    return electricity_bill, total_expense, per_person


def main():
    print("=== Monthly Rent & Expense Calculator ===\n")

    rent = get_positive_float("Enter total monthly house/flat rent: ")
    food = get_positive_float("Enter total food/grocery expenses: ")
    electricity_units = get_positive_float("Enter total electricity units consumed: ")
    rate_per_unit = get_positive_float("Enter charge per electricity unit: ")
    internet = get_positive_float("Enter Wi-Fi / maintenance charges: ")
    people = get_roommate_count("Enter number of people sharing the flat: ")

    electricity_bill, total_expense, per_person = calculate_rent_split(
        rent, food, electricity_units, rate_per_unit, internet, people
    )

    print("\n--- Monthly Expense Summary ---")
    print(f"Base Rent:        {rent:.2f}")
    print(f"Food & Groceries: {food:.2f}")
    print(f"Electricity Bill: {electricity_bill:.2f}")
    print(f"Internet/Maint.:  {internet:.2f}")
    print("-" * 31)
    print(f"Total Expense:    {total_expense:.2f}")
    print(f"Each Person Pays: {per_person:.2f}")


if __name__ == "__main__":
    main()
