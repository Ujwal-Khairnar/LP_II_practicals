import heapq
N=3
#For movement positions
drow=[1,0,-1,0]
dcol=[0,-1,0,1]

class Node:
    def __init__(self,mat,x,y,g,parent=None):
        self.mat=[row[:] for row in mat]
        self.parent=parent
        self.g=g
        self.h=None
        self.x=x
        self.y=y

    def __lt__(self,other):
        return (self.g+self.h)<(other.g+other.h)
    
def print_matrix(mat,g,h):
    for row in mat:
        print(' '.join(map(str,row)))
    print("g:",g,"h:",h,"f:",g+h)
    print()

def heuristic(initial,final):
    count=0
    for i in range(N):
        for j in range(N):
            if initial[i][j] and initial[i][j]!=final[i][j]:
                count+=1
    return count
    
def is_safe(x,y):
    return 0<=x<N and 0 <=y<N

def print_path(root):
    if root is None:
        return
    print_path(root.parent)
    print_matrix(root.mat,root.g,root.h)

def solve(start,x,y,goal):
    cnt=0
    pq=[]
    heapq.heappush(pq,Node(start,x,y,0))

    while pq:
        m=heapq.heappop(pq)
        m.h=heuristic(m.mat,goal)

        if m.h==0:
            print("\n\nThis puzzle is solved in",cnt,"moves\n")
            print_path(m)
            return
        
        cnt+=1
        for i in range(4):
            dx=m.x+drow[i]
            dy=m.y+dcol[i]

            if is_safe(dx,dy):
                child=Node(m.mat,m.x,m.y,m.g+1,m)
                child.mat[m.x][m.y],child.mat[dx][dy]=child.mat[m.x][m.y],child.mat[dx][dy]
                child.x,child.y=dx,dy
                child.h=heuristic(child.mat,goal)
                heapq.heappush(pq,child)

def main():
    start=[[0]*N for _ in range(N)]
    goal=[[0]*N for _ in range(N)]

    x=-1
    y=-1

    print("Enter the start state: ")
    for i in range(N):
        start[i]=list(map(int,input().split()))
        if 0 in start[i]:
            x,y=i,start[i].index(0)

    print("ENter the goal state:")
    for i in range(N):
        goal[i]=list(map(int,input().split()))

    solve(start,x,y,goal)


if __name__=="__main__":
    main()