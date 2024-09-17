# 20240916-ways_to_score-gist

**Gist file**: [https://gist.github.com/athursto/2c976e28eb865ce71725b766cb221df7](https://gist.github.com/athursto/2c976e28eb865ce71725b766cb221df7)

**Description**: Cassidy's interview question of the week: a function to find the minimum number of rows people can
sit in with various group sizes

## min_rows.py

```Python

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
```