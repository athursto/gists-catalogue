# 20241009-grocery_list-gist

**Gist file**: [https://gist.github.com/athursto/4f2e4046bc2e027ddce1f8e4f2b91937](https://gist.github.com/athursto/4f2e4046bc2e027ddce1f8e4f2b91937)

**Description**: Cassidy's interview question of the week: a function to find how much you need to buy for a recipe based on what's in the pantry

## grocery_list.py

```Python
import datetime

"""10.10.2024
Given a list of ingredients needed for a recipe, represented as strings, and a list of ingredients you have in your 
pantry, write a function to return the minimum number of additional ingredients you need to buy to make the recipe. If
 you want to do some extra credit, add expiration dates to the pantry items, and only account for food that isn't 
 expired.

"""
import datetime

def grocery_list(needed, stock):
    format_string = "%m/%d/%y"
    for i in range(len(stock) - 1):
        for key, value in stock[i].items():
            if datetime.datetime.strptime(value,format_string ) < datetime.datetime.now():
                del stock[i]
    valid_pantry = set()
    for dict_ in stock:
        valid_pantry.update(dict_.keys())
    matches = set(needed).intersection(valid_pantry)
    print(matches)
    return len(needed) - len(matches)

recipe1 = ["eggs", "flour", "sugar", "butter"]
pantry1 = [{"sugar": "5/6/23"},
           {"butter": "11/1/24"},
           {"milk":"11/2/24"}]
```