class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    unique_elements = set()

    current_node = llist_1.head
    while current_node:
        unique_elements.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        unique_elements.add(current_node.value)
        current_node = current_node.next

    result_linked_list = LinkedList()
    for element in unique_elements:
        result_linked_list.append(element)

    return result_linked_list

def intersection(llist_1, llist_2):
    set_1 = set()
    set_2 = set()

    current_node = llist_1.head
    while current_node:
        set_1.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        set_2.add(current_node.value)
        current_node = current_node.next

    common_elements = set_1.intersection(set_2)

    if not common_elements:
        return None

    result_linked_list = LinkedList()
    for element in common_elements:
        result_linked_list.append(element)

    return result_linked_list

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print("Union", union(linked_list_1, linked_list_2)) 
print("Intersection", intersection(linked_list_1, linked_list_2))
print()
#returns Union 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
#returns Intersection 4 -> 21 -> 6 ->


linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union:", union(linked_list_3, linked_list_4))
print("Intersection:", intersection(linked_list_3, linked_list_4))
print()
#returns Union: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
#returns Intersection: None


linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [6, 6, 7, 7, 7, 7, 8, 8, 4]
element_2 = [55, 56, 67, 7, 8, 8]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Union:", union(linked_list_5, linked_list_6))
print("Intersection:", intersection(linked_list_5, linked_list_6))
print()
#returns Union: 67 -> 4 -> 6 -> 7 -> 8 -> 55 -> 56 ->
#returns Intersection: 8 -> 7 ->


linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [0, -10, 15, "string"]
element_2 = ["string", 40, 30]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("Union:", union(linked_list_7, linked_list_8))
print("Intersection:", intersection(linked_list_7, linked_list_8))
print()
#returns Union: 0 -> 40 -> 15 -> -10 -> string -> 30 ->
#returns Intersection: string ->

