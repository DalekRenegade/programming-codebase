gcd_map = {}


def generalizedGCD(num, arr):
    if num == 0:
        return 0
    i, res = 1, arr[0]
    while i < num:
        key = (res, arr[i]) if res < arr[i] else (arr[i], res)
        if key in gcd_map:
            res = gcd_map[key]
        else:
            res = twoNumbersGCD(res, arr[i])
            gcd_map[key] = res
        i += 1
    return res


def twoNumbersGCD(a, b):
    key = (a, b)
    while b > 0:
        a, b = b, a % b
    gcd_map[key] = a
    return a


list1 = [2, 4, 6, 8, 10]
list2 = [-60, -4, 40, 20]
list3 = [0, 0, 0]
list4 = [3, 5, 7, 11, 13, 17]
list5 = [30, 40, 60, 80]
print generalizedGCD(len(list1), list1)
print generalizedGCD(len(list2), list2)
print generalizedGCD(len(list3), list3)
print generalizedGCD(len(list4), list4)
print generalizedGCD(len(list5), list5)
