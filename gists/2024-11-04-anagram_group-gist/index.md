# 202411-04-anagram_group-gist

**Gist file**: [https://gist.github.com/athursto/3d70dc2f701126fd92fffb647b9e7f8e](https://gist.github.com/athursto/3d70dc2f701126fd92fffb647b9e7f8e)

**Description**: Cassidy's interview question of the week: a function to group anagrams in a list

## anagram_group.py

```Python

"""11.04.2024
Given an array of strings, group the anagrams together.

"""

def group_anagrams(input_list):
    result_list = []
    seen_keys = []
    for word in input_list:
        # Sort the word to get a unique representation for its anagram group
        sorted_word = tuple(sorted(word))
        print(sorted_word)
        #If sorted word key is already in seen keys, add word to its group
        if sorted_word in seen_keys:
            index = seen_keys.index(sorted_word)
            result_list[index].append(word)
        else:
            seen_keys.append(sorted_word)
            result_list.append([word])
    return result_list


assert group_anagrams(["coffee", "donut", "ant", "tan"]) == [['coffee'], ['donut'], ['ant', 'tan']]
```