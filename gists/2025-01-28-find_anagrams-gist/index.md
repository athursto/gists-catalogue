# 2024-01-28-find_anagrams-gist

**Gist file**: [https://gist.github.com/athursto/63f6242d4de38a9cef2ab030583b27e6](https://gist.github.com/athursto/63f6242d4de38a9cef2ab030583b27e6)

**Description**: Cassidy's interview question of the week: a function to find indices of an anagram in a string, when given another string


```Python
def find_anagrams(string1, string2):
    # freq_dict = {}
    anagram_indices = []
    # sorted_substring = sorted(tuple(string2))
    # # print(sorted_substring)
    # for char in sorted_substring:
    #     if char not in freq_dict:
    #         freq_dict[char] = 1
    #     else:
    #         freq_dict[char] += 1
        # if string1[i] in freq_dict.keys():
        #     subsset = sorted(tuple(string1[i:i+len(string2)]))
        #     if subsset == sorted_substring:
        #         anagram_indices.append(i)
    # return anagram_indices
    """ First solution had a o* n log n runtime, so then I tried to do sliding windows"""
    from collections import Counter
    n, m = len(string1), len(string2)
    if m > n:
        return []
    string2_count = Counter(string2)
    sliding_window = Counter(string1[:m]) #First window
    print(sliding_window)
    for i in range(len(string1) - len(string2)+ 1):
        if i >0:
            sliding_window[string1[i-1]] -=1 #remove left character, if it's not the first character
            if sliding_window[string1[i-1]] == 0: #if there are no longer any of those character, delete them from counter
                del sliding_window[string1[i-1]]
            sliding_window[string1[i+m-1]] +=1 #keep sliding to the right



find_anagrams("fish", "cake")
print(find_anagrams("cbaebabacd", "abc"))
```