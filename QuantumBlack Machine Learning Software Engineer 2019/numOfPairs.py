def numberOfPairs(a, k):
    history = {}
    result = set()
    for num in a:
        if num in history:
            result.add(tuple(sorted([num, history[num]])))
        else:
            history[num] = k - num

    return len(result)
