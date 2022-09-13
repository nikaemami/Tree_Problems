# Tree_Problems
Implementation of different projects with different tree algorithms, like the **binary search tree**, and the **red-black tree**.

<h2>The Cantankerous Tree:</h2>

On a tree with numbers on the edges, the aim is to set **all the edges** between two chosen leaves to **zero** by **adding a constant** to the values.

In each step we choose two leaves, and add a constant value to all the edges between these two vertices. The ultimate goal is to have values of all the edges equal to zero. We want to know if achieving this goal is **possible** with the given tree, or not.

INPUT: n is given in the first line, which is the **number of vertices** in the tree. In the next n-1 lines, two numbers u,v are given, which indicates that an **edge** exists between these two vertices.

OUTPUT: print **"YES"** if winning this game is possible. Otherwise print **"NO"**.

**INPUT:**

3

1 2

2 3
  
**OUTPUT:**

NO

The key part of the code, is updating the values on the edges as follows:

```ruby
for  i in range(len(nodes)):
    if (nodes[i] in node_dict):
        node_dict[nodes[i]]+=1
    else:
        node_dict[nodes[i]]=1
```

<h2>Super Powers:</h2>

People with super powers are registered in a league. The goal is to find out **the number of people each individual is stronger than**.

The league is empty in the beginning. We have q commands, each of them indicates: First, whether a person with power x is **registered**. Second, if a person's power is s, how many people are **weaker** than him.

INPUT: In the first line q is given, which is the **number of commands**. The commands are given in the next q lines.

OUTPUT: For each command, print the number of people that the individual is stronger than.

**INPUT:**

5

2 5

1 3

1 7

2 4

2 1

**OUTPUT:**

0

1

0
 
First, a class **Node** is defined to store the value, and the children of each node in a **tree**:

```ruby
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data
        self.left_count = 0
```

Next, two functions are defined: insert, for **registering** people, and Count_less for computing the output:

```ruby
def insert(root, new)
def Count_less(root, x)
```
