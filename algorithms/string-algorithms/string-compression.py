def compress(s):
    if not s:
        return s
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
