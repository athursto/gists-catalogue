# 2024-01-02-new_years-gist

**Gist file**: [https://gist.github.com/athursto/fe5f66e8d4d32e0b5df6387343886be2](https://gist.github.com/athursto/fe5f66e8d4d32e0b5df6387343886be2)

**Description**: Cassidy's interview question of the week: a function to say what day of the week new year's day is/was that year

## cassidoo0102.py

```Python

"""
01.02.2024
Given a year, return the day of the week for New Year's Day of that year."""

from datetime import date
def new_years_day(year):
    date_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    if type(year) == int and len(str(year)) == 4:
        ordinal_day = date_dict[date(year, 1,1).weekday()]
        return ordinal_day
    else:
        print(f"{year} is not in the format yyyy-- please enter a four-digit integer.")
        return

assert new_years_day(2025) == "Wednesday"


```