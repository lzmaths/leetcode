import sys

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        m = {}
        dummy_head = Node(0)
        tail = dummy_head
        curr = head
        while curr:
            node = Node(curr.val)
            tail.next, tail = node, node
            m[curr] = node
            m[node] = curr
            curr = curr.next
            
        curr = dummy_head.next
        while curr:
            if m[curr].random:
                curr.random = m[m[curr].random]
            curr = curr.next
        return dummy_head.next