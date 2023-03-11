class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root) :
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node

#Given a non_empty binary search tree ,return the node with minimum
#key value found in that tree.Note that the entire tree does not need
#to be searche
def minvaluenode(node):
    current=node
    
    #loop down to find the leftmost leaf
    while (current.left is not None):
        current=current.left
    return current

#given a binary search tree and a key,this function delete the key and 
#returns the new root
def deletenode(root,key):
    
    #Base code
    if root is None:
        return root
    
    #key < root,it lies in left subtree
    if key<root.key:
        root.left=deletenode(root.left,key)
    elif(key>root.key):
        root.right=deletenode(root.right,key)

    #if key is same as root's key,then this is the node to be deleted
    else:

         #node with only ONE child or NO child
         if root.left is None:
             temp=root.right
             root=None
             return temp
         elif root.right is None:
            temp=root.left
            root=None
            return temp

        #node with TWO children:
        #get the inorder successor(smallest in the right subtree)
         temp=minvaluenode(root.right)

        #copy the inorder successsor's content to this node
         root.key=temp.key

        #delete the inorder succcessor
         root.right=deletenode(root.right,temp.key)
    return root

root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("inorder traversal of the given tree")
inorder(root)
print("\ndelete 20")
root=deletenode(root,20)
print("inorder traversal of the modified tree")
inorder(root)
print("\ndelete 30")
root=deletenode(root,30)
print("inorder traversal of the modified tree")
inorder(root)
print("\ndelete 50")
root=deletenode(root,50)
print("inorder traversal of the modified tree")
inorder(root)












