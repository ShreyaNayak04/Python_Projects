name=input("Type your name:")
print("Welcome", name, "to this adventure!")
answer=input("You can go left or right.Which way would you like to go? ").lower()

if answer=="left":
    answer=input("You come to a river,you can walk around it or swim across? Type walk to walk around and swim to swim around:")
    if answer=='swim':
        print("You swam across and eaten by a alligator!")
    elif answer=="walk":
        print("You walked for many miles and you lost a game.")
    else:
         print("Not a valid option.You lose") 
            
    
    
elif answer=="right":
    answer=input("You come to a bridge,do you wnat to cross it or head back(cross/back)? ")
    if answer=='cross':
        answer=input("You cross the bridge and you meet a stranger.Do you talk to them(yes/no)? ")
        if answer=="yes":
         print("You talk to the stranger and they gave you a gold. YOU WIN!")
        elif answer=="no":
         print("You ignored the stranger.You lose!")
        else:
            print("Not a valid option.You lose")    
 
                
    elif answer=="back":
        print("You go back.")
    else:
         print("Not a valid option.You lose") 
    
else:
    print("Not a valid option.You lose")  
print("THANK YOU FOR TRYING!",name)      

