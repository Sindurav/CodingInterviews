# Got these problems in HACKERRANK challenge

- I was given 60 minutes to solve the two questions.    


## 1. Distinct Pairs
-----
In this challenge, you wi;ll be given an array of integers and a target value.  
Determine the number of distinct pairs of elements in the array that sum up to the target value.  
Two pairs (a, b) and (c, d) are considered to be distinct if and only if the values in sorted order do not match i.e. (1, 9) and (9, 1) are indistinct but (1, 9) and (9, 2) are distinct.  

For Example, given the array `[1, 2, 3, 6, 7, 8, 9, 1]` and a target value of 10, the seven pairs (1, 9), (2, 8), (3, 7), (8, 2), (9, 1), (9, 1) and (1, 9) all sum to 10 and there are only three distinct pairs: (1, 9), (2, 8), and (3, 7).


Function Description:
Complete the function `numberOfPairs` in the editor below.  
The function must return an integer, the total number of distinct pairs of elements in the array that sum to the target value.  
 
`numberOfPairs` has the following parameter(s):
- a[a[0], ..., a[n-1]]: an array of integers to select the pairs from.
  
  
Constraints:  
- 1 <= n <= 5 x 10^5
- 0 <= a[i] <= 10^9
- 0 <= k <= 5 x 10^9 
 

Input
	Sample Input 0:
	6
	1
	3
	46
	1
	3
	9
	47
	
	Sample Output 0:
	1
	
	Explanation 0:
	a = [1, 3, 46, 1, 3, 9]
	There are 4 pairs of unique elements where a[i]+a[j] = k:
	
	1. (a[0] = 1, a[2] = 46)
	2. (a[2] = 46, a[0] = 1)
	3. (a[2] = 46, a[3] = 1)
	4. (a[3] = 1, a[2] = 46)
	In the list above, all four pairs contain the same values.  
	We only have 1 distinct pair (1, 46).


## 2. Stock Analysis
-----
In data analysis, the eliminate algorithm determines the single final value to use for each data parameter.  
The eliminate algorithm works in the following way:  
- Data is acquired from multiple sources in order from least to most preferred, i.e. If a parameter `Pi` is present in both source 1 and source 2, the parameter from the higher priority source, source 2, is used in the final parameter list, and any value from an earlier source is superseded.  
- As new parameters arrive, they are added to the list.  
- If a parameter `Pi` is present only in one of the sources, it is directly added to the final parameter list. 
Hence, 
- The result of performing the above operations until all the parameters from source 1 and source 2 are exhausted is the result of Eliminate-algorithm(source 1, source 2).   
- Each time a new value for a parameter is encountered from a higher preferred site, the old data is superseded.  
- Assuming three sources S1, S2, and S3.
	- Eliminate-algorithm(S1, S2, S3) = Eliminate-algorithm(Eliminate-algorithm(S1, S2), S3)
	
Given a list of sources S1, S2, ..., Sn, find the final parameter list given by Eliminate-algorithm(S1, S2, .., Sn). Maintain your result in the order a key was first encountered.  

For example, a rating parameter of buy, sell or hold from three sources in increasing order of preference: [buy, sell, hold], where buy is from S1, immediately superseded by sell S2, immediately superseded by hold S3.   
The final rating is the only one that hasn't been superseded, so you use "hold"  as the final rating.  


Function Description:
Complete the function `computeParameterValue` in the editor below.  
The function must return an array of strings that denotes the final parameter list values in the order their keys were first encountered.  

`computeParameterValue` has following parameter(s):
sources: A 2-dimensional  array of key:value pairs, each row is one source's data, sources presented from lowest to highest preference.  
   
Constraints:  
 - 1 <= n < 100
 - 1 <= p < 1000
 
		Sample Input 0:
		2
		3
		P1:a P3:b P5:x
		P1:b P2:q P5:x

		Sample Output 0:
		b
		b
		x
		q
		
		Explanation 0:
		Final parameter list:
		- P1 b (Source 2)
		- P3 b (Source 1)
		- P5 x (Source 2)
		- P2 q (Source 2)  
		
## 3. K-Subsequences
-----		

We define a k-subsequence of an array as follows:
- It is a subsequence of contiguous elements in the array, i.e. a subarray.  
- The sum of the subsequence's elements, s, is evenlt divisible by k (i.i: s % k = 0).

Given an array of integers, determine the number of k-subsequences it contains.   
For example k = 5 and the array nums = [5, 10, 11, 9, 5].  
The 10 k-subsequences are: {5}, {5, 10}, {5, 10, 11, 9}, {5, 10, 11, 9, 5}, {10}, {10, 11, 9}, {10, 11, 9, 5}, {11, 9}, {11, 9, 5}, {5}.  


Function Description:
Complete the function `kSub` in the editor below.  
The function must return an long integer that represents the number of k-subsequences.  

`kSub` has following parameter(s):
- k: an integer that the sum of the subsequence must be divisible by 
- nums[nums[0], ..., nums[n-1]]: an array of integers
   
Constraints:  
 - 1 <= n <= 3 x 10^5
 - 1 <= k <= 100
 - 1 <= nums[i] <= 10^4
 

		