def distance2Obstacle(numRows, numColumns, lot):
    q = []  # initialize queue
    q.append((0, 0, 0))  # append start point with dist=0
    lot[0][0] = -1  # mark cell(0,0) as visited
    while len(q) > 0:
        temp = q.pop(0)  # pop element
        x, y, dist = temp[0], temp[1], temp[2]  # get x-coord, y-cord and dist so far
        lot[x][y] = -1  # mark popped cell as visited
        # calculating neighbors in horizontal and vertical directions
        row_add = [-1, 0, 1, 0]
        col_add = [0, 1, 0, -1]
        for t in range(0, 4):
            # calculate new cell positions (neighbors)
            nrow = x + row_add[t]
            ncol = y + col_add[t]
            # validate neighbors bounds
            if 0 <= nrow < numRows and 0 <= ncol < numColumns:
                # check if the cell is valid and not visited
                if lot[nrow][ncol] == 1:
                    q.append((nrow, ncol, dist + 1))  # append new neighbor cell with its corresponding dist
                # check if neighbor cell is obstacle
                elif lot[nrow][ncol] == 9:
                    return dist + 1  # return corresponding dist
    # return -1 if obstacle not found
    return -1


inputs = [[[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [9, 1, 1, 1], [0, 1, 1, 1]],
          [[1]],
          [[1, 0], [1, 9]],
          [[1, 1, 1, 1], [1, 0, 0, 1], [1, 9, 1, 1]]
          ]
for inp in inputs:
    print distance2Obstacle(len(inp), len(inp[0]), inp)
