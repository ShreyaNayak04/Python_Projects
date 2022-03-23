import random


def gamewin(computer, you):
    if(computer == you):
        return None
    elif (computer == 's'):
        if(you == 'g'):
            return True
        elif(you == 'w'):
            return False
    elif(computer=='w'):
        if(you=='s'):
            return True 
        elif(you=='g'):
            return False
    elif(computer=='g') :
        if(you=='s'):
            return False
        elif(you=='w'):
            return True
        
print("Comp turn: Snake(s) Water(w)  or Gun(g)?")
randNo=random.randint(1, 3)
if randNo=='1':
    computer='s'
elif randNo=='2':
    computer='w'
elif randNo=='3':
    computer='g'
you=input("Your turn:Snake(s) Water(w)  or Gun(g)?")   
a =gamewin(computer, you)
print("Computer chose {computer}")
print("You chose {you}") 

if a==None:
    print("Game is tie...")
elif a:
    print("You win...")
else:
    print("You lose...")        
    
