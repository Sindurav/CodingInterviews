#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

from collections import defaultdict

def longestChain(words):
    # Write your code here
    if not words:
        return 0
    
    words = sorted(words, key=len)
    longest = 0
    mapping = defaultdict(int)
    for word in words:
        if word in mapping:
            continue
        mapping[word] = 1
        for i in range(0, len(word)):
            new_word = word[:i]+word[i+1:]
            if (new_word in mapping) and ((mapping[new_word]+1)>(mapping[word])):
                mapping[word] = mapping[new_word]+1
        longest = max(longest, mapping[word])
    return longest
