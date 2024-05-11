def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]==1:
            return False
        
    return True

def print_board(board,n):
    for row in board:
        print(' '.join("Q" if cell==1 else "." for cell in row))
    print()

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join("Q" if cell==1 else "." for cell in row))
        print()

def solve_n_queens_util(board,row,n,solutions):
    if row == n:
        print_board(board,n)
        solutions.append([row[:] for row in board])
        return solutions
    
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            print_board(board,n)
            solve_n_queens_util(board,row+1,n,solutions)
            board[row][col]=0

def solve_n_queens(n):
    board=[[0]* n for _ in range(n)]
    solutions=[]
    solve_n_queens_util(board,0,n,solutions)
    return solutions

if __name__ =="__main__":
    n=int(input("Enter the number of queens:"))
    solutions=solve_n_queens(n)
    print("Print all possible solution: ")
    print_solutions(solutions)