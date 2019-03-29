def cellComplete(state, days):
    i, l = 0, len(state)
    temp = [False] * l
    while i < l:
        temp[i] = state[i]
        i += 1
    while days > 0:
        temp[0] = state[1] ^ False
        temp[l - 1] = state[l - 2] ^ False
        j = 1
        while j < (l - 2 + 1):
            temp[j] = state[j - 1] ^ state[j + 1]
            j += 1
        j = 0
        while j < l:
            state[j] = temp[j]
            j += 1
        days -= 1
    return state


arr1 = [1, 0, 0, 0, 0, 1, 0, 0]
day1 = 1
arr2 = [1, 1, 1, 0, 1, 1, 1, 1]
day2 = 2
print cellComplete(arr1, day1)
print cellComplete(arr2, day2)
