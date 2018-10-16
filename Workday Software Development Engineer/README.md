# Got this problems in HACKERRANK challenge


## 1. Array Reduction
-----

Anna has array of `n` integer called `num`.
She can reduce the array 1 element by performing a move.
Each move consists of the following three steps:
1. Pick two different elements.
2. Remove the two selected elements from the array
3. Add the sum of the selected elements to the end of the array

Each move has a `cost` associated with it, and this cost is equal to the sum of the two elements removed from the array during the move.
Anna wishes to calculate the minimum total cost of reducing her array to one element.   

For example consider `num = [4, 6 ,8]`.   
Anna removes 4 and 6 in her first move at the cot of 4+6=10 and resulting `num1 = [8, 10]`.   
She then removes 8 and 10 in her second move at a cost of 8+10=18 and resulting `num2 = [18]`.  
The total cost of reducing this array to one element using this sequence of moves is 10+18=28.  
This is just one set of possible moves. For instance, she could have started with 4 and 8.   

Function Description:
Complete the function `reductionCost`. The function must return minimum total cost of reducing the input array to one element.

reductionCost has the following parameters:   
num[num[0], ..., num[n-1]]: an array of integers

Constraints
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
		Anna makes the following moves to reduce the array num = [1, 2, 3]:
		1. Removes 1 and 2 at cost1 = 1+2 = 3, resulting in num1 = [3, 3].
		2. Removes 3 and 3 at cost2 = 3+3 = 6, resulting in num2 = [6].
		
		When we sum up the cost of each reduction, we get 3+6 = 9
		
		