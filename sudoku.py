#Basic Module
#Program to solve Sudoku Problem Using BackTracking Approach
board = [[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]
def solve(bo):

    find = find_empty(bo)
    if find:
        row,col = find
    else:
        return True
    for i in range(1,10):
        if valid(bo,(row,col),i):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False


def valid(bo,pos,num):
    #check Row
    for i in range(0,len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #chech Column
    for i in range(0,len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
    
    #check Box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)
solve(board)
print("<------------------------------------------->")
print("<------------------------------------------->")
print("<------------------------------------------->")
print_board(board)

"""Problem Matrix1
| 3 0 6  | 5 0 8  | 4 0 0 
| 5 2 0  | 0 0 0  | 0 0 0 
| 0 8 7  | 0 0 0  | 0 3 1 
- - - - - - - - - - - - - -
| 0 0 3  | 0 1 0  | 0 8 0 
| 9 0 0  | 8 6 3  | 0 0 5
| 0 5 0  | 0 9 0  | 6 0 0
- - - - - - - - - - - - - -
| 1 3 0  | 0 0 0  | 2 5 0
| 0 0 0  | 0 0 0  | 0 7 4
| 0 0 5  | 2 0 6  | 3 0 0

Soution Matrix1

| 3 1 6  | 5 7 8  | 4 9 2
| 5 2 9  | 1 3 4  | 7 6 8
| 4 8 7  | 6 2 9  | 5 3 1
- - - - - - - - - - - - - -
| 2 6 3  | 4 1 5  | 9 8 7
| 9 7 4  | 8 6 3  | 1 2 5
| 8 5 1  | 7 9 2  | 6 4 3
- - - - - - - - - - - - - -
| 1 3 8  | 9 4 7  | 2 5 6
| 6 9 2  | 3 5 1  | 8 7 4
| 7 4 5  | 2 8 6  | 3 1 9    """