"""
  Given a list of non negative integers, arrange them in such a manner that 
  they form the largest number possible.The result is going to be very large, 
  hence return the result in the form of a string.
  
  Input: 3 30 34 5 9
  Output: 9534330
  
  Explaination: Suppose a = [20,10,3]. The possible pairs are [(20,10)(10,3)(20,3)]
  1st pair: 20 , 10 -> return True as 2010 > 1020. So do not swap. (20,10,3)
  2nd pair: 10 , 3 -> return False as 103 < 310. So swap.(20,3,10)
  3rd pair: 20 , 3 return False as 203 < 320, so swap.(3,20,10)
  So the array would be [3,20,10]
"""

import functools
def large(a, b):
    if a + b < b + a:
        return 1 # sort it
    else:
        return -1 # do not sort it

t = int(input())
while t > 0:
    t -=1
    n = int(input())
    ar = [each for each in input().split()]
    ar.sort(key = functools.cmp_to_key(large))
    print (''.join(ar))
