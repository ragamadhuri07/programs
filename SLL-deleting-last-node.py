#single linked list deleting last node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def delete(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None    

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp=temp.next
obj=SLL()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n2=node(30)
n1.next=n2
obj.display()
print()
obj.delete()
obj.display()
