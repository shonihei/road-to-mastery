"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6
LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
"""

def readBinaryWatch(num):
    return ["%d:%02d" % (h, m) for h in range(12) for m in range(60) if (bin(h)[2:] + bin(m)[2:]).count('1') == num]