"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

def plusOne(digits):
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	i = len(digits) - 1
	while i >= 0:
		digit = digits[i]
		new_digit = digit + 1
		if new_digit <= 9:
			digits[i] += 1
			return digits
		else:
			digits[i] = new_digit % 10
		i -= 1
	return [1] + digits