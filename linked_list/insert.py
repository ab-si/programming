class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def push_at_end(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def push_at_pos(self, data, val):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
            return
        temp = self.head
        while temp.next:
            if temp.data == val:
                break
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def print_middle(self):
        pass

if __name__ == "__main__":
    llist = LinkedList()
    llist.push_at_start(1)
    llist.push_at_start(2)
    llist.push_at_start(3)
    llist.push_at_end(2)
    llist.push_at_end(3)
    llist.push_at_pos(0, 1)
    llist.print_list()