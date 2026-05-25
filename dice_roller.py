import random

#Instructions
print("Welcome to Dice Roller Game")
print("1) if you want to roll the dice press key'Y'")
print("2) if you don't want  to roll the dice press key'N'")
print("'Y' means Yes")
print("'N' means No")
print("You have only 3 attempts")



#Dice roller game with function

user_choice=''

def dice_roller(user_choice):
    attempts=3
    i=1
    while i<=attempts:
       user_choice=input("Enter if you want to roll the dice press,('Y')=").upper()
       
       if user_choice=='Y':
         generate_random_num=random.randrange(1,7,1)
         print("Random outcome of dice is=",generate_random_num)
                
       else:
         print("You pressed 'N' that means dice is  not rolling ")
         break     
        
       i=i+1     
     
print("Your attempts are finished")
print("Goodbye! Thanks for playing")
    
dice_roller(user_choice) 




