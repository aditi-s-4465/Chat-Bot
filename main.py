'''
Type your first and last names here
Aditi Shrivastava
Jay Lim
Anna Shepovalova
'''
######Team LEADER Directions#######
#Fork the challenge using the 'fork' button above
#Invite your team members to the challenge by pressing the 'invite' button
######Project Directions##### 
#Create your own chatbot like the example given in Canvas.  In order to get points, your chatbot must have the following charactheristics:  1-It must ask the user at least 9 questions 2-It must respond to the user using their answers within the response and 3-It must include at least 2 mathematical computations 

greeting = input("Hello? ")
if (greeting == "Hello!" or greeting == "hello!" or greeting == "Good Morning!" or greeting == "Good morning!" or greeting == "good morning!" ):
  print("Good Morning!")
else:
  print("Hi!")

#Question 1
print("My name is *insert quirky chatbot name*!")
chatBotName = input("Oops, look like my creator forgot to give me a name, can give one to me?   ")
print(f"{chatBotName}...hmmmm")
print("It has a nice ring to it, I like it!")
print("")

#Question 2
username = input("Since we're going to be chatting for a while, why don't you tell me your name   ")
print(f"Well hello {username}, it's nice to meet you!")
print("")

#Question 3
pizzaPref = input("Before we can be friends, pineapples on pizza? yay or nay ")
if (pizzaPref.lower()=="yay"):
  print("Good Choice")
else:
  print("We don't agree, but you seem pretty cool so we can be friends")

#Question 4
year = 2020
print(f"The year is {year}")
botAge = input("Do you want to guess my age? Have a try! (Hint: It is less than 100) ")
botAgeGuess = int(botAge)
until100 = 100-botAgeGuess
futureYear = 2020 + until100
print(f"You are correct, my age is {botAgeGuess} I will be 100 years old in {until100} which will be the year {futureYear}")

print("What about you?")
age = input("What is your age? ")
intAge = int(age)

if (intAge<=20):
  print("That is very young!")
else:
  print("That is great!")

#Question 5 + 6:
do = input("Let's have some fun now ..... Do you want to just talk? Or do you want to do something more educational such as ..... Math? (Enter '1' for the first option and '2' for the second option) ")
if(do=="1"):
  #Question 5
  print()
  ansAni = input("Alright let's talk more about each other. Anyway, what's your favorite animal? Mine is a rat! ")
  print(f"Oh you like {ansAni} ? That is really cool!")
  print()
  
elif(do=="2"):
  #Question 6
  print("Math is great! Here is something for you to try: ")
  print(" A factorial is the product of all positive integers less than or equal to a given positive integer")
  print("For example, the factorial of 3 is 3*2*1=6")
  a = input("So give me a number and I'll find a factorial: ")
  b = 1
  a = int(a)
  b = int(b)
  for i in range(1,a+1):
    b=b*i
  print(f"The factorial of {a} is {b}")

#Question 7 + 8
feelOne = input("Okey, lets chat about something else. How do you feel today? ")

if (feelOne == "happy" or feelOne == "Happy" or feelOne == "great" or feelOne == "Great" or feelOne == "good" or feelOne == "Good"):
  print("That is great!")
else:
  feel = input("Oh interesting, why do you feel" + feelOne + "today? ")
  print("Oh, that makes sense!")

#Question 9
song = input("I'm out of things to ask so how about you recommend me a song ")
print (f"{song} is a nice song")
yay = input("Do you want to recommend some more songs? yay or nay ")
while (yay=="yay"):
  song = input("Alright, give me a song ")
  print (f"{song} is a pretty cool song")
  yay = input("Do you want to recommend some more songs? yay or nay ") 

#Goodbye
goodbye = input(f"It was nice talking to you {username}. Goodbye!")


