# Linked List class Implementation

class Node:
    """
    Class that implements a node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        """
        Determines the way that a Node will print
        """
        return str(self.data)


class LinkedList:
    """
    Class that implements a linked list
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """
        Determines the way that the whole LinkedList will print
        :return: str_l that models all the components of the linked list: "node1 -> node2 -> node3"
        """
        temp = self.head
        str_l = ""
        while temp.next:
            str_l = str_l + str(temp)
            str_l = str_l + " -> "
            temp = temp.next
        str_l = str_l + str(temp)
        return str_l

    def append(self, new_data):
        """
        Appends data to the linked list
        :param new_data: an int that wil be added to the linked list
        """
        new_node = Node(new_data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def merge(self, b):
        """
        Merges two linked lists
        :param b: linked list
        :return: the first LinkedList with the nodes of the second one
        """
        temp = b.head
        while temp:
            self.append(temp.data)
            temp = temp.next
        return self

    def sort(self):
        """
        Sorts the linked list
        """
        n1 = self.head
        while n1:
            n2 = n1.next
            while n2:
                if n2.data < n1.data:
                    n1.data, n2.data = n2.data, n1.data
                n2 = n2.next
            n1 = n1.next
