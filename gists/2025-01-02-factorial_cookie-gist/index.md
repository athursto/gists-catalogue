# 2024-01-02-factorial_cookie-gist

**Gist file**: [https://gist.github.com/athursto/0aa74dcfb63a484c48537222762919fb](https://gist.github.com/athursto/0aa74dcfb63a484c48537222762919fb)

**Description**: Cassidy's interview question of the week: a function to find trailing zeros of a factorial

## factorial_cookie.py

```Python

import math


def count_round_cookies(num):
    """
    At the Magic Cookie Factory, cookies are baked in factorial quantities. A cookie is "perfectly round" if its size ends with a zero. Write a function to determine how many perfectly round cookies will be made when baking with n! ingredients.
    """
    if type(num) != int:  # Input check-- make sure what's entered could have a factorial
        print(f"{num} is not an integer-- please enter an integer")
        return
    factorial = math.factorial(num)  # Calculate factorial of input
    # print(factorial)
    list_version = [int(digit) for digit in str(factorial)]  # Turn factorial into its digits
    # print(list_version)
    trail_count = 0
    # loop backwards through list, stopping when you encounter a non-zero char
    for i in range(len(list_version) - 1, -1, -1):
        if list_version[i] == 0:
            trail_count += 1
        else:
            break
    # print(f"trail_count is {trail_count}")
    return trail_count


assert count_round_cookies(5) == 1
assert count_round_cookies(10) == 2
assert count_round_cookies(100) == 24


```