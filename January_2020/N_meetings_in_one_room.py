"""
  Problem Statement : There is one meeting room in a firm. 
                      There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i 
                      and F[i] is finish time of meeting i.
                      What is the maximum number of meetings that can be accommodated in the meeting room?
  Input : s[] = {1, 3, 0, 5, 8, 5}, f[] = {2, 4, 6, 7, 9, 9}
  Output : 1 2 4 5
           First meeting [1, 2] -> index of (1,2) is 1
           Second meeting [3, 4] -> index of (3,4) is 2
           Fourth meeting [5, 7] -> index of (5,7) is 4
           Fifth meeting [8, 9] -> index of (8,9) is 5
"""

lis1=[1,3,0,5,8,5]
lis2=[2,4,6,7,9,9]

d_new = sorted(zip(lis1,lis2),key=lambda x:(x[1]))  # sorting list of tuples by second value
#d_new = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]

lis_1 = [i[0] for i in d_new] #[1, 3, 0, 5, 8, 5]
lis_2 = [i[1] for i in d_new] #[2, 4, 6, 7, 9, 9]

finish = lis_2[0]
print(lis1.index(lis_1[0]) + 1,end=" ")

for i in range(1,len(d_new)):
    if lis_1[i] > finish:
        print(lis1.index(lis_1[i]) + 1,end=" ")
        finish = lis_2[i]
