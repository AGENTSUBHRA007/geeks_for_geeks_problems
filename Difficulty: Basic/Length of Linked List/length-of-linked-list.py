''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        n=0
        curr=head
        if curr is None:
            return 1
        while curr is not None:
            curr=curr.next
            n+=1
        return n