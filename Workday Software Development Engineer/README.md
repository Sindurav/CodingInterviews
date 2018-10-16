# Got this problems in HACKERRANK challenge


## 1. Array Reduction
-----


Anna has an array of n integers called sum.
She can reduce the array by 1 element by performig a move.
Each move consists of following three steps:
1. Pick two different elements.
2. Remove the two selected elements from array.
3. Add the sum of the two selected elements to the end of the array.

Each move has a cost associated with it.
The cost is equal to the sum of the two elements removed from the array during the move.
Anna wishes to calculate the minimum total cost of reducing her array to one element.

Function Description:   
Complete the function `reductionCost`.   
The function must return the minimum total cost of reducing the input array to one element.   

`reductionCost` has following parameters:
num[num[0], ..., num[n-1]]: an array of integers.

Constraints:  
- 2 <= n <= 10000.
- 0 <= num[i] <= 100000

		Sample Input 0:
		3
		1
		2
		3
		Sample Output 0:
		9
		
		Explanation 0:
		Anna makes the following moves to reduce the num = [1, 2, 3]:
		1. Removes 1 and 2 at cost1 = 1+2 = 3, resulting in num1 = [3, 3]
		1. Removes 3 and 3 at cost2 = 3+3 = 6, resulting in num2 = [6]
		When we sum up the cost at each reduction, we get 3+6 = 9
		
		Sample Input 1:
		3
		4
		6
		8
		Sample output 1:
		28
		