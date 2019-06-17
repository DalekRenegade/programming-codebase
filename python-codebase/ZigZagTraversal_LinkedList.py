class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def printTree(node, traversalType='in'):
    traversal = []

    def traverseTree(node, traversalType='in'):
        if not node:
            return
        if traversalType == 'pre':
            traversal.append(node.value)
            traverseTree(node.left, traversalType)
            traverseTree(node.right, traversalType)
        elif traversalType == 'post':
            traverseTree(node.left, traversalType)
            traverseTree(node.right, traversalType)
            traversal.append(node.value)
        else:
            traverseTree(node.left, traversalType)
            traversal.append(node.value)
            traverseTree(node.right, traversalType)

    traverseTree(node, traversalType)
    print traversal


def createTree():
    n8, n9, n13, n11, n12 = Node(8), Node(9), Node(13), Node(11), Node(12)
    n10 = Node(10, right=n13)
    n4 = Node(4, n8, n9)
    n5 = Node(5, left=n10)
    n6 = Node(6, left=n11)
    n7 = Node(7, right=n12)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)
    return n1


def zigZagTraverse(node):
    ans = []
    parity = False
    ll = [node]
    while ll:
        for x in ll:
            ans.append(x.value)
        new_ll = []
        idx = len(ll) - 1
        while idx >= 0:
            if parity:
                if ll[idx].left:
                    new_ll.append(ll[idx].left)
                if ll[idx].right:
                    new_ll.append(ll[idx].right)
            else:
                if ll[idx].right:
                    new_ll.append(ll[idx].right)
                if ll[idx].left:
                    new_ll.append(ll[idx].left)
            idx -= 1
        ll = new_ll
        parity = not parity
    return ans


tree = createTree()
printTree(tree)
printTree(tree, 'pre')
printTree(tree, 'post')

print zigZagTraverse(tree)
