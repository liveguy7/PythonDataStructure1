import sys

class Node1:

    def __init__(self, data=None):
        self.data = data
        self.next1 = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self,data):
        node = Node1(data)
        if(self.tail):
            self.tail.next1 = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count = self.count + 1

    def search(self,val):
        for node in self.iterate_item():
            if(val == node):
                return True
        return False

    def __getitem__(self,index):
        if(index > self.count - 1):
            return "Index Out of Range"
        curr_val = self.tail
        for n in range(index):
            curr_val = curr_val.next1
        return curr_val.data

    def __setitem__(self,index,value):
        if(index > self.count - 1):
            raise Exception("Index Out of Range")
        current = self.tail
        for n in range(index):
            current = current.next
        current.data = value

    def delete_item(self,data):
        current = self.tail
        prev = self.tail
        while current:
            if(current.data == data):
                if(current == self.tail):
                    self.tail = current.next1
                else:
                    prev.next = current.next1
                self.count = self.count - 1
                return
            prev = current
            current = current.next1

    def iterate_item(self):
        current_item = self.head
        while(current_item):
            val = current_item.data
            current_item = current_item.next1
            yield val


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if(self.head is None):
            print("Linked List is Empty")
            return
        itr = self.head
        llstr = ''
        while(itr):
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data,None)
            return
        itr = self.head
        while(itr.next):
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while(itr):
            count = count + 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if(index < 0 or index >= self.get_length()):
            raise Exception("Invalid Index")
        if(index == 0):
            self.head = self.head.next
            return


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes",'orange'])
    ll.insert_at_beginning(90)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(50)
    ll.insert_at_end(100)
    ll.insert_at_beginning(1)
    ll.print()
    len1= ll.get_length()
    print("The length is {0}".format(len1))
    ptr = SLinkedList()
    ptr.append_item("A")
    ptr.append_item("B")
    ptr.append_item("C")
    ptr.append_item("E")
    ptr.append_item("X")
    ptr.append_item("Y")
    ptr.append_item("Z")
    ptr.append_item("F")
    for val in ptr.iterate_item():
        print(val,end=' ')
    ptr.delete_item("F")
    print()
    for val in ptr.iterate_item():
        print(val, end=' ')
    print()









