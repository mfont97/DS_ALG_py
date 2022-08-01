from contextlib import nullcontext
from typing import Container

class DLL:
    class node:
        def __init__(self, val, next=None, prev=None) -> None:
            self.data= val
            self.next=next
            self.prev

    def __init__(self, val, mult=False, next=None) -> None:
        if not mult:
            self.head=self.node(val, next)
            self.tail=self.heead
        else:
            self.head=self.node(val[-1],next)
            self.tail=self.head
            for v in val[-2::-1]:
                self.push(v)

    def head(self):
        return self.head
    
    def tail(self):
        return self.tail

    def tail(self):
        curr=self.head()      
        while curr.next:
            curr= curr.next
        return curr 
    
    def len(self):
        i=1
        curr=self.head
        while curr.next:
            curr=curr.next
            i+=1
        return curr
        

    def at(self, index):
        i=0
        curr=self.head
        while i !=index:
            curr=curr.next
        return curr
    
    def insertAt(self, index, val, mult):
        if mult:
            curr=self.at(index-1)
            dest=curr.next
            for v in val:
                curr.next=self.node(v)
                curr=curr.next
            curr.next=dest
        else:
            curr=self.at(index-1)
            dest=curr.next
            curr.next=self.node(val)
            curr.next.next=dest
    
    def search(self, val):
        if not self: return None
        if self.data==val:
            return self
        else:
            return self.search(self.next, val)
    
                

    def pop(self, ind=0):
        if ind==0:
            curr=self.head
            self.head=self.head.next
            return curr
        curr=self.at(ind-1)
        next=curr.next
        curr.next=curr.next.next
        return next

    def push(self, val=None, mult=False):
        if isinstance(val, list) and mult:
            for v in val:
                self.push(v)
        else:
            curr=self.node(val)
            curr.next=self.head
            self.head=curr

    def update(self, ind, val):
        curr=self.at(ind)
        curr.data=val
    def append(self, val=None, mult=False):
        tail=self.tail()
        if mult:
            for v in val:
                tail.next=self.node(v)
                tail=tail.next
        else:
            tail.next=self.node(val)
            tail=tail.next
    
    def printLL(self):
        curr=self.head
        print('[ ',end=''),
        while curr.next:
            print(curr.data,'-> ', end='')
            curr=curr.next
        print(curr.data, ' ]')


class LL:
    class node:
        def __init__(self, val, next=None) -> None:
            self.data= val
            self.next=next

    def __init__(self, val, mult=False, next=None) -> None:
        if not mult:
            self.head=self.node(val, next)
        else:
            self.head=self.node(val[-1],next)
            for v in val[-2::-1]:
                self.push(v)

    def head(self):
        return self.head()

    def tail(self):
        curr=self.head()      
        while curr.next:
            curr= curr.next
        return curr 
    
    def len(self):
        i=1
        curr=self.head
        while curr.next:
            curr=curr.next
            i+=1
        return curr
        

    def at(self, index):
        i=0
        curr=self.head
        while i !=index:
            curr=curr.next
        return curr
    
    def insertAt(self, index, val, mult):
        if mult:
            curr=self.at(index-1)
            dest=curr.next
            for v in val:
                curr.next=self.node(v)
                curr=curr.next
            curr.next=dest
        else:
            curr=self.at(index-1)
            dest=curr.next
            curr.next=self.node(val)
            curr.next.next=dest
    
    def search(self, val):
        if not self: return None
        if self.data==val:
            return self
        else:
            return self.search(self.next, val)
    
                

    def pop(self, ind=0):
        if ind==0:
            curr=self.head
            self.head=self.head.next
            return curr
        curr=self.at(ind-1)
        next=curr.next
        curr.next=curr.next.next
        return next

    def push(self, val=None, mult=False):
        if isinstance(val, list) and mult:
            for v in val:
                self.push(v)
        else:
            curr=self.node(val)
            curr.next=self.head
            self.head=curr

    def update(self, ind, val):
        curr=self.at(ind)
        curr.data=val
    def append(self, val=None, mult=False):
        tail=self.tail()
        if mult:
            for v in val:
                tail.next=self.node(v)
                tail=tail.next
        else:
            tail.next=self.node(val)
            tail=tail.next
    
    def printLL(self):
        curr=self.head
        print('[ ',end=''),
        while curr.next:
            print(curr.data,'-> ', end='')
            curr=curr.next
        print(curr.data, ' ]')


class Stack:
    def __init__(self, val=None, mult=False):
        if not mult:
            self.container=LL(val,mult)
        else:
            self.container=LL(val[0])
            for v in val:
                self.push(v)
        self.top=self.container.head()
    
    def top(self):
        return self.top

    def push(self, val):
        self.container.push(val)
        self.top=self.container.head()
    
    def pop(self):
        ans= self.container.pop(0)
        self.top=self.container.head()
        return ans

class Queue:


mylist=LL([5,6,34,23,53,121,23], mult=True)
mylist.printLL()