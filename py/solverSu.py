
# puzzle = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,7,9]
# ]

def is_free(puzzle):
    for x in range(0,9):
        for y in range(0,9):
            if puzzle[x][y]== 0:
                return x , y
    return None,None

def is_valid(i,ix,iy,puzzle):
    key = True
    if i in puzzle[ix] :
        return False
    else:
        for adad in range(0,9):
            if i == puzzle[adad][iy]:
                key =  False
                break
        if key :
            newx = ix - ix%3
            newy = iy - iy%3
            for adad in range(newx,newx+3):
                for adaddovom in range(newy,newy+3):
                    if i == puzzle[adad][adaddovom]:
                        key = False
                        break
                if not key :
                    break
        return key

def solve(puzzle):
    # The challenge was returning true and false in solve function and also my is_free function was wrong 
    #from the begining
    px, py = is_free(puzzle)
    if px is None :
        return True
    for n in range(1,10):
        if is_valid(n,px,py,puzzle):
            puzzle[px][py] = n
            if solve(puzzle):
                return True
        puzzle[px][py] = 0
    return False

def solverSu(puzzle):
    if solve(puzzle):        
        for each in puzzle : print(each)
    else:
        print("It's unsolvable!")

