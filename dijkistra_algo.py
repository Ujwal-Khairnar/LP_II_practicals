import heapq

class Graph:
    def __init__(self, nv):
        self.nv = nv
        self.adjList = [[] for _ in range(nv)]

    def addEdge(self, src, des, weight):
        self.adjList[src].append((des, weight))
        self.adjList[des].append((src, weight))  # For undirected graph

    def dijkstras(self, src):
        pq = [(0, src)]
        dist = [float('inf')] * self.nv
        dist[src] = 0

        while pq:
            dis, u = heapq.heappop(pq)

            for v, weight in self.adjList[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        for i in range(self.nv):
            print(f"Shortest path from {src} to {i} is {dist[i]}")

if __name__ == "__main__":
    nv = int(input("Enter the number of vertices: "))
    g = Graph(nv)

    ne = int(input("Enter the number of edges: "))
    print("Enter edges in the format 'source destination weight': ")
    for _ in range(ne):
        src, des, weight = map(int, input().split())
        g.addEdge(src, des, weight)

    src_vertex = int(input("Enter the source vertex: "))
    g.dijkstras(src_vertex)

# Enter the number of vertices:5
# Enter the number of edges:7
# Enter the src,dest,weight
# 0 1 2
# 0 3 6
# 1 3 8
# 1 2 3
# 1 4 5
# 4 2 7
# 4 3 9
# Enter the starting position0
# Shortest pathat from 0 to 0 is: 0
# Shortest pathat from 0 to 1 is: 2
# Shortest pathat from 0 to 2 is: 5
# Shortest pathat from 0 to 3 is: 6
# Shortest pathat from 0 to 4 is: 7
