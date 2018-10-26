# Got these problems in HACKERRANK challenge


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

