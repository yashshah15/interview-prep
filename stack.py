class node():
    def __init__(self,value):
        self.data=value
        self.next=None

class stack():
    def __init__(self):
        self.top=None
    def insert(self,value):
        nn=node(value)
        if self.top is None:
            self.top=nn
        else:
            nn.next=self.top
            self.top=nn
    def delete(self):
        if self.top is None:
            print("Stack Empty")
        else:
            self.top=self.top.next
    def display(self):
        ptr= self.top
        while(ptr):
            print(ptr.data)
            ptr=ptr.next

s=stack()
ch=1
while ch:
    print("1. Insert")
    print("2. Delete")
    print("0.exit")
    ch=int(input("Enter choice"))
    if ch is 1:
        s.insert(int(input("Enter value to be inserted")))
        s.display()
    if ch is 2:
        s.delete()
        s.display()
    if ch is 0:
        break