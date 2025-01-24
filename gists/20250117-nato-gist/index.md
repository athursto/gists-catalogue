# 2024-01-17-nato-gist

**Gist file**: [https://gist.github.com/athursto/0aa74dcfb63a484c48537222762919fb](https://gist.github.com/athursto/0aa74dcfb63a484c48537222762919fb)

**Description**: Cassidy's interview question of the week: a function to find trailing zeros of a factorial

## factorial_cookie.py

```Python
def nato_alphabet(string):
    result = []
    nato_dict = {"A":"Alfa",
    "B":	"Bravo",
    "C":	"Charlie",
    "D": "Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":	"Golf",
    "H":	"Hotel",
    "I":	"India",
    "J":	"Juliett",
    "K":	"Kilo",
    "L":	"Lima",
    "M":	"Mike",
    "N":	"November",
    "O":	"Oscar",
    "P":	"Papa",
    "Q":	"Quebec",
    "R":	"Romeo",
    "S":	"Sierra",
    "T":	"Tango",
    "U":	"Uniform",
    "V":	"Victor",
    "W":	"Whiskey",
    "X":	"Xray",
    "Y":	"Yankee",
    "Z":	"Zulu"}

    nums = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
            "8":"Eight", "9":"Nine"}
    for char in string:
        if char.upper() in nato_dict:
            result.append(nato_dict[char.upper()])
        elif char in nums:
            result.append(nums[char])
        elif char.isspace():
            result.append("space")
        else:
            result.append("invalid_entry")
    return " ".join(result)

print(nato_alphabet("2alis on*"))
```