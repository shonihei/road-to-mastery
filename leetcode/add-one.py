"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

Unfinished
"""

def plusOne(digits):
    digits[-1] += 1
    if digits[-1] >= 10:
        digits[-1] = digits[-1] % 10
        carry = True
        i = len(digits) - 2
        if i < 0:
            digits.insert(0, 1)
            return digits
        while i >= 0 and carry:
            num = digits[i]
            new_num = num + 1
            if new_num >= 10:
                new_num = new_num % 10
                digits[i] = new_num
                if i == 0:
                    digits.insert(0, 1)
                    return digits
            else:
                carry = False
        return digits
    else:
        return digits

print(plusOne([9]))
