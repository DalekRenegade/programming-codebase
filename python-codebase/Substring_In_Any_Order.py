def hasSubstring(long_str, short_str):
    num_offset, caps_offset, small_offset = 0, 10, 36
    num_beg, caps_beg, small_beg = 48, 65, 97
    flag = 0
    buff = [0] * 62
    for ch in short_str:
        ord_val = ord(ch)
        if ord_val >= small_beg:
            ord_val = ord_val - small_beg + small_offset
        elif ord_val >= caps_beg:
            ord_val = ord_val - caps_beg + caps_offset
        elif ord_val >= num_beg:
            ord_val = ord_val - num_beg + num_offset
        flag |= (1 << ord_val)
        buff[ord_val] += 1
    print flag


hasSubstring('abcddefggh', 'a')
