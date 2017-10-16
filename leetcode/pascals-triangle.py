"""
Given numRows, generate the first numRows of Pascal's triangle.
"""

def generate(numRows):
    if numRows < 1:
        return []
    else:
        out = [[1]]
        i = 0
        while len(out) != numRows:
            j = 0
            k = j - 1
            row = []
            while k < len(out[i]):
                if k < 0:
                    row.append(1)
                elif j >= len(out[i]):
                    row.append(1)
                else:
                    row.append(out[i][k] + out[i][j])
                k += 1
                j += 1
            i += 1
            out.append(row)
    return out
