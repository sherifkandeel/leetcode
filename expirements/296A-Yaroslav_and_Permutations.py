# from collections import Counter
# n = input()
# arr = map(int, raw_input().split(' '))
# arrd = dict(Counter(arr)) #creates a dict of item in arr and value the recurrence of it 
# largestV = 0
# for k, v in arrd.items():
#     if v > largestV:
#         largestV = v

# if largestV + largestV-1 <= len(arr):
#     print "YES"
# else:
#     print "NO"

import hashlib
print hashlib.md5("something").hexdigest()
