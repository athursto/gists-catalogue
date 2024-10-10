# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

"""
9.17.2024
You are given an array of people represented by integers, where each number corresponds to the number of people in a
 group. Determine the minimum number of rows required to seat everyone such that no group is split across different
  rows. You can assume no group will be larger than a given row size!"""

import itertools

def min_rows(array, n):
    power_set = []
    groups_to_check = array
    sum_list = []
    for k in range(n):
        power_set.extend(itertools.combinations(array, k))
    sorted_list = sorted(power_set, key=sum, reverse=True)
    while len(groups_to_check) > 0:
        for item in sorted_list:
            if sum(item) <= n and sum(item) > 0 and set(item).issubset(groups_to_check):
                sum_list.append(item)
                # print(f"sum_list is now {sum_list}")
                for ele in item:
                    groups_to_check.remove(ele)
    return len(sum_list)
            #remove all those added from items_to_check

array_1 = [4, 8, 3, 5, 6]
array_2 = [4, 5, 4, 3, 3]
array_3 = [7, 7, 8, 9, 6]

assert min_rows(array_1, 10) == 3
assert min_rows(array_2, 10) ==2
assert min_rows(array_3, 10) ==5

"""9.25.2024"""
"""
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
        # print(f"evaluating {item}")
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

# assert grocery_list(recipe1, pantry1) == 3



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
