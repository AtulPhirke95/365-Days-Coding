"""
Input:
2
22
100

Output:
6
20

"""

#User function Template for python3

def number0f2s(n):
    
    #add Code here
    c=0
    s = str(n)
    for _ in s:
        if _ == '2':
            c+=1
    return c
    
def numberOf2sinRange(n):
    #add code here
    count=0
    for i in range(n+1):
        count+=number0f2s(i)
    return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
# } Driver Code Ends
