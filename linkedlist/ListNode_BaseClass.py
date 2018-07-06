class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
    def append(self, node, newnode):
        node.next = newnode
