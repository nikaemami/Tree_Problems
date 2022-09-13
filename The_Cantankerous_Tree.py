n = int(input())
nodes = []
for i in range(n-1):
    myinput = list(map(int,input().split()))
    nodes.append(myinput[0])
    nodes.append(myinput[1])

node_dict = {}
for  i in range(len(nodes)):
    if (nodes[i] in node_dict):
        node_dict[nodes[i]]+=1
    else:
        node_dict[nodes[i]]=1

condition = 0
for i in node_dict:
    if(node_dict[i]==2):
        print("NO")
        condition = 1 
        break
if (condition == 0):
    print("YES")