class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):  # insert an element at the beginning
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev node doesnt exist.")
            return
        # print(prev_node.next)

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:  # if is not first node
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            current_node = self.head
            if pos == 0:
                self.head = current_node.next
                current_node = None
                return
            prev = None
            count = 0
            while current_node and count != pos:
                prev = current_node
                current_node = current_node.next
                count += 1
            if current_node is None:
                return
            prev.next = current_node.next
            current_node = None

    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.append('F')
# llist.insert_after_node(llist.head.next, 'F')
# llist.delete_node('A')
# llist.delete_node('C')
# llist.delete_node_at_pos(3)
print(llist.len_iterative())
print('Recursive',llist.len_recursive(llist.head))
# llist.print_list()
