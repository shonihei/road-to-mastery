"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
"""

def compress(chars):
	"""
	:type chars: List[str]
	:rtype: int
	"""
	left = i = 0
	while i < len(chars):
		char, length = chars[i], 1
		while (i + 1) < len(chars) and char == chars[i + 1]:
			length, i = length + 1, i + 1
		chars[left] = char
		if length > 1:
			len_str = str(length)
			chars[left + 1:left + 1 + len(len_str)] = len_str
			left += len(len_str)
		left, i = left + 1, i + 1
	return left