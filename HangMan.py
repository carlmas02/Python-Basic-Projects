print("'$$\   $$\'")
print(" $$ |  $$ |")
print("'$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\'")
print("'$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\' ")
print(" $$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |")
print(" $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |")
print(" $$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |")
print(" \__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|")
print("                               $$\   $$ |                                  ")
print("                               \$$$$$$  |                                  ")
print("                                \______/                                   ") 


#modules
import random



#lists
newlist = [] #list for text file
main_list = []
guessed = []
life = []


#file reading
file = open("word.txt","r")
f = file.readlines()

for i in f:
   newlist.append(i[:-1])


#word to be guessed
eg = (random.choice(newlist)).upper()
print(eg)


#checking list
win_word = [x for x in eg]

#main
guesses = len(eg)

print(f"Letters which you have guessed :{guessed} \n")

for letter in eg:
   main_list.append("-")
print(main_list)   


for letter in eg:
   life.append("★")
print(f"Available chances :{life}")   

def getind(char):
   return [k for k,v in enumerate(eg) if char == v]
   
while "-" in main_list:
   alpha = input("guess :").upper()
   print("\n")
   if alpha in eg:
      if alpha in main_list:
         print("Already exists")
      else:
         indexes = getind(alpha)
         for index in indexes:
            main_list[index] = alpha
         
         
        
                     
   else :
      if guesses == 1:
         print("Game over , you lose")
         print(f"The word was {eg}")
         break
      else:
         print("Invalid choice")
         life.pop()
         guesses -= 1
         

   print(f"Letters which you have guessed :{guessed} ")
   print(main_list)
   print(f"Available chances :{life}") 
   
