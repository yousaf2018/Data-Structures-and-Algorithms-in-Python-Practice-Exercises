# Implementation of stack data structure
class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def checkStack(self):
        return self.items == []
    def getPeek(self):
        if self.items == []:
            return -1
        else:
            return self.items[-1]
    def displayStack(self):
        if self.items == []:
            print("Stack is empty")
        else:
            for i in range(len(self.items)-1,-1,-1):
                print(self.items[i])
    def getStack(self):
        return self.items