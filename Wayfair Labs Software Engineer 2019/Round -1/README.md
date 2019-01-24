# Codility Assessment (130 minutes)

## 1. Bug fix question
-----  

You are given an implementation of a function:  

`def solution(S)`  

that given a non-empty string consisting of N lowercase English letters, returns the character which occurs most frequently in the string.  
If more than one character satisfies this requirement, the function should return the earliest alphabetically.  
For example, if both c and d are the most frequent letters, then the answer is c.  

For example, given a string:  

`S = "hello"`  

the function should return "1". It appears twice in S. No other characters appear as frequently.

The attached code is still **incorrect** on some inputs.  
Despite the error(s), the code may produce a correct answer for the example test cases.  
The goal of the exercise is to find and fix the bug(s) in the implementation.  
You can modify at most **four** line.

Write an efficient algorithm for the following assumptions:  
- N is an integer within the range[1.. 100,000];
- string S consists only of lowercase letters(a-z).


## 2. Physical Algorithm
-----  

Your room is being decorated.  
On the largest wall you would like to paint a skyline.  
The skyline consists of rectangular building arranged in a line.  
The building are all of the same width, but they may have different heights.  
The skyline shape is given as an array `A` whose elements specify the heights of consecutive building. 

For example, consider array `A` such that:

	A[0] = 1
	A[1] = 3
	A[2] = 2
	A[3] = 1
	A[4] = 2
	A[5] = 1
	A[6] = 5
	A[7] = 3
	A[8] = 3
	A[9] = 4
	A[10] = 2

The shape specified by this array is represented by the figure below.  

[image1]: ./images/q2f1.JPG "q2f1"
![q2f1][image1]  


[image2]: ./images/q2f2.JPG "q2f2"
![q2f2][image2]

You would like to paint the skyline using continuous horizontal brushstrokes.  
Every horizontal stroke is one unit high and arbitrary wide.   
The goal is to calculate the minimum number of horizontal strokes needed.    
For example the above shape can be painted using nine horizontal strokes.   

Starting from the bottom, you can paint the skyline in horizontal stripes with 1, 3, 2, 2, 1 strokes per respective stripe. 
Write a function:  

`def solution(A)`   

that given a non-empty array A consisting of N integers, returns the min number of horizontal brushstrokes needed to paint the shape represented by the array.  

The function should return -1 if the number of strokes exceeds 1,000,000,000.  

For example, given array A as described above, the function should return 9, as explained above.  

On the other hand, for the following array A:  

	A[0] = 5
	A[1] = 8 

the function should return 8, as you must paint one horizontal stroke at each height from 1 to 8.  

For the following array:  

	A[0] = 1
	A[1] = 1
	A[2] = 1
	A[3] = 1   

The function should return 1, as you can paint this shape using a single horizontal stroke.  

Write an **efficient** algorithm for the following assumptions:  

- N is an integer within the range[1.. 100,000];
- each element of array A is an integer within the range [1.. 1,000,000,000].



## 3. Mathematical Algorithm
-----  

There are N cities arranged in a row.  
Cities are numbered from 0 to N-1, form left to right.  
Each city has an attractiveness level, which will be denoted by an integer: the higher the better.  

You would like to go on a trip to visit two cities (it is possible to visit the same city twice).  
The appeal of your trip is the attractiveness level of the visited cities increased by the distance between them  
(two neighboring cities are at a distance of 1 from each other).  
The goal is to find the trip with the highest possible level of appeal.  

Write a function:  

`def solution(A)`  

that, given an array A consisting of N integers (A[K] denotes the attractiveness level of the K-th city),   
returns the highest possible appeal of your trip.  

1. Given A = [1, 3, -3] your function should return 6.  
There six possible trips:  

- if you visit city 0 two times, then appeal of trip is A[0] + A[0] + (0-0) = 1 + 1 + 0 = 2  
- if you visit city 1 two times, then appeal of trip is A[1] + A[1] + (1-1) = 3 + 3 + 0 = 6  
- if you visit city 2 two times, then appeal of trip is A[2] + A[2] + (2-2) = (-3) + (-3) + 0 = -6  
- if you visit city 0 and 1, then appeal of trip is A[0] + A[1] + (1-0) = 1 + 3 + 1 = 5
- if you visit city 0 and 2, then appeal of trip is A[0] + A[2] + (2-0) = 1 + (-3) + 2 = 0  
- if you visit city 1 and 2, then appeal of trip is A[1] + A[2] + (2-1) = 3 + (-3) + 1 = 1  


Visiting city 1 two times has the highest appeal equal to 6.  

2. Given A = [-8, 4, 0, 5, -3, 6] your function should return 14, because you can visit cities 1 and 5.  
The attractiveness level are: A[1]=4, A[5]=6 and the distance is `5 - 1 = 4`.   
So, in total, the highest appeal of your trip is 4 + 6 + 4 = 14.  

Write an efficient algorithm for the following assumptions:  
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [-1,000,000,000..1,000,000,000]. 



  





