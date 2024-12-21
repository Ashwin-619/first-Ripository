# import random
from random import choice 

# prints a random value from the list
list = [0, 1, 2]
comp_choice= choice(list)

print("0 for Snake ")
print("1 for Water ")
print("2 for Gun")
player_choice=int(input())

'''
   comp_choice        S(0)  W(1)  G(2) 
                S(0)   D     W     L
                W(1)   L     D     W
                G(2)   W     L     D 


'''

result=["Draw","Won","Lost"],["Lost","Draw","Won"],["Won","Lost","Draw"]



print(result[comp_choice][player_choice])
print(f"You : {player_choice}")
print(f"Computers choice : {comp_choice}")
