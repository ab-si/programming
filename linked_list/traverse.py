#!/bin/python3

'''
Given a pointer to the head node of a linked list, print its elements in order,
one element per line.
If the head pointer is null (indicating the list is empty), don’t print anything
'''

import os

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_list2(head):
    while(head):
        print(head.data)
        head = head.next
    
def print_list(head):
    if head is not None:
        print(head.data)
        print_list(head.next)

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    print_list(llist.head)
    print_list2(llist.head)