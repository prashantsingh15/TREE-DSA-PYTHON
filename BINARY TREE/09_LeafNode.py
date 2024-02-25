class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


def printTree(root):
    if root==None:
        return 

    print(root.data,end=" ")
    print(root.left)
    print(root.right)

def printTreeDetailed(root):
    if root ==None:
        return 

    print(root.data,end=":")
    if root.left !=None:
        print("L",root.left.data,end=",")
    if root.right !=None:

        print("R",root.right.data,end="")

    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

# I/O Input FUNCTION GOES THERE

def treeInput():
    rootData=int(input())
    if rootData ==-1:
        return None

    root =BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root


# BASE GOES THERE FOR FINDING THE LEAF NODE IN A BINARY TREEEE

def numleafNode(root):
    if root ==None:
        return 0

    if root.left==None and root.right==None:
        return 1

    numLeafLeft=numleafNode(root.left)
    numLeafRight=numleafNode(root.right)
    return numLeafLeft + numLeafRight



root=treeInput()
printTreeDetailed(root)
print(numleafNode(root))
