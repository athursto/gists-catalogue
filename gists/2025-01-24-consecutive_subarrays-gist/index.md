# 2024-01-24-consecutive_subarrays-gist

**Gist file**: [https://gist.github.com/athursto/bfaaaf972035a97889995f15294d96af](https://gist.github.com/athursto/bfaaaf972035a97889995f15294d96af)

**Description**: Cassidy's interview question of the week: a function to find longest consecutive subsequence with differences of 1 or -1 between elements

## cassidoo0124.py

```Python
"""
01.25.2025
Given a list of integers, write a function that finds the longest subsequence where the difference between consecutive elements is either 1 or -1. Return the length of this subsequence.."""
def find_consecutive_subarrays(array):
    front = 0
    back = 1
    max_diff = 0
    diff_count = 1
    while back < len(array): #overall loop that stops when the back pointer is at the end of the list
        #print(f"checking {array[front]}, {array[back]}")
        if abs(array[front] - array[back]) == 1:
            #print(f"diff of 1 found at positions {front} and {back}")
            diff_count +=1
            back += 1
            front +=1
            max_diff = max(diff_count, max_diff) #Keep track of how many in a row have that difference-- if it ever is greater than max, it's the new max
            #print(f"max is now {max_diff}")
        else:
            diff_count = 1
            front += 1
            back = front + 1

    return max_diff


assert find_consecutive_subarrays([10,11,7,8,9,12]) == 3
assert find_consecutive_subarrays([4,2,3,1,5]) == 2
assert find_consecutive_subarrays([1,2,3,4,5]) == 5
```