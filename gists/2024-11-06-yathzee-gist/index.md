# 202411-06-yahtzee-gist

**Gist file**: [https://gist.github.com/athursto/c35e3994b2d8355eea278280cfce2838](https://gist.github.com/athursto/c35e3994b2d8355eea278280cfce2838)

**Description**: Cassidy's interview question of the week: a function to implement a round of Yahtzee

## cassidoo1106.py

```Python

"""11.06.2024
Implement a round of the game Yahtzee, where 5 dice are randomly rolled, and the function returns what options the user has to score more than 0 points. Extra credit: implement all 13 rounds!

"""
import random 

def yahtzee_game():
    dice_list = []
    result_list = []
    possibilities = {1: "aces", 2: "twos", 3: "threes", 4: "fours",
                     5: "fives", 6: "sixes"}
    #subsets to use for scoring later
    small_straights = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
    large_straights = [[1, 2, 3, 4,5], [2, 3, 4, 5, 6]]
    dice_dict = {}
    for _ in range(6):
        # roll the dice and save its result
        dice_list.append(random.randint(1, 6))
    #Create a frequency dictionary for scoring
    for item in dice_list:
        if item not in dice_dict:
            dice_dict[item] = 1
        else:
            dice_dict[item] += 1
    # possibility maker
    for key in dice_dict:
        # print(f"checking {key}")
        if dice_dict[key] in possibilities:
            result_list.append(possibilities[key])
    if any(value == 3 for value in dice_dict.values()):
        result_list.append("three of a kind")
    if any(value == 4 for value in dice_dict.values()):
        result_list.append("four of a kind")
    if any(value == 5 for value in dice_dict.values()):
        result_list.append("Yahtzee")
    if any(value == 3 for value in dice_dict.values()) and any(value ==2 for value in dice_dict.values()):
        result_list.append("full house")
    for straight in small_straights:
        if set(straight).issubset(set(dice_list)):
            result_list.append("small straight")
            break
    for straight in large_straights:
        if set(straight).issubset(set(dice_list)):
            result_list.append("large straight")
            break
    print(f"dice rolled are {dice_list}")
    result = {"dice": dice_list, "options": result_list}
    return result
```