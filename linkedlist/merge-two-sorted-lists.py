import ListNode_BaseClass as L

#L1,L2 - 2 sorted singly linked lists
#o/p - merged sorted linked list

def merge_two_sorted_lists( L1, L2):
    dummy_head = tail = L.ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next

L1 = L.ListNode(5)
L2 = L.ListNode(3,L1)

l1 = L.ListNode(4)
l2 = L.ListNode(2, l1)

res = head = merge_two_sorted_lists(L2,l2)
while head:
    print(head.data, end=" ")
    head = head.next
