# Got these problems in HACKERRANK challenge


## 1. Validate JSON
-----
Your job is to determine if an input string is valid JSON.  
An easy resource for understanding JSON is here: http://www.json.org/   

Your requirements:
  - Determine if the input string is valid JSON.   
  - Return "true" if it is valid. Return "false" if it is not.   
  
Example:  

If you are given the following input data:   
`{"test": "Hello World"}`


The output will be:   
`true`

On the other hand, if you are given the following input data:    
`{"test": Hello World"}`

The output will be:   
`false`



## 2. HTML Entity Codes
-----

## Background
When working with item like HTML and XML, you often want to use replacements for normal characters.   
In HTML, these are often called referenced "entities".   


## Problem
You will need to do a limited version of character replacement.   
Specifically, you need to find these characters in an input string:    
	
	 - "<"     
	 - ">"    
	 - "&"    

and replace them with:     

	 - "&lt;"     
	 - "&gt;"     
	 - "&amp;"    

## Example

For example, if you are given this string:   
`Hello <World> Goodbye & World`      
The output would be:     
`Hello &lt; World &gt; Goodbye &amp; World`  


## Considerations

 - Replace all of the characters
 - Your code should be able to handle Unicode characters (i.e., non-English)


## 3. Wikipedia Article
-----

In this challenge, use an **HTTP GET** method to retrieve information from Wikipedia.  
Query https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic] to get the topic Wikipedia article.  
Return the total number of times that the string [topic] appears in the article's text field.   
Note that the search is case-sensitive.  

The query response from the website is a JSON object described below:  
  - parse: A JSON object representing the article's parsed web page. It has following three fields:
	1. title: The article's title, as specified by the argument passed as topic.
	2. pageid: The article's Page ID.
	3. text: A JSON object that contains the Wikipedia article as an HMTL dump.
	
**Function Description:**     

Complete the function `getTopicCount` in the editor below.  
The function must return an integer, the number of times the search term topic appears in the returned text field.
	
`getTopicCount` has the following parameter(s):     
	topic: a string to query
	
	
[image0]: ./images/Wikipedia.JPG "Wikipedia"
![Wikipedia][image0]
	

## 4. Loading a web page
-----

Imagine you just purchased a new computer, and you've opened up a web browser for the first time.  
You go to the address bar type in:
`https://example.org`

Describe what happens between the moment you press the `Enter` key when the page has finished loading in the browser.  

Note: this is an open-ended question. You will need to decide the level of detail you want to include.  


	Ans: 
	- When the user hits enter, the browser looks in the cache whether the corresponding IP address is present or not.
	- If the IP is present in the browser cache then it renders the page from the cache.
	- If IP is not present in the browser cache then it will try to find the IP for the corresponding URL in the DNS server.
	- Once the browser gets the IP from DNS server, it will establish a connection and send the HTTP request to the server with that IP.
	- The server will serve the browser by checking the URL and responding with HTTP response.
	- The browser receives the HTTP response which is usually an HTML page which browser then renders the response in the window. 

	
## 5. Complexity of the Code Snippet
-----

Consider the following code snippet:

		int a = 1;
		while (a<n){
			a = a * 2
		}

What is complexity of the above code snippet:      

**Pick one of the choices**     
	 - O(n)     
	 - O(1)     
	 - O(log(n))     
	 - O(2^n)      

**The correct answer is O(log(n)).**
	 
	 
## 6. Number of Paths in a Matrix
-----

Consider a maze mapped to a matrix with an upper left corner at coordinates `(row, column) = (0, 0)`.   
Any movement must be in increasing row or column direction.  
Determine the number of distinct paths through the maze.  
Always start at position `(0, 0)`, the top left, and end up at `(max(row), max(column))`, the bottom right.   


**Function Description:**   
Complete the function `numberOfPaths` in the editor below.   
The function must return the number of paths through the matrix modulo `(10^9+7)`.   

`numberOfPaths` has the following parameter(s):     
a[a[0], ...., a[n-1]]: an array of strings, each a row of the matrix where each character represents a column.   


**Constraints:**
   - 1 <= n, m <= 1000
   - Each cell in matrix a contains either a 0 or a 1. 
   
**Input Format for Custom Testing:**    
Input from stdin will be a processed as follows and passed to the function.
The first line contains an integer `n`, the number of rows in a matrix `a`.
The next line contains an integer `m`, the number of columns in matrix `a`.
The next `n` lines each contain a string `a[i]` where 0 <= i < n and |a[i]| = m. 



	Sample Case 0 
	Sample Input 0
	3
	4
	1 1 1 1
	1 1 1 1
	1 1 1 1
	
	Sample Output 0 
	10
	
	Explanation 0
[image1]: ./images/Q6E1.JPG "Q6E1"
![Q6E1][image1]
	
	Sample Case 1 
	Sample Input 1
	2
	2
	1 1
	0 1
	
	Sample Output 1 
	1
	
	Explanation 1
[image2]: ./images/Q6E2.JPG "Q6E2"
![Q6E2][image2]
	
