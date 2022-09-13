class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data
        self.left_count = 0

def insert(root, new):
    if root is None:
        return Node(new)
    else:
        if (root.value == new):
            return root
        elif (root.value < new):
            root.right = insert(root.right, new)
        else:
            root.left = insert(root.left, new)
            root.left_count+=1
    return root

def Count_less(root, x):
    if root == None:
        return 0
    if root.value == x:
        return (root.left_count) 
    if root.value < x:
        return (root.left_count + 1 + Count_less(root.right,x))
    else:
        return Count_less(root.left, x)

n = int(input())
root = None
for i in range (n):
    myinput = list(map(int,input().split()))
    if (myinput[0] == 1):
        root = insert(root,myinput[1])
    else:
        print(Count_less(root,myinput[1]))
