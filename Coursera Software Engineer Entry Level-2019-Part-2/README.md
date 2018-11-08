# Got these problems in HACKERRANK challenge

- I was given 60 minutes to solve the two questions.    

## 1. Sub-palindrome
-----
A palindrome is a string that reads the same forward and backward e.g. `121` or `tacocat`.  
A substring is a contiguous subset of characters in a string.  
Given a string `s`, how many distinct substring of s are palindrome.   

For example, `s = mokkari`.   
Its distinct palindromic substrings are `[m, a, k, r, i, kk, akka]`.

Function Description:
Complete the function `palindrome  in the editor below.  
The function must return the number of distinct palindromes as in integer.


`palindrome` has the following parameter(s):   
   s: a string.
   
Constraints:  
 - 1 <= |s| <= 5000 
 - Each character `s[i]` belongs `ascii[a-z]`

 
 
		Sample Input 0:
		s = aabaa
		
		Sample Output 0:
		5
		
		Explanation 0:
		Palindromic substring are [a, aa, aabaa, aba, b]
		The substring "a" occurs 4 times, but is counted only once.  
		Similarly, "aa" occurs twice but counts as one distinct palindrome.
	

## 2. Triplets
-----
Given an array of `n` distinct integers, `d = [d[0], d[1], ..., d[n-1]]`, and an integer threshold `t`, how many `(a, b, c)` index triplets exist that satisfy both of the followings conditions?
- `d[a] < d[b] < d[c]`
- `d[a] + d[b] + d[c] <= t`

For example, given the array `d = [1, 2, 3, 4, 5]` and threshold `t = 8`, the following triplets satisfy the constraints:   

	(1, 2, 3) => 1 + 2 + 3 = 6 <= 8   
	(1, 2 ,4) => 1 + 2 + 4 = 7 <= 8   
	(1, 2, 5) => 1 + 2 + 5 = 8 <= 8   
	(1, 3, 4) => 1 + 3 + 4 = 8 <= 8   
		
Function Description:
Complete the function `triplets`  in the editor below.  
The function must return a long integer denoting the number of triplets of (a, b, c) triplets satisfying the given conditions.     


`triplets` has the following parameter(s):      
   t: an integer threshold.  
   d[d[0], ..., d[n-1]]: an array of integers.  
   
Constraints:  
 - 1 <= n <= 10000 
 - 0 <= d[i] < 10^9
 - 0 < t < 3x10^9
 
Input Format:
Input from stdin will be processes as follows and passed to the function
The first line contains the integer `t`.
The second line contains an integer `n`, the size og the array d.
Each of the next `n` lines contains an integer `d[i]` where 0 <= i <= n.


	Sample Input 0:
	8
	5
	1
	2
	3
	4
	5
	
	Sample Output 0:
	3
	
	Explanation 0:
	Given t=8 and d = [1, 2, 3, 4, 6] the following triplets satisfy the conditions:
	1. (0, 1, 2) =>. 1 + 2 + 3 <= 8
	2. (0, 1, 3) =>. 1 + 2 + 4 <= 8
	3. (0, 2, 3) =>. 1 + 3 + 4 <= 8
	