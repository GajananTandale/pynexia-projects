from datetime import datetime


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


def get_flatmate_names(count):
  """Collects names for each flatmate or assigns default labels."""
  names = []
  print("\nEnter flatmate names (or press Enter to use default names):")
  for i in range(1, count + 1):
    name = input(f"  Flatmate {i} name: ").strip()
    names.append(name if name else f"Flatmate {i}")
  return names


def calculate_rent_split(
    rent, electricity_units, rate_per_unit, water, internet, shared_other, people
):
  """Calculates total expenses and the per-person share."""
  electricity_bill = electricity_units * rate_per_unit
  total_expense = rent + electricity_bill + water + internet + shared_other
  per_person = total_expense / people
  return electricity_bill, total_expense, per_person


def build_summary_report(
    rent,
    electricity_bill,
    water,
    internet,
    shared_other,
    total_expense,
    per_person,
    names,
):
  """Formats the itemized breakdown into a clean text report."""
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  lines = [
      "==========================================",
      "      MONTHLY RENT & EXPENSE SUMMARY      ",
      f"      Generated: {timestamp}      ",
      "==========================================",
      f"Base Rent:             {rent:>10.2f}",
      f"Electricity Bill:      {electricity_bill:>10.2f}",
      f"Water Bill:            {water:>10.2f}",
      f"Internet / Wi-Fi:      {internet:>10.2f}",
      f"Other Shared Expenses: {shared_other:>10.2f}",
      "------------------------------------------",
      f"TOTAL MONTHLY EXPENSE: {total_expense:>10.2f}",
      "==========================================",
      "ITEMIZED SHARE PER FLATMATE:",
  ]
  for name in names:
    lines.append(f"  - {name:<20} {per_person:>10.2f}")
  lines.append("==========================================")
  return "\n".join(lines)


def export_summary(report_text, filename="rent_summary.txt"):
  """Exports the formatted summary breakdown to a text file."""
  with open(filename, "w", encoding="utf-8") as file:
    file.write(report_text)
  return filename


def main():
  print("=== Monthly Rent & Shared Expense Calculator ===\n")

  rent = get_positive_float("Enter total monthly rent: ")
  electricity_units = get_positive_float(
      "Enter total electricity units consumed: "
  )
  rate_per_unit = get_positive_float("Enter charge per electricity unit: ")
  water = get_positive_float("Enter total water bill: ")
  internet = get_positive_float("Enter total internet / Wi-Fi bill: ")
  shared_other = get_positive_float(
      "Enter other shared expenses (groceries/maintenance): "
  )

  people = get_roommate_count("\nEnter number of flatmates/tenants: ")
  names = get_flatmate_names(people)

  electricity_bill, total_expense, per_person = calculate_rent_split(
      rent,
      electricity_units,
      rate_per_unit,
      water,
      internet,
      shared_other,
      people,
  )

  report = build_summary_report(
      rent,
      electricity_bill,
      water,
      internet,
      shared_other,
      total_expense,
      per_person,
      names,
  )

  print("\n" + report)

  choice = (
      input("\nDo you want to export this summary to a file? (y/n): ")
      .strip()
      .lower()
  )
  if choice == "y":
    custom_name = input(
        "Enter filename (press Enter for 'rent_summary.txt'): "
    ).strip()
    filename = (
        custom_name
        if custom_name
        else f"rent_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )
    if not filename.endswith(".txt"):
      filename += ".txt"
    saved_file = export_summary(report, filename)
    print(f"Summary successfully exported to '{saved_file}'!")


if __name__ == "__main__":
  main()
