def numberOfPairs(a, k):
    i, count, a_size = 0, 0, len(a)
    pair_dict = {}
    for ele in a:
        key = min(ele, k - ele)
        if key not in pair_dict:
            pair_dict[key] = ele
        elif pair_dict[key] + ele == k:
            pair_dict[key] += ele
            count += 1
    print pair_dict
    return count


a1 = [1, 2, 3, 6, 7, 8, 9, 1]
s1 = 10
a2 = [1, 3, 46, 1, 3, 9]
s2 = 47
a3 = [6, 6, 3, 9, 3, 5, 1]
s3 = 12
print numberOfPairs(a1, s1)
print numberOfPairs(a2, s2)
print numberOfPairs(a3, s3)
