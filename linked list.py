class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def merge(self, list1, list2):

        head = None
        dummy = ListNode()

        head = dummy

        while list1 and list2:

            if list1.val > list2.val:   """ if we checked list1.val > list2.val the code will print all elements of list2.val (but it heavily depends on the values assigned in each list) to understand this,
            the code will check 1 and 1 from both list1 and list2; the if statement will be falsy and therefore it will move to the else statement where it appends '1' from list2, then in the second iteration
            it will check '1' and '3' from list2, if statement will again be falsy -> moves to else statement and appends 3, it will carry on until the loop is finished, now we only appended list2 only, the program
            moves to the second condition and appends all list1"""

            
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next
        
        if list1:
            head.next = list1
        else:
            head.next = list2

        return dummy.next


def build_linked_list(our_lists): """ this function's purpose is to take every element/value passed to it and pass it to the ListNode class """
    dummy = ListNode()
    tail = dummy  """ calling tail as head would be a bit misleading since it is tracking the growing end of the list, not the beginning """

    for value in our_lists:
        tail.next = ListNode(value)  """ tail here takes the value and pass it to listNode, so that val would be = to whatever value is; since we didn't pass anything to next it will be None as default """
        tail = tail.next  """ ofc we move tail's index by 1 """

    return dummy.next

def print_list(node):  """ we need this function because linked list is just a chain of separate object scattered into memory, we need to transfere it from object memory into a readable text """
    values = []
    while node:  """ we need to loop through every element inside node, the reason while loop is better then for loop here is because with for loop we have to use range() but we don't know how many elements are inside node """
        values.append(str(node.val))  """ we append them as str here because join() func only takes strings """
        node = node.next
    print(" -> ".join(values))

list1 = build_linked_list([1, 2, 3])
list2 = build_linked_list([1, 3, 4])

solution = Solution()

result = solution.merge(list1, list2)

print_list(result)
