# task: given a string, replace all white spaces with '%20'

def urlify(s):
    out = ""
    for c in s:
        if c == " ":
            out += "%20"
        else:
            out += c
    return out

A = "hello my name is    sho"
print(urlify(A))
