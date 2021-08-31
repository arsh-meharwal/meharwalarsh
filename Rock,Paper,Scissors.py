def RPS(C,H):
 if (C == "R"):
     if H == "P":
         return H
     elif H == "S":
         return C
 if C == "P":
     if H == "R":
         return C
     elif H == "S":
         return H
 if C == "S":
      if H == "R":
          return H
      elif H == "P":
          return C 
 if C == H:
     return False  

import random
print("Computer Chosed")
rand = random.randint(1,3) 
if rand == 1:
    C = 'R'
if rand == 2:
    C = 'P'
if rand == 3:
    C = 'S'   

H = input(print("Your Turn")) 
print(f"Computer chosed {C}")
print(f"You Chosed {H}") 
m = RPS(C,H) 
if m == False:
    print("Tie")
elif m == C:
    print("Computer Wins")
elif m == H:
    print("Human Wins ")        









