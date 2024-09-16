# 20240916-ways_to_score-gist

**Gist file**: [https://gist.github.com/athursto/2c976e28eb865ce71725b766cb221df7](https://gist.github.com/athursto/2c976e28eb865ce71725b766cb221df7)

**Description**: Cassidy's interview question of the week: a function to find the most unique ways a football team can get a given score

## ways_to_score.py

```Python
import itertools

"""9.16.2024
You are given an integer n representing the total points a team wants to score in an American football game. You need
 to determine the number of unique ways the team can achieve exactly n points using any combination of touchdowns
  (6 points), field goals (3 points), or safeties (2 points).

"""

def ways_to_score(n):
    power_set = []
    sum_list = []
    for k in range(n):
        power_set.extend(itertools.combinations_with_replacement([2,3,6], k))
    for item in power_set:
        if sum(item) == n:
            sum_list.append(item)
    # print(sum_list)
    return len(sum_list)


assert ways_to_score(12) == 6
assert ways_to_score(5) == 1
assert ways_to_score(6) == 3
```