from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def menbar(root):

	MenuBar = Menu(root)

	FileMenu = Menu(MenuBar, tearoff=0)
	FileMenu.add_command(label="New")

	FileMenu.add_command(label="Open")

	FileMenu.add_command(label = "Save")
	FileMenu.add_separator()
	FileMenu.add_command(label = "Exit")
	MenuBar.add_cascade(label = "File", menu=FileMenu)

	EditMenu = Menu(MenuBar, tearoff=0)
	EditMenu.add_command(label = "Cut")
	EditMenu.add_command(label = "Copy")
	EditMenu.add_command(label = "Paste")

	MenuBar.add_cascade(label="Edit", menu = EditMenu)
	HelpMenu = Menu(MenuBar, tearoff=0)
	HelpMenu.add_command(label = "About Notepad")
	MenuBar.add_cascade(label="Help", menu=HelpMenu)
	root.config(menu=MenuBar)

root=Tk()
root.title("notepad")
root.geometry("720x480")
TextArea=Text(root).pack(expand=True, fill=BOTH)

menbar(root)


# Scroll = Scrollbar(TextArea)
# Scroll.pack(side=RIGHT,  fill=Y)
# Scroll.config(command=TextArea.yview)
# TextArea.config(yscrollcommand=Scroll.set)


root.mainloop()