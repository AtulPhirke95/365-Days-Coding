"""Longest common prefix in Array"""
"""
    Input: aab aa a
    Output: a
"""
#Method 1: Using re.match module (Spzce efficient)
import re    
T = int(input())
while(T>0):
    n = int(input())
    lis = input().split()
    lis.sort(reverse = True,key=len)
    compare_to = lis[0]
    del lis[0]
    pattern = ""
    prev=""
    flag_a=False
    result = ""
    for _ in compare_to:
        prev += _
        pattern = r"{}".format(prev)
        count=0
        for item in lis:
            if re.match(pattern,item):
                count+=1
            else:
                flag_a=True
                break
        if count==len(lis):
            result = prev
        if flag_a:
            break
    if result=="":
        print("-1")
    else:
        print(result)
    T-=1

#Method 2: Using dp approach
def fuct(one,two):
    if len(one) >= len(two):
        m = len(one)
        n = len(two)
    else:
        n = len(one)
        m = len(two)
    flag = True
    flag_a=False
    result = ""
    for i in range(n):
        if one[i] == two[i]:
            result += one[i]
        else:
            flag = False
            break
    return result
    
T = int(input())
while(T>0):
    n = int(input())
    lis = input().split()
    lis.sort(reverse=True)
    count = 0
    s = ""
    result = lis[0]
    flag=False
    while(count<len(lis)-1):
        if result == "":
            flag= True
            break
        result = fuct(result,lis[count+1])
        count+=1
    if flag:
        print("-1")
    else:
        print(result)
    T-=1
