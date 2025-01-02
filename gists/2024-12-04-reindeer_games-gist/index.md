# 2024-12-04-reindeer_games-gist

**Gist file**: [https://gist.github.com/athursto/c984cb61211fbce7e6dd8db9456fa16f](https://gist.github.com/athursto/c984cb61211fbce7e6dd8db9456fa16f)

**Description**: Cassidy's interview question of the week: a function to reverse and alphabetize a list of strings

## reindeer_games.py

```Python

"""
12.04.2024
Santa is conducting his daily roll call for the reindeer, but the printer has mistakenly printed all their names backwards. To take attendance properly, he urgently needs a tool to reverse the reindeer names and put them in alphabetical order! Can you help Santa?"""

def sort_reindeer_names(arr):
    sorted_list = sorted(arr, key=lambda word: word[-1])
    for i in range(len(sorted_list)):
        sorted_list[i] = ''.join(reversed(sorted_list[i]))
    return sorted_list


assert sort_reindeer_names(["yzneT","ydissaC","enimA"]) == ["Amine","Cassidy","Tenzy"]
assert sort_reindeer_names(["rennuD","nexiV","recnarP","temoC","neztilB","recnaD","diduC","rehsaD","hploduR"]) == ["Blitzen","Comet","Cupid","Dancer","Dasher","Donner","Prancer","Rudolph","Vixen"]
assert sort_reindeer_names(["A","B","C"]) == ["A","B","C"]
```