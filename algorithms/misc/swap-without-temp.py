# task: swap two integers without the use of a third temporary variable

def swap(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b
