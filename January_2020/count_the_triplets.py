"""
  Statement: Given an array of distinct integers. 
  The task is to count all the triplets such that sum of two elements equals the third element.
  Input: 1 5 3 2
  Output: 2
  Input: 3 2 7
  Output: -1
  
  Solution: one approach to solve this problem is by taking the combinations and then find whether the addition of two minus third equals to 0.
  Other way is to use hashing solution where we are 
        1) storing the array in the set
        2) sort the array in ascending order
        3) save the last element of sorted array in variable as max
        4) then iterate the sorted array and check if the addition of two is there in set. 
              If it is then increament the count.If addition of two is greater than max then break the loop.
"""

from itertools import combinations as cb
T = int(input())
while(T>0):
    """
    n=int(input())
    s = list(map(int,input().split()))
    count_of_tuples = 0
    flag = False
    for tup in cb(s,3):
        a,b,c=tup
        if (a+b)-c == 0 or (b+c)-a == 0 or (a+c) - b == 0:
            count_of_tuples += 1
            flag = True
    if flag:
        print(count_of_tuples)
    else:
        print(-1)
    """
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    set_a = set(arr)
    max_a = arr[-1]
    c = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            s = arr[i]+arr[j]
            if(s>max_a):
                break
            elif(s in set_a):
                c+=1
    print(c if c>0 else -1)
    T-=1
