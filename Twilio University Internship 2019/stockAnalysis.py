def computeParameterValue(sources):
    mapping = {}
    for idx, source in enumerate(sources):
        for kv in source:
            k, v = kv.split(":")
            mapping[k] = v

    results = []
    for key in mapping:
        results.append(mapping[key])
    return results
