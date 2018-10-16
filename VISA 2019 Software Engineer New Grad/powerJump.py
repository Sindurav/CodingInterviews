#
# Complete the 'powerJump' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING game as parameter.
#


def powerJump(game):
    # Write your code here
	last_value = game[-1]
		
	indices = []
    
    for i in range(len(game)):
        if game[i] == last_value:
		    indices.append(i)
    
	curPow = minPow = indices[0]+1
  
    for i in range(1, len(indices)):
	    idx = indices[i]
	    curPow = indices[i]-indices[i-1]
	    minPow = max(minPow, curPow)
 
    return minPow