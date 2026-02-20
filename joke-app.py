
#Option-2
import random 
secret=random.randint(1,10)
attempts=0
while True:
 guess=int(input("Your guess:"))
 attempts+=1
 if guess>secret:
    print("A little lower")
 elif guess<secret:
    print("A little higher")
 else:
    print("Correct!")
    print("You guessed in",attempts,"attempts") 
    break