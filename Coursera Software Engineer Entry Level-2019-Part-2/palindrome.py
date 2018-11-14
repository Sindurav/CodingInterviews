def palindrome(s):
    n = len(s)
    ans = set([])
    for center in range(2*n - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            ans.add(s[left: right+1])
            left -= 1
            right += 1
    return len(ans)
