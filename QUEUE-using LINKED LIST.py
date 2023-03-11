# QUEUE usin LIST
queue=[]
def enqueue():
    element=input("enter the element:")
    queue.append(element)
    print(element,"is addded in q")
def dequeue():
    if not queue:
        print("q is empty")
    else:
        e=queue.pop()
        print("removed element",e)
def display():
    print(queue)
while True:
    print("select operation 1.dequeue 2.enqueue 3.quit")
    choice=int(input())
    if choice ==1:
        dequeue()
        
    elif choice==2:
        enqueue()
        
    elif choice==3:
        print('operation quited')
        break
    else:
        print("enter right operation:")

        
