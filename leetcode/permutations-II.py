"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

def permuteUnique(nums):
	_set = set()
	lst = []
	backtrack(_set, lst, nums, [])
	return lst

def backtrack(_set, lst, choices, cur):
	if not choices and tuple(cur) not in _set:
		lst.append(cur)
		_set.add(tuple(cur))
	else:
		for i in range(len(choices)):
			backtrack(_set, lst, choices[:i] + choices[i+1:], cur + [choices[i]])
