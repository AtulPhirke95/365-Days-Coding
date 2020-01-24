def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    if root == None:
        return
    print(root.data,end=" ")
    if root.left == None and root.right != None:
        root=root.right
        print(root.data,end=" ")
    LeftView(root.left)
