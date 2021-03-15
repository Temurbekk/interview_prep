import random
import os
import sys
utils_path = os.path.join('..', '..', '..', '..',
                          'problems', 'utils', 'python')
sys.path.append(utils_path)


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.arbitrary = None


def insert_at_head(head, data):
    newNode = LinkedListNode(data)
    newNode.next = head
    return newNode


def insert_at_tail(head, node):
    if head is None:
        return node

    temp = head

    while temp.next != None:
        temp = temp.next

    temp.next = node
    return head


def create_random_list(length):
    list_head = None
    for i in range(0, length):
        list_head = insert_at_head(list_head, random.randrange(1, 100))
    return list_head


def create_linked_list(lst):
    list_head = None
    for x in reversed(lst):
        list_head = insert_at_head(list_head, x)
    return list_head


def display(head):
    temp = head
    while temp:
        print(str(temp.data), end="")
        temp = temp.next
        if temp != None:
            print(", ", end="")


def to_list(head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.data)
        temp = temp.next
    return lst


def is_equal(list1, list2):
    if list1 is list2:
        return True

    while list1 != None and list2 != None:
        if list1.data != list2.data:
            return False
        list1 = list1.next
        list2 = list2.next

    return list1 == list2
