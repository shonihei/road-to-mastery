"""
[UNFINISHED]

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

def canJump(nums):
	pos = 0
	while True:
		if pos >= len(nums) - 1 or pos + nums[pos] >= len(nums) - 1:
			return True
		elif nums[pos] == 0:
			return False
		else:
			max_dist = 0
			next_pos = pos
			for i in range(pos + 1, pos + 1 + nums[pos]):
				try:
					if nums[i] >= max_dist:
						max_dist = nums[i]
						next_pos = i
				except IndexError:
					return True
			if max_dist == 0:
				pos += nums[pos]
			else:
				pos = next_pos

if __name__ == "__main__":
	import unittest

	class Test(unittest.TestCase):
		def test1(self):
			self.assertTrue(canJump([2, 3, 1, 1, 4]))
		
		def test2(self):
			self.assertTrue(canJump([2, 3, 0, 0, 0]))
		
		def test3(self):
			self.assertTrue(canJump([0]))
		
		def test4(self):
			self.assertTrue(canJump([5,9,3,2,1,0,2,3,3,1,0,0]))

	unittest.main()
