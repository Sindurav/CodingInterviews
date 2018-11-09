# Technical Phone Interview

## 1. Technical Questions
-----
- What is deadlock
- What can you not do with a class with private constructor
- What is finally block
- How does hashmap work
- What should be a concerns when you are designing the hashmap
- Differnce between deep copy and shallow copy


## 2. Coding and Debugging Round
-----

### 1. Debug Hash function
--------------------------
What is wrong in the below code
	public override int GetHashCode(List<string> listA, bool isA){

			return IsA.GetHashCode()*31 + listA.GetHashCode();
	}



### 2. Is the String Duplicate?
--------------------------
- Write a function to see if there is any duplicate character in the string.     
- The function should have a time complexity of O(n) and space complexity of O(1).    
	 


### 3. What's Wrong in Parallel Computing
--------------------------
- `ConcurrentDictionary` is a Dictionary which is thread safe.
- `DoCompute` function is costly.
- What is wrong in the below code when multiple threads execute `Compute` function at the same time:

		
	ConcurrentDictionary<ComputeParams, double> _resultCache = new ConcurrentDictionary<ComputeParams, double>();

	public double Compute(ComputeParams params){

		double result;
		if (_resultCache.TryGetValue(params, out result)) return result;
		var result = DoCompute(params);
		_resultCache[params] = result;
		return result;
	}

	double DoCompute(ComputeParams params){

			// calculate
	}
