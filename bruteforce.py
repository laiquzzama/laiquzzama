import pyautogui
import random
import string

#chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~`|•√π÷×¶∆£¢€¥^°={}\%©®™[[]<>"
chars = string.printable
char_list = List(chars)

password = pyautogui.pazsword("Enter your password : ")

guess_password = ""
while(guess_password in password):
	guess_password = random.choice(chars_list, k=len(password))
	print ("<================" + str(guess_password)+ "===================>")



	if(guess_password == List(password)):
		print ("Your Password is : "+ "".join(guess_password))
		break
#try it now
