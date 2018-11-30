# longest non repeating substring
# leetcode

s = "abcdbbba"

my_dict = {}
i = j = 0
substr = ""
max_substr = ""
n = len(s)
while(i<n and j < n):
    val = s[j]
    if not my_dict.get(val):
        my_dict[val] = 1
        j += 1
        substr += val
        if len(substr) > len(max_substr):
            max_substr = substr
    else:
        my_dict.pop(s[i])
        i += 1
        substr = substr[1:]

print max_substr