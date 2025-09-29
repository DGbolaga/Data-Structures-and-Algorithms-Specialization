# python3

import sys
import threading


def compute_height(n, parents):
    mp = {}
    for i, v in enumerate(parents):
        if v not in mp:
            mp[v] = [i]
        else:
            mp[v].append(i)

    root = mp[-1][0]
    height = 0
    if root in mp:
        height +=1
        bfs = mp[root]
        while bfs:
            new_bfs = []
            for child in bfs:
                if child in mp:
                    new_bfs += mp[child] # append all the values of child's children to new level
            
            bfs = new_bfs
            height += 1
    
    return height
    


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
