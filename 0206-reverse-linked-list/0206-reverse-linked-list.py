# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        l = head
        a = []
        while head!= None:
            a.append(head.val)
            head = head.next
        left = 0
        right = len(a)-1
        while left<right:
            a[left] , a[right] = a[right], a[left]
            left += 1
            right -= 1
        print(a)
        head = l
        i = 0
        while head!= None:
            head.val = a[i]
            i += 1
            head = head.next
        head = l
        return head


