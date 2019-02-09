def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    n = len(states)
    states = [0]+states+[0]
    for day in range(days):
        new_states = [0]+[1]*n+[0]
        for idx in range(1, len(states)-1):
            state = states[idx]
            if states[idx-1] == states[idx+1]:
                new_states[idx] = 0
        states = new_states
    return new_states[1:len(states)-1]


print(cellCompete([1, 0, 1, 1, 0, 1, 0], 3))
print(cellCompete([0, 0, 1, 0, 0, 1, 1], 5))
