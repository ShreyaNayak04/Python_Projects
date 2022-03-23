print("Welcomwe to the quiz game")
play=input("Do you want to play ? ")
if play.lower()!="yes":          #by using this yes and YES will be same
    quit()
    print("Okay lets play!")
score=0  
answer=input("What does cpu stands for ? ") 
if answer.lower()=="central processing unit":
    print("Correct")
    score+=1
else:
    print("incorrect")  
    
     
answer=input("What does RAM stands for ? ") 
if answer.lower()=="random access memory":
    print("Correct")
    score+=1
else:
    print("incorrect")
       
    
answer=input("What does ROM stands for ? ") 
if answer.lower()=="read only memory":
    print("Correct")
    score+=1
else:
    print("incorrect")
    
       
answer=input("What does GNU stands for ? ") 
if answer.lower()=="graphic processing unit":
    print("Correct")
    score+=1
else:
    print("incorrect") 

print("You got "+ str(score) + " questions correct !")     
print("You got "+ str((score)/4 * 100) + "%")     
    