# Complete the checkJSON function below.

def solution(string, character):
    for idx, char in enumerate(string):
        if char == character:
            return idx
    return -1

res = solution("hi, this is bitgo test", "t")
print(res)
