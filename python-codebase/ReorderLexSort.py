# Leetcode - 937


def reorderLexSort(orderList):
    def fnGetKey(order):
        id, meta = order.split(' ', 1)
        if meta[0].isalpha():
            return -1, meta, id
        else:
            return 1,

    return sorted(orderList, key=fnGetKey)


inputs = [
    ['zld 93 12', 'fp kindle book', '10a echo show', '17g 12 25 6', 'ab1 kindle book', '125 echo dot second gen'],
    ['a1 9 2 3 1', 'g1 act car', 'zo4 4 7', 'ab1 off key dog', 'a8 act zoo'],
    ['g1 act', 'a8 act aoo'],
    ["g1 act car","a8 act zoo"],
    ['l5sh 6 3869 08 1295', '16o 94884717383724 9', '43 490972281212 3 51', '9 ehyjki ngcoobi mi',
     '2epy 85881033085988', '7z fqkbxxqfks f y dg', '9h4p 5 791738 954209', 'p i hz uubk id s m l',
     'wd lfqgmu pvklkdp u', 'm4jl 225084707500464', '6np2 bqrrqt q vtap h', 'e mpgfn bfkylg zewmg',
     'ttzoz 035658365825 9', 'k5pkn 88312912782538', 'ry9 8231674347096 00', 'w 831 74626 07 353 9',
     'bxao armngjllmvqwn q', '0uoj 9 8896814034171', '0 81650258784962331', 't3df gjjn nxbrryos b'],
    ]


for input in inputs:
    output = (reorderLexSort(input))
    for word in output:
        print word
    print '-------------------------------------'
