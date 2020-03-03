"""
n=7
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print("")
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * *
"""

"""------------------------------------------------------------------------------------
n=7
c=n
for i in range(1,n+1):
    for j in range(c):
        print("* ",end=" ")
    c=c-1
    print("")
        
*  *  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*

"""

"""-------------------------------------------------------------------------------------
n = 7
c=n
for i in range(1,n+1):
    for j in range(c-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print("")
    c-=1

      *
     **
    ***
   ****
  *****
 ******
*******
"""

"""____________________________________________________________________________________
n=7
c=n
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(c):
        print("*",end="")
    print("")
    c-=1
    
*******
 ******
  *****
   ****
    ***
     **
      *
"""

"""_____________________________________________________________________________________
n=7
c=n
s=0
for i in range(1,n+1):
    for j in range(c-1):
        print(" ",end="")
    c-=1
    for k in range(i+s):
        print("*",end="")
    s+=1
    print("")

      *
     ***
    *****
   *******
  *********
 ***********
*************

"""

"""--------------------------------------------------------------------------------------
n=7
c=n

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(c*2-1):
        print("*",end="")
    c-=1
    print("")

*************
 ***********
  *********
   *******
    *****
     ***
      *
"""

"""______________________________________________________________________________________
n=5
c=n
s=0
for i in range(1,n+1):
    for j in range(c*2-2):
        print(" ",end="")
    c-=1
    for k in range(i+s):
        print("* ",end="")
    s+=1
    print("")
for b in range(n):
    for o in range(n*2-2):
        print(" ",end="")
    print("||")

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
        ||
        ||
        ||
        ||
        ||

   *
  /|\
 /_|_\
  /|\
 / | \
/__|__\
   |
"""
n=3
c=n
l=0
p=0
e=n
while p < n:
    c=n
    for i in range(1,e+1):
        for j in range(c):
            print(" ",end="")
        if i==1 and p==0:
            print("*",end="")
        else:
            print("/",end="")
            if 2<i<e:
                for k in range(i-2):
                    print(" ",end="")
            elif i!=2 and i==e:
                for k in range(i-2):
                    print("_",end="") 
            print("|",end="")
            if 2<i<e:
                for k in range(i-2):
                    print(" ",end="")
            elif i!=2 and i==n:
                for k in range(i-2):
                    print("_",end="") 
            print("\\",end="")
        print("")
        c-=1
    e+=1
    p+=1

n=5
c=n
s=0
x=2
flag=False
flag_=False
while True:
    c=n
    s=0
    for i in range(1,x+1):
        for j in range(c*2-2):
            print(" ",end="")
        c-=1
        for k in range(i+s):
            if k!=n:
                print("* ",end="")
            else:
                flag=True
                break
        if flag:
            flag_=True
            break
        
        s+=1
        print("")
        x=x+1
    if flag_:
        break
    

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(abs(gcd(-24,-18)))


n=856
j=0
for i in reversed(range(11,n)):
    if str(i)==str(i)[::-1]:
        print(i)
        j=i
        break
k=0
for i in range(n,n*2):
    if str(i) == str(i)[::-1]:
        print(i)
        k=i
        break
print(k if k-n < n-j else j)

from itertools import count
for i in count(n):
    if str(i)==str(i)[::-1]:
        print(i)
        break

from collections import Counter
a = [1,2,2,3,4,5,5,6,4,5,7,0]
##l=[0]*10
##for i in a:
##    l[ord(str(i))-48]+=1
##
##for i in range(len(l)):
##    if l[ord(str(i))-48] == 1:
##        print(i)
##c=Counter(a)
##for k,v in c.items():
##    if v==1:
##        print(k)
d={}
for i in a:
    if i not in d:
        d.setdefault(i,0)
    d[i]+=1

for k,v in d.items():
    if v==1:
        print(k)
    

arr1 = [11, 1, 13, 21, 3, 7] 
arr2 = [11, 3, 7, 10]
flag=False
for i in arr2:
    if i in arr1:
        continue
    else:
        flag=True
print("No" if flag==True else "Yes")

l = ["aabsxdc", "aabcd","aabbdcgdtu", "bcdtgjf"]
l.sort()
temp = min(len(l[0]),len(l[-1]))
i=0
c=0
while(i<temp):
    if l[0][i]==l[-1][i]:
        c+=1
    i+=1
print(l[0][:c])

arr = [ 5, 8, 1, 4, 2, 9, 3, 7, 6 ]
arr.sort() #[1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(arr)
for i in range(len(arr)):
    if arr[size-1] == arr[i]:
        break
    print(arr[size-1],arr[i])
    size=size-1


d = {1:{"month":"January","days":31},2:{"month":"February","days":28},3:{"month":"March","days":31},4:{"month":"April","days":30},
     5:{"month":"May","days":31},6:{"month":"June","days":30},7:{"month":"Jully","days":31},8:{"month":"August","days":31},
     9:{"month":"September","days":30},10:{"month":"October","days":31},11:{"month":"November","days":30},12:{"month":"December","days":31}}

choice = int(input())
for i in range(1,choice+1):
    print(d[i]["month"],d[i]["days"])

for j in range(1,d[choice]["days"]+1):
    if j%7!=0:
        print(j,end="      ")
    else:
        print(j)


"""1223334444333221"""
n = 4
count=n-1
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
for i in range(1,n):
    for j in range(count):
        print(count,end="")
    count-=1

n=4
c=2*n-1
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    print("*",end="")

    for k in range(c-2):
        print(" ",end="")
    
    if c>1:
        print("*")
    c-=2

"""
 *     *
  *   *
   * *
    *
"""

n=6
c=6
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(c-1):
        print(chr(k+65),end=" ")
    print("")
    c-=1

"""
 A B C D E 
  A B C D 
   A B C 
    A B 
     A
##"""
