def kSub(k, nums):
    bucket = []
    for i in xrange(k):
        bucket.append([])
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        bucket[curr_sum % k].append(i)
    print bucket
    total = 0
    for i in xrange(len(bucket)):
        if i == 0:
            total += (len(bucket[0]) * (len(bucket[i]) + 1)) / 2
        else:
            total += (len(bucket[i]) * (len(bucket[i]) - 1)) / 2
    return total


k1 = 5
nums1 = [5, 10, 11, 9, 5]
k2 = 3
nums2 = [1, 2, 3, 4, 1]
print kSub(k1, nums1)
print kSub(k2, nums2)
