"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

def combine(n, k):
	choices = [x for x in range(1, n + 1)]
	_set = set()
	out = []
	backtrack(out, _set, choices, k, [])
	return out

def backtrack(out, _set, choices, k, cur):
	if k == 0:
		if tuple(sorted(cur)) not in _set:
			out.append(cur)
			_set.add(tuple(cur))
	else:
		for i in range(len(choices)):
			backtrack(out, _set, choices[:i] + choices[i+1:], k - 1, cur + [choices[i]])


