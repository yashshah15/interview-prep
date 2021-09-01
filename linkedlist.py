class Node():
    def __init__(self,val):
        self.data=val
        self.next=None

class linkedList():
    def __init__(self):
        self.Head=None
    def insert(self,value):
        nn=Node(value)
        if self.Head:
            current=self.Head
            while(current):
                current=current.next
            current.next=nn
        else:
            self.Head=nn
    def delete(self,value):
        curr=self.Head
        prev=None
        if curr == None:
            print("Underflow")
        while curr != None and curr.data!=value:
            prev=curr
            curr=curr.next
        if curr ==None:
            print("Element not found")
        elif curr==self.Head:
            self.Head=curr.next
        else:
            prev.next=curr.next
    def display(self):
        ptr=self.Head
        while ptr:
            print(ptr.data," ",end="")
            ptr=ptr.next

ch=1
ll=linkedList()
while ch:
    print("1. Insert")
    print("2. Delete")
    print("0.exit")
    ch=int(input("Enter choice"))
    if ch is 1:
        ll.insert(int(input("Enter value to be inserted")))
        ll.display()
    if ch is 2:
        ll.delete(int(input("Enter value to be deleted")))
        ll.display()
    if ch is 0:
        break

