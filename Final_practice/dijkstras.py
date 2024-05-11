import heapq

class Graph:
    def __init__(self,nv):
        self.nvert=nv
        self.adjList=[[] for _ in range(nv)]

    def addEdge(self,src,des,weight):
        self.adjList[src].append((des,weight))
        self.adjList[des].append((src,weight))

    def dijkstras(self,start):
        pq=[(0,start)]
        dist=[float('inf')] * self.nvert
        dist[start]=0

        while pq:
            distance,u=heapq.heappop(pq)

            for v,weight in self.adjList[u]:
                if dist[v]>dist[u]+weight:
                    dist[v]=dist[u]+weight
                    heapq.heappush(pq,(dist[v],v))

        for i in range(self.nvert):
            print(f"Shortest path from {start} to {i} is {dist[i]}")






if __name__=="__main__":
    nv=int(input("Enter the number of vertices:"))
    g=Graph(nv)

    ne=int(input("Enter the number of edges: "))
    print("Enter the source ,destination, weight:")
    for _ in range(ne):
        src,des,weight=map(int,input().split())
        g.addEdge(src,des,weight)


    start_src=int(input("Enter the starting source:"))
    g.dijkstras(start_src)
