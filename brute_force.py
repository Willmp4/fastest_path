import random

class Position:

    def __init__(self,x=0,y=0):
        self.x = x 
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Node:

    def __init__(self, x=0, y=0, data=None, passable=True):
        self.passable = passable
        self.x= x
        self.y= y
        self.data = data
        self.position = Position(self.x,self.y)

    def __repr__(self):
        return f"{self.position}"
        


class Grid:
    
    def __init__(self,rows,cols):
        self.e =random.randint(0,rows-1)
        self.e1 = random.randint(0,cols-1)
        self.start_node = Node(0,0,"S")
        self.end_node = Node(self.e, self.e1,"E")
        self.rows = rows
        self.cols = cols
        self.board = []

    def make_board(self):
        
        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                if row == 0 and col == 0:
                    self.board[row].append(self.start_node)
                elif row == self.e and col == self.e1:
                    self.board[row].append(self.end_node)
                else:
                    c= random.randint(0,self.cols)
                    r = random.randint(0,self.rows)
                    if row == r or c == col:
                        self.board[row].append(Node(row,col,"#",False))
                    else:
                        self.board[row].append(Node(row,col,"."))
        return self.board


    def __getitem__(self,n):

        return self.board[n].data
    

    
def find_path(grid=None, start_node=None, end_node=None):
    if not grid: return[]
    prev, bag = {start_node: None}, [start_node]
    w, h = len(grid), len(grid[0])
    inbound = lambda n, m :(0<=n<w and 0<=m<h)  
    passable = lambda n: n.passable and n not in prev
    while bag:
        node = bag.pop(0)
        if node == end_node:
            path = []
            while node:
                path.append(node)
                node = prev[node]
            return path[::-1]

        x, y = node.position.x, node.position.y 
        for i, j in (1,0),(0,1),(0,-1),(-1,0):
            n,m = x + i, y + j
            if not inbound(n,m): continue 
            next_node = grid[n][m]
            if passable(next_node):
                bag.append(next_node)
                prev[next_node] = node
            

def print_board(grid= None, path = None):
    res = []
    w, h = len(grid), len(grid[0])
    for row in range(w):
        res.append([])
        for col in range(h):
            if path:
                if grid[row][col] in path[1:-1]:
                    res[row].append("Y")
                else:
                    res[row].append(grid[row][col].data)
            else:
                res[row].append(grid[row][col].data)
    return '\n'.join([' '.join(row) for row in res])


g = Grid(50,50)
g.make_board()
p = find_path(g.board, g.start_node, g.end_node)
print(print_board(g.board, p))
