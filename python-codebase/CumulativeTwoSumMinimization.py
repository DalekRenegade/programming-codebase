class Queue:
    def __init__(self, default=None):
        self.queue = default if default else []
        self.queue.sort()

    def add(self, elem):
        self.queue.append(elem)

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def sort(self):
        self.queue.sort()

    def hasElement(self):
        return True if self.queue else False


def cumulativeSumMinimize(arr):
    min_sum = 0
    arr_queue, buff = Queue(arr), Queue()

    while arr_queue.hasElement() or buff.hasElement():
        pair = []
        while len(pair) < 2:
            if arr_queue.hasElement() and buff.hasElement():
                if arr_queue.peek() < buff.peek():
                    pair.append(arr_queue.pop())
                else:
                    pair.append(buff.pop())
            elif arr_queue.hasElement():
                pair.append(arr_queue.pop())
            else:
                pair.append(buff.pop())
        pair_sum = sum(pair)
        if arr_queue.hasElement() or buff.hasElement():
            buff.add(pair_sum)
        min_sum += pair_sum
    return min_sum


list1 = [8, 20, 4, 2]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 6, 7, 15, 22, 39]
list4 = [-1, -2, -3, -4, -5]
print cumulativeSumMinimize(list1)
print cumulativeSumMinimize(list2)
print cumulativeSumMinimize(list3)
print cumulativeSumMinimize(list4)
