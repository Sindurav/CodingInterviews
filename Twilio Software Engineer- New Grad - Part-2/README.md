# Got these problems in HACKERRANK challenge

- I was given 45 minutes to solve the two questions.    


## 1. Hosts and Total Number of Requests
-----
In this challenge, write a program to analyze a log file and summarize the results.   
Given a text file of an http requests log, list the number of requests from each host.  
Output should be directed to a file as described in the Program Description below.

The format of the log file, a text file with a `.txt` extension, follows.     
Each line contains a single log record with the following columns (in order):     
1. The hostname of the host making the request.    
2. This column's value are missing and were replaced by hyphen.   
3. This column's value are missing and were replaced by hyphen.   
4. A timestamp enclosed in square brackets following the format [DD/mm/YYY:HH:MM:SS-0400].   
5. The request, enclosed in quotes(eg, "GET/images/NASA-logosmall.gif HTTP/1.0").  
6. The HTTP response code.  
7. The total number of bytes sent in the response.  


Function Description:
Your function must create a unique list of hostnames with their number of requests and output to a file names records_filename where filename is names `records_filename` where `filename` is replaced with input `filename`.   
Each `hostname` should be followed by a space then the number of requests and a newline.  
Order doesn't matter.
  

   
Constraints:  
 - The log file has a maximum pf 200000 lines of records
 
		Sample Input 0:
		host_access_log_00.txt
		
		Sample Output 0:
		unicomp6.unicompt.net 4
		burger.letters.com 3
		d104.aa.net 3
		
		Explanation 0:
		The log file hosts_access_log_00.txt contains the following log records;
		unicomp6.unicompt.net - - [01/JUL/1995:00:00:06 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985 
		burger.letters.com - - [01/JUL/1995:00:00:11 - 0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
		burger.letters.com - - [01/JUL/1995:00:00:12 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 304 0
		burger.letters.com - - [01/JUL/1995:00:00:12 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 0
		d104.aa.net - - [01/JUL/1995:00:00:13 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985 
		unicomp6.unicompt.net - - [01/JUL/1995:00:00:14 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 40310 
		unicomp6.unicompt.net - - [01/JUL/1995:00:00:14 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 786 
		unicomp6.unicompt.net - - [01/JUL/1995:00:00:14 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 1204 
		d104.aa.net - - [01/JUL/1995:00:00:15 - 0400] "GET /shuttle/countdown/ HTTP/1.0" 200 40310 
		d104.aa.net - - [01/JUL/1995:00:00:15 - 0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786 


## 2. Missing Words
-----
Given two strings, one is a subsequence if all of the elements of the first string occur in the same order within the second string.  
They do not have to be contiguous in the second string, but order must be maintained.  
For example, given the string "I like cheese", the words "I" and "cheese" are one possible subsequence of that string.

In this challenge, you will be given two strings, `s` and `t`, where `t` is a subsequence of `s`, report the words of `s`, missing in `t`, in order they are missing.  
Revisiting the earlier example, if `s = I like cheese` and `t = like`, then like is the longest subsequence, and `[I, cheese]` is the list of missing words in order.   

		
Function Description:
Complete the function `missingWords` in the editor below.   
It must return an array of strings containing any words in `s` that are missing from `t` in the order they occur within `s`.

`missingWords` has the following parameter(s):      
   s: a sentence of space separated words
   t: a sentence of space separated words
   
Constraints:  
 - Strings `s` and `t` consists of English alphabetic letters and spaces only. 
 - 1 <= |t| < |s| 10^6
 - 1 <= length of any word in `s` or `t` <= 15
 - It is guaranteed that string `t` is a subsequence of string `s`.
 
Input Format:
Input from stdin will be processes as follows and passed to the function
The first line contains a string `s`.
The second line contains a string `t`.

	Sample Input 0:
	I am using HackerRank to improve programming
	am HackerRank to improve
	
	Sample Output 0:
	I
	using
	programming
	
	Explanation 0:
	The missing words are:
	1. I
	2. using
	3. programming
	
	We add these words in order to the array ["I", "using", "programming"], then return this array as our answer. 
	
	Sample Input 1:
	I love programming
	programming
	
	Sample Output 1:
	I
	love
	
	Explanation 1:
	The missing words are:
	1. I
	2. love
	
	We add these words in order to the array ["I", "love"], then return this array as our answer. 
	
