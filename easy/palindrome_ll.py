"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        # O(1) space and (n) time SOLUTION
        # PSEUDOCODE
        # Find the end of the first half.
        # Reverse the second half.
        # Determine whether or not there is a palindrome.
        # Restore the list.
        # Return the result.


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
# O(n) time and space SOLUTION
    #     arr = []
    #     while head is not None: # O(n)
    #         arr.append(head.val)
    #         head = head.next
        
    #     return self.isPalArr(arr)
        
    # def isPalArr(self, array):
    #     start, end = 0, len(array) - 1
        
    #     while start <= end: # O(n)
    #         if array[start] != array[end]:
    #             return False
    #         start += 1
    #         end -= 1
    #     return True
