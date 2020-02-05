"""
  Problem statement: Given two sorted arrays, arr1 and arr2 where length of arr1 is appended by 0 with number of times the length of arr2,
                     your job is to apply sorting on the combine array into arr1 with O(n).
  Input: arr1[10,20,30]
         arr2[9,11,14]
  Output: arr1[9,10,11,14,20,30]
  Explanination: 1) First append 3 0's to arr1 as 3 is the length of arr2.
                 2) Assign i to len(arr1)-len(arr2)-1 and j to len(arr2)-1 and count to len(arr1)-1
                 3) Start comapring last element of both arrays and append the greater number to last position of arr1.
                 4) Decrease the size of count and also decrease the size of i or j depending upon the comparision.
                 5) Insert remaining elements of arr2 to arr1.
"""

def sorting(arr1,arr2):
    """
        Compare last non zero element of arr1 with last element of arr2 and append largest element to the end of arr2.
    """
    i=len(arr1)-len(arr2)-1
    j=len(arr2)-1
    count=len(arr1)-1
    
    while(i>=0 and j>=0):
        if arr1[i] > arr2[j]:
           arr1[count]=arr1[i]
           i-=1
           
        elif arr1[i] < arr2[j]:
            arr1[count]=arr2[j]
            j-=1
        elif arr1[i] == arr2[j]:
            arr1[count]=arr1[i]
            i-=1
        count-=1

    #Remaining elements from arr2 should go to arr1
    i_=j
    if j!=-1:
        while j>=0:
            arr1[i_]=arr2[j]
            i_-=1
            j-=1
    return arr1


arr1=[10,14,30,99]
arr2=[9,10,14,55,99,101,202]
for i in range(len(arr2)):
    arr1.append(0)
print(sorting(arr1,arr2))
