# double linked list insertion end

class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self):
        n=node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp   
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj=DLL()
n1=node(10)
obj.head=n1
n2=node(20)
n2.prev=n1
n1.next=n2
obj.display()
print()
obj.insert_end()
obj.display()
