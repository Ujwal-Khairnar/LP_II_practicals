from collections import defaultdict

#Graph
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    #bfs traversal
    def bfs(self,s):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(s)
        level=0
        while queue:
            level_size=len(queue)
            print("---------------")
            print("Level:",level)
            for i in range(level_size):
                s=queue.pop(0)
                if not visited[s]:
                    print("Node:",s)
                    visited[s]=True
                    for i in self.graph[s]:
                        if not visited[i]:
                            queue.append(i)
            level+=1
    #dfs_util
    def dfs_util(self,v,visited,level,dfs_traversal):
        visited[v]=True
        dfs_traversal.append(v)
        print("Level:",level,"Node:",v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i,visited,level+1,dfs_traversal)
                
    #dfs traversal
    def dfs(self,v):
        visited=[False]*len(self.graph)
        dfs_traversal=[]
        self.dfs_util(v,visited,0,dfs_traversal)
        print("DFS Traversal:",dfs_traversal)
#Manual input of edges
g=Graph()
num_edges=int(input("Enter the number of edges: "))
print("Enter the edges(u,v): ")
for _ in range(num_edges):
    u,v=map(int,input().split())
    g.add_edge(u,v)

#Printing the Graph
print("\n The graph:")
for node in g.graph:
    print(node,"->",g.graph[node])

#Breadth First Search
print("\nBreadth First Search:")
start_node_bfs=int(input("Enter the starting node for BFS traversal: "))
g.bfs(start_node_bfs)


#Depth First Search
print("\nDepth First Search: ")
start_node_dfs=int(input("Enter the starting node for DFS traversal: "))
g.dfs(start_node_dfs)

