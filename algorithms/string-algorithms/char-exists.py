# task: given a string and a character, write an algorithm to construct another string that
#       consists of 1s and 0s where 1 corresponds to the location where a given character
#       appeared in a string

def char_count(s, c):
    o = ""
    for char in s:
        if char == c:
            o += "1"
        else:
            o += "0"
    return o

def main():
    print(char_count("helloworld", "l"))
    print(char_count("aaabbabaccc", "a"))

if __name__ == "__main__":
    main()
