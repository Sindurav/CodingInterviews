def cutSticks(lengths):
    # Write your code here
    results = []
    while lengths:
        results.append(len(lengths))
        mini = min(lengths)
        new_lengths = []
        for i in range(len(lengths)):
            lengths[i] -= mini
            if lengths[i] != 0:
                new_lengths.append(lengths[i])

        lengths = new_lengths

    return results
