"""
  Problem Statement: Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
                     1. The amount of petrol that every petrol pump has.
                     2. Distance from that petrol pump to the next petrol pump.

                    Your task is to complete the function tour() which returns an integer denoting the first point from 
                    where a truck will be able to complete the circle (The truck will stop at each petrol pump 
                    and it has infinite capacity).
  Input: 1
         4
         4 6 6 5 7 3 4 5
  Output:
         1 
  Explaination: if we start from (6,5) then we left with 1 petrol as 6-5 is 1
                At (7,3) we get 1+(7-3) = 6
                At (4,5) we get 6+(4-5) = 5
                At (4,6) we get 5+(4-6) = 3
                Now with 3 liters petrol left you can go to next pertol pump (6,5) which is nothing but our end point.
                So, At last we have to check if our total sum is greater than 0 or not?
"""

def tour(lis, n):
    c = 0
    diff = 0
    start = 0
    for i in range(len(lis)):
        c += lis[i][0]-lis[i][1]
        
        if c < 0:
            start = i+1
            diff += c
            c=0
    return start if (c+diff > 0) else -1
    
lis = [[4,6],[6,5],[7,3],[4,5]]  #here lis=[[petrol,distance],[petrol,distance],]
n = 4
print(tour(lis,n))
