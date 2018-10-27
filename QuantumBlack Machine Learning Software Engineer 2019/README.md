# Got these problems in HACKERRANK challenge


## 1. Computing the Correlation
-----
You are given  the scores of **N** students in three different subjects, Maths, Physics, and Chemistry.
All three are graded on a scale of 0 to 100.
Your task is to compute the Pearson product moment correlation coefficient between the scores of different pairs of subject.This data is based on the records of the CBSE K-12 Exam, a national school leaving exam in India, for year 2013.

Input Format:
The first row contains an integer **N**.
This is followed by **N** rows containing three space-separated integers ** M, P, C** corresponding to a candidate's scores in Maths, Physics, Chemistry.
Each row contains to the scores obtained in these three subjects by one students.

Input Constraints:
- 1 <= N <= 500000
- 0 <= M, P, C <= 100

Output Format:
The output should contain three lines, with correlation coefficients computed and rounded **off to exactly 2 decimal places.**
The first line should contain the correlation coefficient between Maths and Physics scores.
The second line should contain the correlation coefficient between Physics and Chemistry scores.
The third line should contain the correlation coefficient between Chemistry and Maths scores.




## 2. Distinct Pairs
-----
In this challenge, you will be given an array of integers and a target value. 
Determining the number of distinct pairs of elements in the array that sum to the target value.
Two pairs (a, b) and (c, d) are considered to be distinct if and only if the values in sorted order do not match, i.e., (1, 9) and (9, 1) are indistinct but (1, 9 ) and (9, 2) are distinct.

For instance given the array [1, 2, 3, 6, 7, 8, 9, 1] and a target value of 10, the seven pairs (1, 9), (2, 8), (3, 7), (8, 2), (9,1), and (1, 9) all sum to 10 and only three distinct pair: (1, 9), (2, 8), and (3, 7).

Function Description:
Complete the function numberOfPairs. The function must return an integer, the total number of distinct pairs of elements in the array that sum to the target value.

numberOfPairs has following parameters:
a[a[0], ..., an-1]]: an array of integers to select the pairs from 
k: target integer value to sum to

Constraints:  
- 1 <= n <= 500000
- 0 <= a[i] <= 1000000000
- 0 <= k <= 500000

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
		a = [1, 3, 46, 1, 3, 9], k = 47
		There are 4 pairs of unique elements where a[i]+a[j] = k
		1. (a[0] = 1, a[2] = 46)
		2. (a[2] = 46, a[0] = 1)
		3. (a[2] = 46, a[3] = 1)
		4. (a[3] = 1, a[2] = 46) 

## 3. Simple queries
-----

Given two array if positive integer, for each element in the second array, find the total number of elements in the first array which are less than or equal to that element.
Store the values determined in an array.
For example, if the first array is `[1, 2, 3]` and the second array is `[2, 4]`, then the there are 2 elements in the first array less than or equal to 2.
There are 3 elements in the first array which are less than or equal to 4.
We can store these answers in an array, answer = [2, 3].

Function Description:
Complete the function `counts`. 
The function must return an array of m positive integers, one for each maxes[i] representing the total number of elements nums[j] satisfying nums[j]<=maxes[i], where 0 <= j < n and 0 <= i < m, in given order

counts has the following parameters:
num[nums[0], ,..., nums[n-1]]: first array of positive integers
maxes[maxes[0], ,..., maxes[n-1]]: second array of positive integers


Constraints:  
- 2 <= n, m <= 100000
- 1 <= nums[j] <= 1000000000, where 0 <= j < n
- 1 <= maxes[i] <= 1000000000, where 0 <= i < m.

		Sample Input 0:
		4
		1
		4
		2
		4
		2
		3
		5
		
		Sample Output 0:
		2
		4
			
		Explanation 0:
		We are given n = 4, nums = [1, 4, 2, 4], m = 2, and maxes = [3, 5].
		1. For maxes[0] = 3, we have 2 elements in nums (nums[0] = 1, and nums[2] = 2) that are <= maxes[0].
		2. For maxes[1] = 5, we have 4 elements in nums (nums[0] = 1, nums[1] = 4, nums[2] = 2, and nums[3] = 4) that are <= maxes[1].
		Thus the function returns the array [2, 4] as the answer.