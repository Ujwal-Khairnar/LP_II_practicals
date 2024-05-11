import heapq

class Graph:
    def __init__(self,nv):
        self.nv=nv
        self.adjList=[[] for _ in range(nv)]

    def addEdge(self,src,des,weight):
        self.adjList[src].append((des,weight))
        self.adjList[des].append((src,weight))
        
    def dijkstras(self,src):
        pq=[(0,src)]
        dist=[float('inf')] * self.nv
        dist[src]=0

        while pq:
            dis,u=heapq.heappop(pq)

            for v,weight in self.adjList[u]:
                if dist[v]>dist[u]+weight:
                    dist[v]=dist[u]+weight
                    heapq.heappush(pq,(dist[v],v))

        for i in range(self.nv):
            print(f"Shortest path from {src} to {i} is {dist[i]}")

if __name__=="__main__":
    nv=int(input("Enter the number of vertices: "))
    g=Graph(nv)

    ne=int(input("Enter the number of edges: "))
    print("Enter edges in the format 'source destination weight':")
    for _ in range(ne):
        src,des,weight = map(int,input().split())
        g.addEdge(src,des,weight)

    src_vertex=int(input("Enter the source vertex: "))
    g.dijkstras(src_vertex)