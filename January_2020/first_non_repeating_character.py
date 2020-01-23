"""
  Input: 3
         5  
         hello
         12
         zxvczbtxyzvy
         6
         xxyyzz
"""
#code
T = int(input())
while(T>0):
    n = int(input())
    s=input()
    flag = False
    lis=[0] * 26
    for _ in s:
        lis[ord(_)-97] +=1
    for _ in s:
        if lis[ord(_)-97] == 1:
            print(_)
            flag = True
            break
    if flag != True:
        print(-1)
    T-=1
