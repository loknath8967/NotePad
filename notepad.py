import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root,undo=True)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):



        # Set the window text
        self.__root.title("Untitled - Notepad")

        # For top and bottom
        self.__root.geometry('1024x786')

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)



        # To open new file

        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile, accelerator="Ctrl+N")
        self.__root.bind("<Control-n>""<Control-N>", self.__newFile)

        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile, accelerator="Ctrl+O")
        self.__root.bind("<Control-o>""<Control-O>", self.__openFile)

        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile, accelerator="Ctrl+S")
        self.__root.bind("<Control-s>", self.__saveFile)

        self.__thisFileMenu.add_command(label="save as ",
                                        command=self.__save, accelerator="Ctrl+Shift+S")
        self.__root.bind("<Control-Shift-s>""<Control-Shift-S>", self.__save)

        self.__thisFileMenu.add_command(label="copy",
                                        command=self.__copy, accelerator="Ctrl+C")
        self.__root.bind("<Control-c>""<Control-C>", self.__copy)

        self.__thisFileMenu.add_command(label="cut",
                                        command=self.__cut, accelerator="Ctrl+X")
        self.__root.bind("<Control-x>""<Control-X>", self.__cut)

        self.__thisFileMenu.add_command(label="paste",
                                        command=self.__past, accelerator="Ctrl+V")
        self.__root.bind("<Control-v>""<Control-V>", self.__past)

        self.__thisFileMenu.add_command(label="undo",
                                        command=self.__undo, accelerator="Ctrl+Z")
        self.__thisFileMenu.add_command(label="redo",
                                        command=self.__redo, accelerator="Ctrl+Y")

        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__Exit, accelerator="Ctrl+Q")
        self.__root.bind("<Control-q>""<Control-Q>", self.__Exit)

        # To create a feature of description of the notepad

        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)








        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)




    def __Exit(self):
        self.__root.destroy()




    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __save(self):
            # Save as new file
        self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

        if self.__file == "":
            self.__file = None
        else:

            # Try to save the file
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

            # Change the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")




    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __past(self):
        self.__thisTextArea.event_generate("<<Paste>>")



    def __undo(self):
        self.__thisTextArea.event_generate("<<Undo>>")
    def __redo(self):
        self.__thisTextArea.event_generate("<<Redo>>")


    def run(self):

        # Run main application
        self.__root.mainloop()

    # Run main application


notepad = Notepad()
notepad.run()
