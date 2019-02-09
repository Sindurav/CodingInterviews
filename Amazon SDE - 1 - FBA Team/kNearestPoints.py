# Time complexity = O(n logn)
# Space complexity = O(n)

import math


def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))


def nearest_neighbor(points, goal_point, k):
    distances = []

    for point in points:
        distance = compute_euclidean_distance(point[0], point[1], goal_point[0], goal_point[1])
        distances.append([point, distance])
    else:
        distances.sort(key=lambda element: element[-1])

    closest_neighbors = [distances[i][0] for i in range(0, k)]
    return closest_neighbors


points_array = [[6, 3], [2, 1], [5, 2], [3, 2], [9, 0]]
goal = [3, 2]
neighbors = nearest_neighbor(points_array, goal, 3)
print(neighbors)
