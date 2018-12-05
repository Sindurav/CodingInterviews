# Time complexity = O(m*n) ==> if we ignore the list concatenation operation
# You can optimize list concatenation operation by using a linked list
# Space complexity = O(m*n)
# Use BFS
# You can optimize the space complexity to O(1) if you change the values of the matrix
# A better tome efficient solution is Dijkstra's Algorithm

from collections import deque


def is_valid(x, y, n, m, matrix, visited):
    if (0 <= x < n) and (0 <= y < m) and (matrix[x][y] == 1) and ((x, y) not in visited):
        visited.add((x, y))
        return True
    return False


def shortest_path(matrix, start, goal):
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))

    visited = set([])
    visited.add((start[0], start[1]))

    queue = deque()
    queue.appendleft([start[0], start[1], 0, [start]])

    while queue:

        x, y, step, path = queue.pop()

        if [x, y] == goal:
            return path

        for i in range(len(neighbors)):
            new_x = x+neighbors[i][0]
            new_y = y+neighbors[i][1]
            if is_valid(new_x, new_y, len(matrix), len(matrix[0]), matrix, visited):
                queue.appendleft((new_x, new_y, step+1, path+[[new_x, new_y]]))

    return []


mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
       [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
       [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]


a = [0, 0]
b = [5, 7]
result_path = shortest_path(mat, a, b)
print(result_path)
