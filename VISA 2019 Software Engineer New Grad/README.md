# Got this problems in HACKERRANK challenge


## 1. Maximum Streak
----

A project manager wants to look at employee attendance data. Given that m employees are working on the project, 
and the manager has the record of the employees present on n days of the project, help him find the maximum number 
of consecutive days on which all employees were present and working on the project.

As an example there are m = 3 employees and n = 5 workdays to analyze. The attendance data strings, `data = [YYY, YYY, YNN, YYN, YYN]`. 
There are only two days at the beginning of the period , where all worker are present. 
Using zero indexing for employees, employees 1 and 2 are absent on the third day, and employee 2 is also out on the forth and fifth days. 
The maximum streak occurs at the beginning and is 2 days long.

Function Description
Complete the maxStrak function in the editor below. The function must return an integer denoting the maximum number of consecutive days where all the employees of the project are present. 

maxStreak has the following parametersL
m: an integer denoting the number of employees working on the project.
data: an array of n strings, where the value of each element data[i] is a string where `data[i][j]` denotes the `jth` employee is present on the `ith` day.


Constraints
- 1 <= m <= 10
- 1 <= n <= 100000
- Each data[i][j] belongs {"Y", "N"}

		Sample Input 0:
		2
		2
		YN
		NN
		Sample Output 0:
		0
		

		Sample Input 1:
		3
		1
		NYY
		Sample output 1:
		0
		
		Sample Input 2:
		4
		5
		YNYY
		YYYY
		YYNY
		NYYN
		Sample Output 2:
		2
		
## 2. Binary Jumps
----

In a revised game of hopscotch a child is trying to cross a line of tiles with a binary string painted on it. Consider the line of tiles to be like 1D array, where each tile has either a 1 or a 0, and a consecutive series of tiles makes the whole string. The game starts with the child standing in front of the leftmost character of the string.
- All jumps to reach the end of the string can only be on tiles with 0 or only be in the tiles with 1.
- The game is won if the child can reach at the end of the string, taking jumps with minimum required power. The power of a jump is given by the number of tiles in the path of a jump as indicated in the diagram below. In 10101, the power of the jump from beginning to the first tile is 1 but from the first tile to the third tile is 2, and so on

Find the minimum power the child's jump should have in order to win the game for different binary strings.
NoteL The value on the last tile determines which tiles to jump on. This is because all tiles landed on mush have the same value and the child must land on the last tile to complete the fame. In one jump, the child can jump to the right, any distance from 1 to the value of the power of her jump.


Constraints
- 1 <= Length of game <= 100000
- s[i] contains either "1" or "0"

		Sample Input 0:
		11111
		Sample Output 0:
		1
		

		Sample Input 1:
		10101
		Sample output 1:
		2


# Got RUNTIME ERROR for the current solution
## 3. Flower Bouquets 
----
Lara owns a flower shop, where she sells only two types of flower bouquets:
- Type 1: the first type of bouquet contains three roses and costs p dollars.
- Type 2L The second type of bouquet contains one cosmos and one rose and costs q dollars.

Lara grows these flowers in her own garden in a single tow. Consider the row as a one-dimensional array, here each cell either contains a rose or a cosmos. For example array 001101011, here 0 indicates rose and 1 indicates cosmos.

Lara follows an important rule when she makes the bouquets: she makes each bouquet with only conse cutive flowers fromm the array. For example in a bouquet, the flower from consecutive (i, i+1, and i+2) in the array can be present, but not from non-consecutive indices (i and i+2) in the array above, Lara can not make any bouquets of type 1 but she can make 3 bouquets of type 2

Now she wonder what is the maximum profit she can make if she makes these bouquets optimally. You are given a binary string representing her garden row. calculate the maximum profit Lara can make. Remember that it is not necessary to use every flower

Function Description:

Complete the flowerBouquets function in the editor below. The function must return an integer that denotes the maximum profit Lara can make if she makes her bouquet optimally.

flowerBouqets has three parameters:
- p: integer denoting the cost of a bouquet of type 1.
- q: integer denoting the cost of a bouquet of type 2.
- s: string denoting the garden pattern, where zero indicated rose and on indicates cosmos

Constraints:

- 1 <=  p,q <= 1000
- 1 <= |s| <= 100000


		Sample Input 0:
		2
		
		3
		0001000
		Sample Output 0:
		5
		
		Explanation 0
		Lara can make two bouquets of three roses by the corresponding indexes: [0, 1, 2] and [4, 5, 6] and can earn 2+2 = 4 profit.
		**OR**
		Lara can make one bouquet of three roses by the corresponding indexes: [0, 1, 2] and one bouquet of one rose and one cosmos by corresponding indexes (3, 4) and can earn 2+3 = 5 profit.
		5 i greater than 4 so print 5
		
		
		
		
		

		