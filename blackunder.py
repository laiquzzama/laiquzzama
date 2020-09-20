from random import *
guess= ""
password=input("password >")
letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while(guess != password):
	guess =""
	for letter in range(len(password)):
		guessletter=letters[randint(0,25)] 
		guess=str(guessletter)+str(guess) 
	print (guess)
print("password is succesfully cracked !") 
input("")
if guess==password:
	print("password is ",guess)
else:
	print ("you entered a wrong password")
print (guess)
print (password)
