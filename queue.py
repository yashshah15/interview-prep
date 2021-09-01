class node():
    def __init__(self,value):
        self.data=value
        self.next=None

class queue():
    def __init__(self):
        self.front=None
        self.rear=None
    def insert(self,value):
        nn=node(value)
        if self.front==None and self.rear==None:
            self.rear=nn
            self.front=nn
        else:
            self.rear.next=nn
            self.rear=nn
    def delete(self):
        if self.front==None:
            print("Queue empty")
        elif self.front==self.rear:
            self.rear=None
            self.front=None
        else:
            self.front=self.front.next
    def display(self):
        ptr=self.front
        while ptr:
            print(ptr.data)
            ptr=ptr.next

q=queue()
ch=1
while ch:
    print("1. Insert")
    print("2. Delete")
    print("0.exit")
    ch=int(input("Enter choice"))
    if ch is 1:
        q.insert(int(input("Enter value to be inserted")))
        q.display()
    if ch is 2:
        q.delete()
        q.display()
    if ch is 0:
        break
