from tkinter.messagebox import YES

print("..Welcome to my mini games..")

playing = input("Do you want to play? ")

if playing.lower() =="yes":
        print("Continue")
else:      
 quit()    
    
print("Okay! Let's play")

Score = 0
    
answer = input("What does CSE stands for? ")
if answer == "Computer Science Engineering":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")
 
answer = input("What does CPU stands for? ")
if answer == "Central Processing Unit":
   print('Correct!')
   Score += 1
else:
   print("Incorrect!")
   
answer = input("What does RAM stands for? ")
if answer == "Random Access Memory":
   print('Correct!')
   Score += 1
else:
   print("Incorrect!")
 
answer = input("What does ROM stands for? ")
if answer == "Read Only Memory":
  print("Correct!")
  Score += 1
else:
  print("Incorrect!")
  
print("You got " + str(Score) + " questions correct!")  

print("You got " + str((Score / 4) * 100) + "%.")  