def nearby_water(i, j):
    neighbors = [(0,1), (1,0), (-1, 0), (0,-1)]
    count = 4
    for neighbor in neighbors:
        m, n = i + neighbor[0], j + neighbor[1]
        if 0<=m<width and 0<=n<height:
            count -= grid[m][n]
    return count

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

width, height = len(grid), len(grid[0])
Perimeter = 0

for i in range(width):
    for j in range(height):
        if grid[i][j] == 1:
            Perimeter += nearby_water(i, j)

print Perimeter
