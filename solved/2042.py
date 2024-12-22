from sys import stdin  

N,M,K = map(int,stdin.readline().strip().split())
A = []
for _ in range(N):
    A.append(int(stdin.readline().strip()))

tree = [0]*(4*N)

def create_tree(A,tree,node,start,end):
    if start == end:
        tree[node] = A[start]
    else:
        create_tree(A,tree,node*2,start,(start+end)//2)
        create_tree(A,tree,node*2+1,(start+end)//2+1,end)
        tree[node] = tree[node*2] + tree[node*2+1]

create_tree(A,tree,1,0,N-1)

def update_tree(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        update_tree(tree, node*2, start, (start+end)//2, index, diff)
        update_tree(tree, node*2+1, (start+end)//2+1, end, index, diff)

def update(a, tree, n, index, val):
    diff = val - a[index]
    a[index] = val
    update_tree(tree, 1, 0, n-1, index, diff)

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

ans = []
for _ in range(M+K):
    a,b,c = map(int,stdin.readline().strip().split())
    if a == 1:
        update(A,tree,N,b-1,c)
    else:
        ans.append(query(tree,1,0,N-1,b-1,c-1))

print(*ans,sep='\n')
