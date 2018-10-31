# Complete the replaceCharacters function below.
def replaceCharacters(original):
    mapping = {"<": "&lt;", ">": "&gt;", "&": "&amp;"}
    results = ""
    for i in range(len(original)):
        if original[i] in mapping:
            results += mapping[original[i]]
        else:
            results += original[i]
    return results
