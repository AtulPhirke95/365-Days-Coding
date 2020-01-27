"""
  Suppose you have given an array. You have to print the sum of all the elemets except the current index.
  Input: [1,2,3,4]
  Output: 9 8 7 6
"""

arr = [1,2,3,4,5]

sum_ = sum(arr)

for item in arr:
    print(sum_ - item, end = ' ')
