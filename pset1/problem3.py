# Problem 3
# 1 point possible (ungraded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc


s = 'ebtsnwdrmmowdljbotctsj'
checkLongestSubstring = s[0]
previousSubstring = ''
count = 0
for i in range(len(s)):
    if s[i] >= checkLongestSubstring[-1] and i != 0:
        checkLongestSubstring += s[i]
    else:
        if len(checkLongestSubstring) > len(previousSubstring):
             previousSubstring = checkLongestSubstring
        checkLongestSubstring = s[i]
    
