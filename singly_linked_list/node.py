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

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        current_1 = self.head
        while current_1 and current_1.data != key_1:
            prev_1 = current_1
            current_1 = current_1.next

        prev_2 = None
        current_2 = self.head
        while current_2 and current_2.data != key_2:
            prev_2 = current_2
            current_2 = current_2.next

        if not current_1 or not current_2:
            return

        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2

        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1

        current_1.next, current_2.next = current_2.next, current_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next

        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev
            q.next = self.head
            self.head = p.next
            p.next = None


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.rotate(2)
llist.print_list()
