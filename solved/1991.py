from sys import stdin 

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

N = int(stdin.readline().strip())

inp = []
for i in range(N):
    x,y,z = stdin.readline().strip().split()
    inp.append([x,y if y != '.' else None,z if z != '.' else None])

nodes = sum(inp,[])[::3]

for i in nodes:
    exec(f'{i}=TreeNode(i)')
    
for i,j,k in inp:
    exec(f'{i}.left = {j}')
    exec(f'{i}.right = {k}')

def recurPreorder(node):
    if node is None:
        return 
    print(node.val, end = '')
    recurPreorder(node.left)
    recurPreorder(node.right)

def recurInorder(node):
    if node is None:
        return 
    recurInorder(node.left)
    print(node.val, end = '')
    recurInorder(node.right)

def recurPostorder(node):
    if node is None:
        return 
    recurPostorder(node.left)
    recurPostorder(node.right)
    print(node.val, end = '')

eval('recurPreorder(A)')
print('')
eval('recurInorder(A)')
print('')
eval('recurPostorder(A)')
print('')
