import heapq

class Graph:
    def __init__(self, nv):
        self.nv = nv
        self.adjList = [[] for _ in range(nv)]

    def addEdge(self, src, des, weight):
        self.adjList[src].append((des, weight))
        self.adjList[des].append((src, weight))  # For undirected graph

    def primsMST(self, start):
        parent = [-1] * self.nv       # To store the parent of each vertex
        key = [float('inf')] * self.nv  # To store the weight of each vertex
        mstSet = [False] * self.nv    # To store the vertices that are already included in MST

        pq = [(0, start)]  # Min heap to store the vertices

        key[start] = 0       # Start with the first vertex

        while pq:
            weight, u = heapq.heappop(pq)
            
            mstSet[u] = True

            for v, w in self.adjList[u]:
                if not mstSet[v] and w < key[v]:
                    parent[v] = u
                    key[v] = w
                    heapq.heappush(pq, (key[v], v))

        for i in range(1, self.nv):
            print(parent[i], "-", i, ":", key[i])

        # total weight of MST
        totalWeight = sum(key[1:])
        print("Total weight of MST:", totalWeight)

if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 3, 6)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 8)
    g.addEdge(1, 4, 5)
    g.addEdge(2, 4, 7)
    g.addEdge(3, 4, 9)

    g.primsMST(0)

# Enter the number of vertices: 5
# Enter the number of edges: 7
# Enter edges in the format 'source destination weight': 
# 0 1 2
# 0 3 6
# 1 3 8
# 1 2 3
# 1 4 5
# 4 2 7
# 4 3 9
# Enter the source vertex: 0
# 0 - 1  : 2
# 1 - 2  : 3
# 0 - 3  : 6
# 1 - 4  : 5
# Totalweight: 16
# PS C:\Users\UJWAL\Desktop\LP II practical> 