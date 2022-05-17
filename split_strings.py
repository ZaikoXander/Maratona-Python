"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
"""

def solution(s):
    
    split_strings = []
    
    for i in range(0, len(s), 2):
        if i == len(s) - 1:
            split_strings.append(s[i : i + 2] + "_")
            break
        split_strings.append(s[i : i + 2])
    
    return split_strings

print(solution("abcdef"))
