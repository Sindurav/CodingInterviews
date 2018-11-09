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

	public override int GetHashCode(List<string> listA, bool isA){

			return IsA.GetHashCode()*31 + listA.GetHashCode();
	}


	def is_duplicate(input_string):
		If len(input_string)>256:
			return True
		flags  = [False]*256
		for char in input_string:
			If flags[ord(char)] == False:
				flags[ord(char)] = True
			else:
				return True
		return False

		
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
