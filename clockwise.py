

chars = "0123456789abcdefghijklmnopqrstuvwxyz"

def frame_clockwise(width, height):
    # When width=5 and height=4
    # 0 1 2 3 4 
    # d       5
    # c       6
    # b a 9 8 7
    # 0 1 2 3 4
    # d       5
    # c       6
    # b a 9 8 7
    global chars
    chars = list(chars)
    grid = []
    for _ in range(height):
        row = ["-"] * width
        grid.append(row)

    print(grid)
    for i in range(width):
        grid[0][i] = chars[0]
        chars.pop(0)

    for i in range(height):
        if grid[i][-1] == "-":
            grid[i][-1] = chars[0]
            chars.pop(0)

    for i in range(width-1, -1,-1):
        if grid[-1][i] == "-":
            grid[-1][i] = chars[0]
            chars.pop(0)

    for i in range(height-1, -1 ,-1):
        if grid[i][0] == "-":
            grid[i][0] =chars[0]
            chars.pop(0)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "-":
                grid[i][j] = " "

    for i in grid:
        for row in i:
            print(row, end=" ")
        print()

    return grid
print(frame_clockwise(7,9))