import random
import string
import sys
from collections import OrderedDict


class Color:
    def __init__(self):
        pass

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Stream:
    def __init__(self, str_size=100):
        self.string = ''.join(random.choice(string.ascii_uppercase) for _ in range(str_size))
        self.index = 0

    def next(self):
        char = None
        if self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
        return char


def char2index(char, offset=65):
    return ord(char) - offset


def index2char(index, offset=65):
    return chr(index + offset)


def longestAlternatingSubsequence(stream_obj=None):
    index, input_range_length = 0, 26
    index_list = [-1] * input_range_length
    pair_map = OrderedDict()

    stream = stream_obj or Stream()
    char = stream.next()    # Accessing the next character from the stream
    while char:
        int_char = char2index(char)
        for k in range(input_range_length):
            if index_list[k] >= 0 and index_list[int_char] <= index_list[k] < index and int_char != k:
                key = index2char(k) + char
                if key not in pair_map:
                    pair_map[key] = 0
                pair_map[key] += 1
        index_list[int_char] = index
        index += 1
        char = stream.next()    # Accessing the next character from the stream

    longest_sequence = ''
    for pair, count in pair_map.items():
        sequence = pair * count
        pos_char1, pos_char2 = index_list[char2index(pair[0])], index_list[char2index(pair[1])]
        if pos_char1 > pos_char2:
            sequence += pair[0]
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    return longest_sequence


# print color.BOLD + 'Hello World !' + color.END
for i in range(10):
    new_stream = Stream(str_size=10 * (i + 1))
    longest_sub_sequence = longestAlternatingSubsequence(new_stream)
    subsequence_len = len(longest_sub_sequence)
    j = 0
    for c in new_stream.string:
        if j < subsequence_len and c == longest_sub_sequence[j]:
            sys.stdout.write(Color.RED + Color.UNDERLINE + Color.BOLD + c + Color.END)
            j += 1
        else:
            sys.stdout.write(c)
        sys.stdout.flush()
    print ' ==>', longest_sub_sequence, subsequence_len
