# 2026-10-27-costume_swap-gist

**Gist file**: https://gist.github.com/athursto/eccdc16c653f09b9ee6ecb9f40c32aee

**Description**: Cassidy's interview question of the week: a function to find how many swaps to get a costume to the right place 

```python
def halloweenSwap(costumes):
    location_dict = {}
    swaps = 0
    for i in range(len(costumes)):
        location_dict[i] = costumes[i]

    for j in range(len(location_dict)):
        while j != location_dict[j]:
            holder = location_dict[j]
            # print(f"wrong position, {j} is holding {location_dict[j]}, temp position is {holder}")
            location_dict[j], location_dict[holder] = location_dict[holder], location_dict[j]
            swaps +=1
            # print(f"location_dict is now {location_dict}, total swaps {swaps}")




assert halloweenSwap([0, 2, 1, 3]) == 2
assert halloweenSwap([4, 3, 2, 1, 0]) == 2
assert halloweenSwap([2, 3, 4, 0, 1]) == 4
```