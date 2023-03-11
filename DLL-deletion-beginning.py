# DLL deletion first node

class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def delete_start(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp.next=None
        
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
n3=node(30)
n3.prev=n2
n2.next=n3
n4=node(40)
n4.prev=n3
n3.next=n4
obj.display()
print()
obj.delete_start()
obj.display()
