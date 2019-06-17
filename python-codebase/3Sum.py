def threeSum(nums, target_sum=0):
    triplets = set()
    if not nums:
        return triplets
    nums.sort()
    if nums[0] > target_sum or nums[-1] < target_sum:
        return triplets
    i, j = 0, len(nums) - 1
    i_flag, j_flag = False, False
    while i < j:
        complement = target_sum - (nums[i] + nums[j])
        k = i + 1
        while k < j:
            if complement == nums[k]:
                break
            k += 1
        if k < j:
            triplets.add((nums[i], complement, nums[j]))
        if i_flag:
            i_flag = False
            j_flag = True
            i -= 1
            j -= 1
        elif j_flag:
            j_flag = False
            i += 1
        elif complement > target_sum:
            i += 1
        elif complement < target_sum:
            j -= 1
        else:
            i_flag, j_flag = True, False
            i += 1
    return [list(elem) for elem in triplets]


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-2, 0, 1, 1, 2]
nums3 = [-2, -1, -1, 0, 1, 1, 2]
nums4 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
print threeSum(nums1)
print threeSum(nums2)
print threeSum(nums3)
print threeSum(nums4)
