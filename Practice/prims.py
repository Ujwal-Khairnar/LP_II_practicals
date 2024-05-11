import heapq

class Graph:
    def __init__(self,nv):
        self.nv=nv
        self.adjList=[[] for _ in range(nv)]

    def addEdge(self,src,des,weight):
        self.adjList[src].append((des,weight))
        self.adjList[des].append((src,weight))

    def Prims_algo(self,start):
        parent=[-1]* self.nv
        key=[float('inf')]* self.nv
        mstSet=[False]* self.nv

        pq=[(0,start)]

        key[start]=0

        while pq:
            dist,u=heapq.heappop(pq)

            mstSet[u]=True

            for v,weight in self.adjList[u]:
                if not mstSet[v] and weight < key[v]:
                    parent[v]=u
                    key[v]=weight
                    heapq.heappush(pq,(key[v],v))

            for i in range(1,self.nv):
                print(parent[i],"-",i,":",key[i])

            totalWeight=sum(key[1:])
            print("Total weight of MST:",totalWeight)

if __name__=="__main__":
    g=Graph(5)
    g.addEdge(0,1,2)
    g.addEdge(0,3,6)
    g.addEdge(1,2,3)
    g.addEdge(1,3,8)
    g.addEdge(1,4,5)
    g.addEdge(2,4,7)
    g.addEdge(3,4,9)

    g.Prims_algo(0)