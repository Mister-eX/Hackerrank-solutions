from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(deque)

    def create_graph(self, edges):
        for src, dest in edges:
            self.graph[src].append(dest)
            self.graph[dest].append(src)


def bfs(n, m, edges, s): # n-> no of nodes; m-> no of edges ; s-> starting point
    G = Graph() ; G.create_graph(edges)

    Q = deque() ; Q.append(s)

    res = [-1]*(n + 1); res[s] = 0
    while Q:
        x = Q.popleft()
        for i in G.graph[x]:
            if res[i] == -1:
                res[i] = res[x] + 6
                Q.append(i)

    del(res[s]) ; del(res[0])
    return res