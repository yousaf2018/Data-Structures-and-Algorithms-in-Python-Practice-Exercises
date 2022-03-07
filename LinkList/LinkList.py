from ctypes import pointer
from email import header
from re import L, T
import re
from tkinter.tix import Tree
from Node import Node

class LinkList:
    def __init__(self):
        self.head = None
    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    def displayLinkedList(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
    def deleteNodeAtValue(self, data):
        if self.head is None:
            print("Sorry there is empty linked list")
            return
        if self.head.data == data and self.head.next is None:
            self.head = None
            print("Deletion successfull")
            return  
        if self.head.data == data and self.head.next != None:
            self.head = self.head.next
            print("Deletion successfull")
            return      
        temp = self.head
        while(True):
            if temp is None:
                print("No node is found for deletion")
                return
            if temp.next is None:
                print("No node is found for deletion")
                return 
            if temp.next.data == data:
                temp1 = temp
                temp2 = temp.next
                if temp2.next is None:
                    temp1.next = None
                    print("Deletion successfull")
                    return
                else:
                    temp2 = temp2.next 
                    temp1.next = temp2
                    print("Deletion successfull")
                    return
            temp = temp.next
    def deleteNodeAtPosition(self, position):
        if self.head is None:
            print("Sorry there is empty linked list")
            return
        if position == 0 and self.head.next is None:
            self.head = None
            print("Deletion successfull")
            return  
        if position == 0 and self.head.next != None:
            self.head = self.head.next
            print("Deletion successfull")
            return      
        temp = self.head
        counter = 0
        while(True):
            if temp is None:
                print("No node is found for deletion")
                return
            if temp.next is None:
                print("No node is found for deletion")
                return 
            if counter  == position - 1:
                temp1 = temp
                temp2 = temp.next
                if temp2.next is None:
                    temp1.next = None
                    print("Deletion successfull")
                    return
                else:
                    temp2 = temp2.next 
                    temp1.next = temp2
                    print("Deletion successfull")
                    return
            temp = temp.next
            counter += 1
    def lenUsingRecursive(self, list):
        if list is None:
            return 0
        return 1 + self.lenUsingRecursive(list.next)    
    def swapTwoNodes(self, Node1, Node2):
        list = self.head
        if list is None:
            print("No values in the link list")
        temp = list
        temp2 = list
        current1 = None
        previous1 = None
        while(temp != None):
            if temp.next.data == Node1:
                current1 = temp.next
                previous1 = temp
                break
            temp = temp.next          
            
        current2 = None
        previous2 = None
        while(temp2 != None):
            if temp2.next.data == Node2:
                current2 = temp2.next
                previous2 = temp2
                break
            temp2 = temp2.next 
        print("Current 1:>", current1.data)
        print("Previous 1:>", previous1.data)  
        print("Current 2:>", current2.data)
        print("Previous 2:>", previous2.data) 
    
    
        previous1.next = current2
        previous2.next = current1

    
        current1.next, current2.next = current2.next, current1.next
    def reverseLinkList(self):
        previous = None
        current = self.head
        while(current):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        print("Done with reverse link list")

    def reverseLinkListRecursive(self,current, previous):
        if not current:
            return previous
        next = current.next 
        current.next = previous
        current = next
        previous = current
        return self.reverseLinkListRecursive(current, previous)

list = LinkList()
list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.addNode(5)
list.addNode(6)
list.displayLinkedList()
list.head = list.reverseLinkListRecursive(list.head, None)
list.displayLinkedList()
