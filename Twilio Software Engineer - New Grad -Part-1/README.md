# Got these problems in HACKERRANK challenge

- I was given 45 minutes to solve the two questions.    


## 1. Reformatting Dates
-----
Given a date string in the format Day Month Year where:

Day is in set {"1st", "2nd", "3rd", "4th", "5th", "6th", .... , "31st"}.   

Month is in set {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep" , "Oct" , "Nov", "Dec"}.   
				 
Year is in the inclusive range [1900, 2100]

For Example:  
- "1st Mar 1984" -> "1984-03-01"
- "2nd Feb 2013" -> "2013-02-02"
- "4th Apr 1990" -> "1990-04-04"  


Function Description:
Complete the function `reformateDate` in the editor below.  
The function must return an array of converted date strings in the order presented.  
 
`reformateDate` has the following parameter(s):
- dates[dates[0], ..., dates[n-1]]: an array of date strings in the format Day Month Year
  
  
Constraints:  
 - The values of Day, Month, Year are restricted to the value ranges specified above.  
 - The given dates are guaranteed to be valid so no error handling is necessary. 
 - 1 <= n <= 10000  
 
		Sample Input 0:
		10
		20th Oct 2052
		6th Jun 1933
		26th May 1960
		20th Sep 1958
		16th Mar 2068
		25th May 1912
		16th Dec 2018
		26th Dec 2061
		4th Nov 2030
		28th Jul 1963
		
		Sample Output 0:
		2052-10-20
		1933-06-06
		1960-05-26
		1958-09-20
		2068-03-16
		1912-05-25
		2018-12-16
		2061-12-26
		2030-11-04
		1963-07-28
		


## 2. Hosts and Total Number of Requests
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