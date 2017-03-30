# problem: https://www.hackerrank.com/challenges/funny-string

t = int(input().strip())
out_string = ""
for test in range(t):
    s = list(map(ord, list(input().strip())))
    f = list(reversed(s))
    for i in range(1, len(s)):
        if abs(s[i] - s[i - 1]) != abs(f[i] - f[i - 1]):
            out_string += "Not Funny\n"
            break
    else:
        out_string += "Funny\n"
print(out_string)
