import solverSu

print("Welcome to the Sudoku solver!\nPlease input your puzzle line by line:\n")
print("[separate each numbers by ',' and place 0 for empty fields]")

puzzle = []
for i in range(1,10):
    temp = input(f"{i}- ").split(",")
    temp = list(map(lambda x: int(x), temp))
    puzzle.append(temp)
print(puzzle)
solverSu.solverSu(puzzle)
