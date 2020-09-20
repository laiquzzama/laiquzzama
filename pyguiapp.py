import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile("save.txt"):
	with open("save.txt", "r") as f:
		tempApps = f.read()
		tempApps = tempApps.split(",")
#		print (tempApps)
		apps = [x for x in tempApps if x.strip()]

def addApp():

	for widget in frame.winfo_children():
		widget.destroy()

		filename = filedialog.askopenfilename(initialdir="/", title="select file",
		filetypes = (("exeutables", "*.exe"), ("all files", "*.*")))
		apps.append(filename)
		print (filename)

		for app in apps:
			label = tk.Label(frame, text=app, bg= "gray")
			label.pack()
def runApps():
	for app in apps:
		os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700,bg= "#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openfile = tk.Button(root, text="Open file", padx=10, pady=5, fg="red", bg="#263D42", command=addApp)
openfile.pack()
runApps = tk.Button(root, text="run Apps", padx=10, pady=5,fg="red", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
	label= tk.Label(frame, text=app)
	label.pack()

root.mainloop()

with open("save.txt","w") as f:
	for app in apps:
		f.write(f + ",")
