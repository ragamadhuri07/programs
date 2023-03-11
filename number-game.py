import random
n=random.randrange(0,20)
guess=int(input("Enter the guess: "))
while n!=guess:
    if guess<n:
        print("too low")
        guess=int(input("Enter no. again: "))
    elif guess>n:
        print("too high")
        guess=int(input("enter no. again: "))
    else:
        break
print("you guessed it right")    
                
