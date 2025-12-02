
def showField(height, length):
    field = [[0 for _ in range(length)] for _ in range(height)]
    for i in field:
        print(i)


showField(10,10)


import random

def generate_maze(rows, cols):
    # Initialize grid with walls
    grid = [['#'] * cols for _ in range(rows)]

    def carve_path(row, col):
        grid[row][col] = ' '  # Mark as visited
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Possible moves
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '#':
                grid[row + dr//2][col + dc//2] = ' ' # Carve passage
                carve_path(new_row, new_col)

    carve_path(1, 1) # Start at (1,1)
    return grid


rows, cols = 15, 15
maze = generate_maze(rows, cols)
for row in maze:
    print(''.join(row))