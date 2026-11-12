# Exact Age Calculator

A Python utility that calculates a person's exact age in **years, months, and days** from a given birth date.

## Features
* **Calendar-Accurate Calculation:** Uses Python's built-in `calendar` module (`calendar.monthrange`) to account for varying month lengths and leap years.
* **Zero External Dependencies:** Runs using only Python's standard library (`calendar` and `datetime`).

## Requirements
* Python 3.x

## How to Run
1. Clone or download the repository:
   ```bash
   git clone https://github.com
   cd pynexia-projects
   ```
2. Run the script from your terminal:
   ```bash
   python age_calculator.py
   ```

## Example Usage
If you import the `calculate_exact_age` function into another script:

```python
from datetime import date
from age_calculator import calculate_exact_age

birth = date(2000, 5, 15)
today = date.today()

# Prints exact age breakdown
calculate_exact_age(birth, today)
```
