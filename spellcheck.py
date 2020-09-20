from textblob import TextBlob 
a = str(input("enter your word to check spell")
_b = TextBlob(a)
print (_b.correct())

# from textblob import Textblob

#mylst = ["firt","clor"]
#correct_list = []
#for word in mylst:
#	correct_list.append(TextBlob())
#
#for word in correct_list:
#	print (word.correct())

