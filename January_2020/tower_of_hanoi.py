"""
  Input: Nunber of disks -> 3
  Output: Move disk 1 from source to destination
          Move disk 2 from source to support
          Move disk 1 from destination to support
          Move disk 3 from source to destination
          Move disk 1 from support to source
          Move disk 2 from support to destination
          Move disk 1 from source to destination
          Number of moves required are : 7
"""

def tower_of_hanoi(source,destination,support,n):
    if n == 0:
        return
    tower_of_hanoi(source,support,destination,n-1)
    print("Move disk {} from {} to {}".format(n,source,destination))
    tower_of_hanoi(support,destination,source,n-1)

number_of_disks = 3   
source = 'source'
destination = 'destination'
support = 'support'
tower_of_hanoi(source,destination,support,number_of_disks)
moves = 2 ** (number_of_disks) - 1
print("Number of moves required are : {}".format(moves))
