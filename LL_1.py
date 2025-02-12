class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

linkedList_1 = LinkedList()

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.append(6)

# print( my_linked_list.find_middle_node().value )
while True:
    users_value = input("Enter a value: ")
    if users_value == "":
        break
    try:
        numeric_value = int(users_value)
        linkedList_1.append(numeric_value)
    except ValueError:
        print("Please enter a valid number.")

print(linkedList_1.find_middle_node().value )
