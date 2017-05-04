# task: implement a binary interpreter using two's complement

def convert_to_twos_complement(b, num_bits):
    return b - (1 << num_bits)
