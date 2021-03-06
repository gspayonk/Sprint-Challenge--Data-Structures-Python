from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #initiating the ring, if not at capacity add to tail, checks for capacity and points to the next node if needed, we're also cheching to see where current is and if it's at the head
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            self.current.value = item
            if self.current.next == None:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            return
        else: 
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed

        list_buffer_contents = []
        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
