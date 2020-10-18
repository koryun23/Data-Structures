import unittest
class LinkedList:
    def __init__(self, value):
        self.length = 1
        self.length_name = 'length'
        self.head = {
            'value':value,
            'next':None
        }
        self.head_name = 'head'
        self.tail = self.head
        self.tail_name = 'tail'
    def create(self):
        self.myLinkedList = {
            'length': self.length,
            'head': self.head,
            'tail': self.tail,
        }
        return self.myLinkedList
    def printList(self):
        values = []
        curNode = self.head
        while curNode != None:
            values.append(curNode['value'])
            curNode = curNode['next']
        return values
    def append(self, value):
        self.node = {
            'value' : value,
            'next' : None
        }
        self.tail['next'] = self.node
        self.tail = self.node
        self.length += 1
        return self.create()
    def prepend(self, value):
        self.node = {
            'value' : value,
            'next' : None
        }
        self.node['next'] = self.head
        self.head = self.node
        self.length += 1
        return self.create()
    def insert(self, index, value):
        i = 0
        curNode = self.head
        if index <= 0 or index >= self.length:
            error_message = 'enter a number between 0 and %s' % (self.length-1)
            return error_message
        while i < index:
            i+= 1
            curNode = curNode['next']
            if i == index-1:
                node = {
                    'value':value,
                    'next': None
                }
                node['next'] = curNode['next']
                curNode['next'] = node    
                self.length += 1
                i+= 1
        return self.create()
    def remove(self, index):
        if index == 0:
            self.head = self.head['next']
            self.length -= 1

        elif index < 0 or index >self.length-1:
            error_message = 'enter a number between 0 and %s' % (self.length-1)
            return error_message
        else:
            i = 0
            curNode = self.head
            while i <= index:
                curNode = curNode['next']
                i += 1
                if i == index - 1:
                    prevNode = curNode
                elif i == index:
                    node = curNode
            
            prevNode['next'] = node['next']
            node = node['next']
            
            self.length -= 1
           
        return self.create()
    def delete_by_value(self, value):
        prevNode = self.head
        curNode = prevNode['next']
        while True:
            if self.head['value'] == value:
                self.head = self.head['next']
                self.length -= 1
                break
            else:
                if curNode['value'] == value:
                    prevNode['next'] = curNode['next']
                    curNode = curNode['next']
                    self.length -= 1
                    break
                else:
                    prevNode = curNode
                    curNode = curNode['next']
        return self.create()
                
                     






                
            
        

        
        
        
    

linked_list = LinkedList(10)
ll = LinkedList(10)
print(linked_list.create())
print(ll.append(5))
print(ll.append(16))
print(ll.prepend(1))
print(ll.printList())
print(ll.insert(2, 2))
print(ll.printList())
print(ll.insert(4, 111))
print(ll.printList())
print(ll.insert(5, 114))
print(ll.printList())
print(ll.remove(0))
print(ll.printList())
print(ll.remove(5))
print(ll.printList())
print(ll.remove(2))
print(ll.printList())
print(ll.delete_by_value(114))
print(ll.printList())








        