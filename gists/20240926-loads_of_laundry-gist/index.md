# 20240926-loads_of_laundry-gist

**Gist file**: [https://gist.github.com/athursto/1ff941cced95fe05ba0e7efe81a5763a](https://gist.github.com/athursto/1ff941cced95fe05ba0e7efe81a5763a)

**Description**: Cassidy's interview question of the week: a function to find the minimum number of loads of laundry
with various restrictions

## min_loads.py

```Python

"""
9.26.2024
You're designing a smart laundry sorting system. You have a list of clothing items, each with a color and a fabric type.
 Sort these items into the minimum number of loads n and return n, where items of the same color can be washed together,
  and some different fabric types cannot be mixed together. "Normal" fabric types can be mixed with "heavy", but 
  "delicate" cannot be mixed with anything.
"""

load1 = [
    ["red", "normal"],
    ["blue", "normal"],
    ["red", "delicate"],
    ["blue", "heavy"]
]

load2 = [
    ["white", "normal"],
    ["white", "delicate"],
    ["white", "normal"],
    ["white", "heavy"]
]

load3 = [
    ["white", "normal"],
    ["red", "normal"],
    ["red", "normal"],
    ["white", "delicate"],
    ["blue", "delicate"],
    ["white", "normal"],
    ["white", "heavy"]
]

load4 = [
    ["white", "normal"],
    ["red", "normal"],
    ["red", "normal"],
    ["white", "normal"],
    ["white", "heavy"]
]


def min_laundry_loads(load):
    load_dict = {"delicate": 0}
    for item in load:
        print(f"evaluating {item}")
        color = item[0]
        if item[1] == "delicate":
            load_dict["delicate"] += 1
        else:
            if item[0] in load_dict.keys():
                load_dict[color] +=1
                # print(f"incrementing {color}, dict is now {load_dict}")
            else:
                load_dict[color] = 1
                # print(f"adding {color}, dict is now {load_dict}")
    colors = list(load_dict.keys())
    colors.remove("delicate")
    num_delicates = load_dict["delicate"]
    return len(colors) + num_delicates


assert min_laundry_loads(load1) == 3
assert min_laundry_loads(load2) == 2
assert min_laundry_loads(load3) == 4
assert min_laundry_loads(load4) == 2
```