"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for
the multiples of five output “Buzz”. For numbers which are multiples of both
three and five output “FizzBuzz”.
"""

def fizzBuzz(n):
    out = []
    for num in range(1, n + 1):
        s = ""
        if num % 3 == 0:
            s += "Fizz"
        if num % 5 == 0:
            s += "Buzz"
        out.append(s if s else str(num))
    return out

print(fizzBuzz(15))