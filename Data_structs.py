from contextlib import nullcontext
from typing import Container

class DLL:
    class node:
        def __init__(self, val, next=None, prev=None) -> None:
            self.data= val
            self.next=next
            self.prev= prev

    def __init__(self, val, mult=False, next=None) -> None:
        self.len=0
        if not mult:
            self.head=self.node(val, next)
            self.tail=self.head
            self.len+=1
        else:
            self.head=self.node(val[0],next)
            self.tail=self.head
            self.len+=1
            self.push(val[1:], True)

    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail

    def length(self):
        return self.len
        
    def at(self, index):
        i=0
        curr=self.head
        while i !=index:
            curr=curr.next
            i+=1
        return curr
     
    def search(self, val, curr=None):
        if not curr:
            return self.search_util(val, self.head)
        else:
            return self.search_util(val, curr)
    
    def search_util(self, val, curr=None):
        if not curr: return None
        if curr.data==val:
            return curr
        else:
            return self.search(val, curr.next)
    
    def pop(self, ind=0):
        if ind==0:
            curr=self.head
            self.head=self.head.next
            self.head.prev=None
            self.len-=1
            return curr
        elif ind==len-1 or ind==-1:
            curr=self.tail
            self.tail=curr.prev
            self.tail.next=None
            self.len-=1
            return curr
        curr=self.at(ind)
        curr.next.prev=curr.prev
        curr.prev.next=curr.next
        self.len-=1
        return curr
    
    def insertAt(self, index, val, mult=False):
        if mult:
            idx=index
            for v in val:
                self.insertAt(idx, v)
                idx+=1
        else:
            curr=self.at(index-1)
            dest=curr.next
            curr.next=self.node(val)
            curr.next.next=dest
            self.len+=1

    def push(self, val=None, mult=False):
        if isinstance(val, list) and mult:
            for v in val:
                self.push(v)
        else:
            curr=self.node(val)
            curr.next=self.head
            self.head.prev=curr
            self.head=curr
            self.len+=1

    def append(self, val=None, mult=False):
        if mult:
            for v in val:
                self.append(v)
        else:
            self.tail.next=self.node(val)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
            self.len+=1
    
    def update(self, ind, val):
        curr=self.at(ind)
        curr.data=val
    
    def printDLL(self):
        curr=self.head
        print('[ ',end=''),
        while curr.next:
            print(curr.data,'<-> ', end='')
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

    def get_head(self):
        return self.head

    def get_tail(self):
        curr=self.head   
        while curr.next:
            curr= curr.next
        return curr 
    
    def length(self):
        i=1
        curr=self.head
        while curr.next:
            curr=curr.next
            i+=1
        return i

    def at(self, index):
        i=0
        curr=self.head
        while i !=index:
            curr=curr.next
            i+=1
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
    
    def search(self, val, curr=None):
        if not curr:
            return self.search_util(val, self.head)
        else:
            return self.search_util(val, curr)
    
    def search_util(self, val, curr=None):
        if not curr: return None
        if curr.data==val:
            return curr
        else:
            return self.search_util(val, curr.next)
                

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
                self.container.push(v)
        self.top=self.container.head
    
    def top(self):
        return self.top

    def push(self, val):
        self.container.push(val)
        self.top=self.container.head()
    
    def pop(self):
        ans= self.container.pop(0)
        self.top=self.container.head()
        return ans
    
    def print_stack(self):
        curr=self.container.head
        print('top to bottom:')
        while curr:
            print(curr.data)
            curr=curr.next
        

class Queue:
    def __init__(self, val=None, mult=False):
        if not mult:
            self.container=DLL(val,mult)
        else:
            self.container=DLL(val[0], False)
            self.container.append(val[1:], True)
        
    def enqueue(self, val, mult=False):
        self.container.append(val, mult)
    
    def dequeue(self):
        return self.container.pop()





mylist=DLL([5,6,34,23,53,121,23], mult=True)
mylist.insertAt(3,[1,2,3],True)
mylist.printDLL()
print(mylist.at(3).data)
