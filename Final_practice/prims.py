import heapq

class Graph:
    def __init__(self,nv):
        self.nv=nv
        self.adjList=[[] for _ in range(nv)]

    def addEdge(self,src,des,weight):
        self.adjList[src].append((des,weight))
        self.adjList[des].append((src,weight))

    def Prims_Mst(self,start):
        parent=[-1]*self.nv
        key=[float('inf')] * self.nv
        mstSet=[False]*self.nv

        pq=[(0,start)]
        key[start]=0

        while pq:
            weight,u=heapq.heappop(pq)
            mstSet[u]=True

            for v,weight in self.adjList[u]:
                if not mstSet[v] and weight<key[v]:
                    parent[v]=u
                    key[v]=weight
                    heapq.heappush(pq,(key[v],v))

        for i in range(1,self.nv):
            print(parent[i],"-",i,":",key[i])

        totalweight=sum(key[1:])
        print("Total sum of MST is: ",totalweight)



if __name__=="__main__":
    nv=int(input("Enter the number of vertices:"))
    g=Graph(nv)

    ne=int(input("Enter the number of edges: "))
    print("Enter Source,Destination,weight of each edge:")
    for _ in range(ne):
        src,des,weight=map(int,(input().split()))
        g.addEdge(src,des,weight)

    
    start_vertex=int(input("Enter the starting vertex:"))
    g.Prims_Mst(start_vertex)

    # g = Graph(5)
    # g.addEdge(0, 1, 2)
    # g.addEdge(0, 3, 6)
    # g.addEdge(1, 2, 3)
    # g.addEdge(1, 3, 8)
    # g.addEdge(1, 4, 5)
    # g.addEdge(2, 4, 7)
    # g.addEdge(3, 4, 9)