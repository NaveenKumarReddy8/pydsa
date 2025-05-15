# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverse(self, linked_list: ListNode):
        result = []
        current = linked_list
        while True:
            result.append(current.val)
            if current.next is None:
                break
            current = current.next
        return result

    def build(self, values: list[int]):
        head = ListNode(val=values[0])
        current = head
        for value in values[1:]:
            new_node = ListNode(val=value)
            current.next = new_node
            current = new_node
        return head

    def reverse_the_list_elements_and_typecast(self, values: list[int]) -> int:
        return int(("".join([str(obj) for obj in values]))[::-1])

    def addTwoNumbers(
        self, l1: None | ListNode, l2: None | ListNode
    ) -> None | ListNode:
        t1 = self.traverse(l1)
        t2 = self.traverse(l2)

        v1 = self.reverse_the_list_elements_and_typecast(t1)
        v2 = self.reverse_the_list_elements_and_typecast(t2)

        total = v1 + v2

        reverse_of_total_str = str(total)[::-1]
        return self.build([int(obj) for obj in reverse_of_total_str])

