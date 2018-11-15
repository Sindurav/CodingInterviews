# Got these problems in HACKERRANK challenge


- I was given 120 minutes to solve the the following questions.    
- I failed at this miserably hence the solutions that I am giving did not pass all the test cases.
- I am not giving out all the solution as other solutions were completely wrong.
- The current solutions are partially correct. 


## MCQ 1 
----
B-Trees are used commonly for:    
Pick one of the following:   

- efficiently sorting very large files
- for checking the consistency of relational databases
- speeding up database search, delete, and insert operations
- organizing hash tables efficiently

## MCQ 2
----

We perform following sequence of actions:

1. Insert th following into a set: 1, 2, 9, 1, 2, 3, 1, 4, 1, 5, 7.   
2. Convert the set into list and sort it in ascending order.   

Which option denotes the sorted list?   

- {1, 2, 3, 4, 5, 7, 9}
- {9, 7, 5, 4, 3, 2, 1}
- {1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9}
- None of the above.

## MCQ 3
----

Check the following statements that are true.  
Pick the correct choices  
- It is more time efficiently to iterate through a doubly linked list in reverse than a singly linked list in reverse
- A doubly linked list is more space efficient than a singly linked list
- Deleting a node in a doubly linked list is more time efficient than deleting a node in a singly linked list
- Singly and doubly linked list are more efficient than an array


## MCQ 4
----

What are some ways to make it easier to test a class / function / feature ? (check all that apply)

- Ensure that all class dependencies are passed into the class constructor
- Reduce or eliminate a function's side-effects
- Make a class' dependencies abstract (i.e interfaces) instead of concrete implementations
- Split larger classes into smaller ones that each have a single responsibility


## MCQ 5
----

What is the return value of this function?

	function f(array, length)
		int i := 0
		int result := 0
		while (i < length)
			tmp := array[i]
			if (tmp > result)
				result := tmp
			end if
			i := i+1
		end while 
		return result 
	end function 
	
- the first value in the array
- the largest value in the array 
- the median of the array 
- the smallest value in the array

## MCQ 6 Smart Mutex Use
----

Which of the following statements are true regarding the snippet of pseudo-code below?

	global int a = 0
	global mutex A = unlocked
	
	global int b = 0
	global mutex B = unlocked
	
	// The following function is called in parallel by many different threads.
	function critical_sections()
		// Critical Section (1)
		A.lock()
		a := a + 1
		
		B.lock()
		b := a + b
		
		B.unlock()
		A.unlock()
		
		// Critical Section (2)
		B.lock()
		b := b + 1
		
		A.lock()
		a := a - b
		
		B.unlock()
		A.unlock()
		
		// Output Results
		print("A =" + a)
		print("B =" + b)
	end function
	
Pick the correct choices:  
- Critical section (1) unlocks B before A, resulting in a potential deadlock in critical section (1).
- Critical section (2) unlocks B before A, resulting in a potential deadlock in critical section (2).
- Critical section (1) and critical section (2) lock A and B in a inconsistent manner, resulting in a potential deadlock.  
- The print statements at the end of the function access a shared variable in an unsafe manner.  
- The code is correct when run concurrently on a single CPU, but is unsafe on a multi-core processor.  


## MCQ 7 - Traversal Order
----	

	function f(node)
		if node is null
			return 
		end if
		f(node.left)
		f(node.right)
		visit(node)
	end function

Pick one of the choices

- A, B, C, D, E, F, G, H, I
- D, G, H, I, E, F, B, C, A
- A, B, D, E, G, H, C, F, I
- D, B, G, E, H, A, C, I, F
- D, G, H, E, B, I, F, C, A

## MCQ 8 - Following code
----
Consider the following pseudo-code:
	function f(int i)
		int x := 1
		int loop := 1
		while (loop < 10)
			x := (x*x)+ 1
			loop := loop + 1
			if (loop equals i)
				break
			end if
		end while 
		return x
	end function
	
What value returned if the function `f` is called with input `i` set to 4?
f(4) will return ______________


## MCQ 9 - Twos complement representation
----

Assume the following binary values are all signed 8-bit values, represented in twos-complement format, with a decimal range of -128 to 127.  
true when two values are equal:    
 _________ 00001010 > 00000111   
 _________ 11111111 > 01111111   
 _________ (11111111 + 11111111) > 00000001 - 00000010   
 _________ (00000100 * 00000100) == 00010000   
 _________ (11111010 * 00000011) == 11101110   
 _________ (00000100 / 00000100) == 11100000   
 _________ (11110000 - 00000001) == 10001111   

## MCQ 10 - Recursion

Complete the blanks in the following question with the appropriate answer.

Consider the following pseudo-code that finds the greatest common divisor of two integers:   

	function gcd(int a, int b)
		if (a equals b)
			return a
		end if
		if (a < b)
			return gcd(a, b - a)
		else
			return gcd(a - b, b)
		end if
	end function
	
How many times is the function gcd entered, including the initial call, if a program calls `gcd(15, 21)`?   
the gcd() function is entered _________ times.


## 11. Account Validation
----


## 12. Travel Distance
----


## 13. Longest Trip
----