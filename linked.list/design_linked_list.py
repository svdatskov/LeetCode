class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def get(self, index: int) -> int:
        dummy = self.head
        counter = 0

        while dummy and counter < index:
            dummy = dummy.next
            counter += 1

        return dummy.val if counter == index and dummy else -1


    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            next_element = self.head
            self.head = self.ListNode(val, next_element)

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.tail = self.ListNode(val)
            self.head = self.tail
        else:
            new_node = self.ListNode(val)
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = self.head
        counter = 0

        while dummy and counter < index - 1:
            dummy = dummy.next
            counter += 1


        if counter == index - 1:
            next_element = dummy.next
            dummy.next = self.ListNode(val, next_element)

    def deleteAtIndex(self, index: int) -> None:
        dummy = self.head
        counter = 0

        while dummy.next and counter < index - 1:
            dummy = dummy.next
            counter += 1

        if dummy == self.head and not dummy.next:
            self.head = None
            self.tail = None
        else:
            dummy.next = dummy.next.next


list = MyLinkedList()

print(list.addAtHead(1))
print(list.addAtTail(3))
print(list.addAtIndex(1,2))
print(list.get(1))
print(list.deleteAtIndex(1))
print(list.get(1))

# print(list.addAtHead(1))
# print(list.deleteAtIndex(0))
# print(list.get(0))

