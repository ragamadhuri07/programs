# DLL insertion at begining
def insert_start(self):
    n=node(300)
    temp=self.head
    temp.prev=n
    n.next=temp
    self.head=n

# DLL insertion at last
def insert_end(self):
    n=node(300)
    temp=self.head
    while temp.next is not None:
        temp=temp.next
    temp.next=n
    n.prev=temp
#DLL insertion in position
def insert_pos(self,pos):
    n=node(300)
    temp=self.head
    for i in range(1,pos-1):
        temp=temp.next
    n.prev=temp
    n.next=temp.next
    temp.next.prev=n
    temp.next=n
