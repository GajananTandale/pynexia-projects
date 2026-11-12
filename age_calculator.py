import calendar
from datetime import date, datetime


def calculate_exact_age(birth_date, current_date):
  years = current_date.year - birth_date.year
  months = current_date.month - birth_date.month
  days = current_date.day - birth_date.day

  if days < 0:
    months -= 1

    prev_month = current_date.month - 1 if current_date.month > 1 else 12
    prev_year = (
        current_date.year if current_date.month > 1 else current_date.year - 1
    )


    days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
    days += days_in_prev_month


  if months < 0:
    years -= 1
    months += 12

  return years, months, days


def main():
  print("=== Exact Age Calculator ===")
  today = date.today()

  while True:
    dob_input = input(
        "\nEnter your Date of Birth (YYYY-MM-DD) or 'q' to quit: "
    ).strip()

    if dob_input.lower() == "q":
      print("Exiting Age Calculator. Goodbye!")
      break

    try:
    
      birth_date = datetime.strptime(dob_input, "%Y-%m-%d").date()

      # Validate against future dates
      if birth_date > today:
        print(
            "Error: Date of birth cannot be in the future. Please try again."
        )
        continue

      
      years, months, days = calculate_exact_age(birth_date, today)
      print(
          f"\nYour exact age is: {years} years, {months} months, and"
          f" {days} days."
      )

    except ValueError:
      print(
          "Error: Invalid date or format. Please use YYYY-MM-DD (e.g.,"
          " 2000-02-29)."
      )


if __name__ == "__main__":
  main()
