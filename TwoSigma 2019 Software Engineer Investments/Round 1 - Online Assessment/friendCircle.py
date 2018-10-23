# Complete the friendCircles function below.


def friendCircles(friends):
    sets = []
    for i in range(0, len(friends)):
        sets.append(i)

    for i in range(1, len(friends)):
        for j in range(0, i):
            if (friends[i][j]) == "Y":
                sets[make_sets(i, sets)] = make_sets(j, sets)

    res = set([])
    for i in range(0, len(friends)):
        res.add(make_sets(i, sets))
    return len(res)


def make_sets(node, sets):
    while sets[node] != node:
        sets[node] = sets[sets[node]]
        node = sets[node]
    return node