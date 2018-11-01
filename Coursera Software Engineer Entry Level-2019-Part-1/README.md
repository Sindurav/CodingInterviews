# Got these problems in HACKERRANK challenge


## 1. Find the Substring
-----
We define the following:
- String `s` consists of lowercase letters in the range ascii[a-z].
- String `x` consists of lowercase letters and may also contain a single wild-card character `*`, that represents any one character.   

Given `s` and `x`, we want to know the zero-based index of the first occurrence of `x` in `s`. 
For example, if `s = xabcdey` and `x = ab*de`, the index is `1`.   

[image1]: ./images/Q1E1.JPG "Question 1 Example 1"
![Question 1 Example 1][image1]

Function Description:
Complete the function `firstOccurence` in the editor below.   
The function must return an integer denoting the zero-based index of the first occurrence of string `x` in `s`.  
If `x` is not in `s` return `-1` instead.  

`firstOccurence` has the following parameter(s):   
   `s`: a string of lowercase letters.
   `x`: a string of lowercase letter which may contain 1 instance of wild-card character `*`
   
 
Constraints:  
 - 1 <= |s| <= 500000
 - 1 <= |x| <= 1000
 
Input Format for Custom Testing:
Input from stdin will be processed as follows and passed to the function.

The first line contains the string `s`.
The second line contains the string `x`.
 
 
	Sample Input 0:
	juliasamanthantjulia
	ant
	
	Sample Output 0:
	8
	
	Explanation 0:   
		
[image2]: ./images/Q1E2.JPG "Question 1 Example 2"
![Question 1 Example 2][image2]
		
	Sample Input 1:
	juliasamanthhasamanthajulia
	has
	
	Sample Output 1:
	11
	
	Explanation 1:    
		
[image3]: ./images/Q1E3.JPG "Question 1 Example 3"
![Question 1 Example 3][image3]
		
		
	Sample Input 2:
	juliasamanthhasamanthajulia
	ant*as
	
	Sample Output 2:
	8
	
	Explanation 2:   
		
[image4]: ./images/Q1E4.JPG "Question 1 Example 4"
![Question 1 Example 4][image4]
		
		
		
## 2. Longest Subarray
-----
We define a subarray of array `a` to be a contiguous block of `a's` elements having a length that is less than or equal to the length of array `a`.  
For example, the subarrays of array `a = [1, 2, 3]` are `[1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]`.   
Now, let's say we have an integer `k = 3`.   
The subarrays of array `a` having elements that sum to a number <= `k` are `[1], [2], and [1, 2]`.   
The longest of these subarrays is `[1, 2]`, which has a length of 2.   

 
		
Function Description:
Complete the function `maxLength`  in the editor below.  


`maxLength` has the following parameter(s):      
   1. An array of integers `a`.  
   2. An integer, `k`. 


The function must return the length of the longest subarray having elements that sum to a number less than or equal to k.   
You can not reorder the array's elements.   
   
   
Constraints:  
 - 1 <= n <= 10000 
 - 1 <= a[i] < 10^3
 - 1 < k < 10^9
 

Input Format:
Locked stub coee in the editor reads the following input from stdin and passes it to the function:
The first line contains a single integer, `n`, denoting the number of elements in array `a`.
Each line `i` of the `n` subsequent lines (where 0 <= i <= n) contains an integer describing element `i` in array `a`.   
The laast line contains an integer, `k`.

Output Format:
The function must return the length of the longest subarray having a sum less than or equal to `k`.  
This is printed to stdout by locked stub coede in the editor.

	Sample Input 0:
	3
	1
	2
	3
	4
	
	Sample Output 0:
	2
	
	Explanation 0:
	The subarrays of [1, 2, 3] having elements that sum to a number <= (k = 4) are [1], [2], [3] and [1, 2].  
	The longest of these is [1, 2], which has a length of 2.  
	Thus, we return 2 as our answer.
	
	Sample Input 1:
	4
	3
	1
	2
	1
	4
	
	Sample Output 0:
	3
	
	Explanation 0:
	The subarrays of [3, 1, 2 , 1] having elements that sum to a number <= (k = 4) are [3], [1], [2], [1], [3, 1], [1, 2], [2, 1] and [1, 2, 1], which has a length of 3.    
	The longest of these is [1, 2, 1], which has a length of 2.  
	Thus, we return 3 as our answer.
	
	
