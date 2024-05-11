import heapq

class Graph:
    def __init__(self, nv):
        self.nv = nv
        self.adjList = [[] for _ in range(nv)]

    def addEdge(self, src, des, weight):
        self.adjList[src].append((des, weight))
        self.adjList[des].append((src, weight))  # For undirected graph

    def prims(self,start):
        parent=[-1]*self.nv
        key=[float('inf')]*self.nv
        mstSet=[False]*self.nv

        pq=[(0,start)]
        key[start]=0
        
        while pq:
            dist,u=heapq.heappop(pq)
            mstSet[u]=True

            for v,w in self.adjList[u]:
                if not mstSet[v] and w < key[v]:
                    parent[v]=u
                    key[v]=w
                    heapq.heappush(pq,(key[v],v))

        for i in range(1,self.nv):
            print(parent[i],"-",i," :",key[i])

        totalweight=sum(key[1:])
        print("Totalweight:",totalweight)


if __name__=="__main__":
    nv = int(input("Enter the number of vertices: "))
    g = Graph(nv)

    ne = int(input("Enter the number of edges: "))
    print("Enter edges in the format 'source destination weight': ")
    for _ in range(ne):
        src, des, weight = map(int, input().split())
        g.addEdge(src, des, weight)

    src_vertex = int(input("Enter the source vertex: "))
    g.prims(src_vertex)