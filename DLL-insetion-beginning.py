# DLL insetion at beginning


class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
        
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
obj.insert_start()
obj.display()
