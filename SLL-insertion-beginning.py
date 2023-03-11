#single linked list insertion at beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None

    def insert_beginning(self,data):
            np=Node(data)
            np.next=self.head
            self.head=np
    def display(self):
          if self.head is None:
                print("Linked lsit is empty")
          else:
                temp=self.head
                while temp:
                    print(temp.data,"--->",end=" ")
                    temp=temp.next
obj=singlelinkedlist()

n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
i=input("enter no. to insert:")
obj.insert_beginning(i)
obj.display()
