
import os
import sys
from queue import Queue
sys.setrecursionlimit(1027)

class Node:
    def __init__(self, data, level):
        self.data= data
        self.level= level
        self.left= None
        self.right= None

def create_tree(indexes):
    Q= Queue()
    root= Node(1, 1)
    Q.put(root)
    for left_child, right_child in indexes:
        ptr= Q.get()
        if left_child!=-1:
            ptr.left= Node(left_child, ptr.level+1)
            Q.put(ptr.left)
        
        if right_child!=-1:
            ptr.right= Node(right_child, ptr.level+1)
            Q.put(ptr.right)
    return root


def in_order(root, result):
    if root is None:
        return 
    in_order(root.left, result)
    result.append(root.data)
    in_order(root.right, result)


def swap_nodes(root, level, k):
    if (root is None) or (not root.left and not root.right):
        return
    if level%k==0:
        root.left, root.right= root.right, root.left
    
    swap_nodes(root.left, level+1, k)
    swap_nodes(root.right, level+1, k)


def swapNodes(indexes, queries):
    root= create_tree(indexes)
    result=[]
    for i in queries:
        R=[]
        swap_nodes(root, 1, i)
        in_order(root, R)
        result.append(R)
    return result



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
