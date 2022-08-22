#Stone(s),Paper(p),Scissors(c) game project in python

import random         #importing random function for pc to choose one of them randomly s,p,c 

def gameWin(pc, you):    #if both values are same then game will tie
    if pc == you:
     return None
    elif pc == 's':      #all possiblity when pc chooses s
        if you == 'p':
          return True
        elif you == 'c':
          return False 
    elif pc == 'p':      #all possiblity when pc chooses p
        if you == 'c':
            return True
        elif you == 's':
            return False 
    elif pc == 'c':       #all possiblity when pc chooses c
        if you == 's':
            return True
        elif you == 'p':
            return False            

print("PC turn: I chose one of them (STONE PAPER SCISSORS) its your turn.") 
randno=random.randint(1,3)

if randno == 1:
    pc ='s'
elif randno == 2:
    pc = 'p'
elif randno == 3:
    pc = 'c'        

you = input("Player turn: STONE(s) PAPER(p) SCISSORS(c)? ")
a= gameWin(pc, you)           #calling function 'gameWin'

print(f"PC chose: {pc}")
print(f"You chose: {you}")
if a == None:               #final results of the game
   print("The game is a tie!")
elif a:
   print("You Win!")
else:
   print("You Lose!")                                        #by Somya Kulshrestha
