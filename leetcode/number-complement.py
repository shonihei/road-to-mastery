"""
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
"""

def findComplement(num):
    bits = bin(num)[2:]
    output = ""
    for bit in bits:
        if bit == "1":
            output += "0"
        else:
            output += "1"
    return int(output, 2)

print(findComplement(5))