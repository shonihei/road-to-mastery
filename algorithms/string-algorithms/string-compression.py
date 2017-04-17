# task: compress a string 

def compress(s):
    # if length < 2 then no need to compress
    if len(s) <= 2:
        return s
    # compress and see if it gets shorter
    c = 0
    cc = s[0]
    out = ""
    for i in range(len(s)):
        if s[i] == cc:
            c += 1
        else:
            out += cc + str(c)
            c = 1
            cc = s[i]
    out += cc + str(c)
    if len(s) < len(out):
        return s
    return out

r = ""
for _ in range(int(input().strip())):
    r += compress(input().strip()) + "\n"
print(r)
