import random 
def roll_dice():
  print (random.randint(1, 6)) 
print("""Welcome to my python random dice program!

Whenever you are over, type exit.
""")
a = True
while a:
   user_prompt = input("To start press enter!")
   if user_prompt.lower() == "exit":
      a = False
   else:
     print("Rolling dice...\nYour number is:") 
     roll_dice()
