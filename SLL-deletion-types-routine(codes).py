#single linked list deletion


#deleting first node(routine code)
def del(self):
    temp=self.head
    self.head=temp.next
    temp.next=none

#deleting last node(routine code)
def del(self):
    temp=self.head.next
    prev=self.head
    while temp.next is not None:
        temp=temp.next
        prev=prev.next
    prev.next=none

#deleting given specific node(routine code)
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(0,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
