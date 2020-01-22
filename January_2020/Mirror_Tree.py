#User function Template for python3
"""
  Problem : Given a Binary Tree, convert it into its mirror.
  Input: 2
         2
         1 2 R 1 3 L
         4
         10 20 L 10 30 R 20 40 L 20 60 R
  output: 2 1 3
          30 10 60 20 40

"""
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

def mirror(root):
    # Code here
    if root == None:
        return
    else:
        templ = root.left
        tempr = root.right
        root.left, root.right = tempr, templ
    mirror(root.left)
    mirror(root.right)
    return root
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None

def inorderTraversalUtil(root):
    # Code here
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)

def inorderTraversal(root):
    # Code here
    inorderTraversalUtil(root)
    print()

if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        
        root = None
        dictTree = dict()
        
        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(int(arr[3*j]))
                parent = dictTree[arr[3*j]]
                
                if j is 0:
                    root = parent
            else:
                parent = dictTree[arr[3*j]]
            
            child = Node(int(arr[3*j+1]))
                
            if(arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child
                
        mirror(root)
        
        inorderTraversal(root)
# } Driver Code Ends
