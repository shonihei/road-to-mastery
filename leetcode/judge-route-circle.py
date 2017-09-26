"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false
representing whether the robot makes a circle.
"""

def judgeCircle(moves):
    pos = [0, 0]

    for move in moves:
        if move == "U":
            pos[1] += 1
        elif move == "D":
            pos[1] -= 1
        elif move == "L":
            pos[0] -= 1
        else:
            pos[0] += 1
    if pos[0] == 0 and pos[1] == 0:
        return True
    return False

print(judgeCircle("UD"))