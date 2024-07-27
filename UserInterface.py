from tkinter import *


def apply():
    pathShowLabel.config(text=f' {inputPath.get()} {inputCopy.get()} {renameList.get(renameList.curselection())}')


if __name__ == '__main__':
    app = Tk()
    app.title('File Categorizer')
    app.minsize(500, 500)
    app.maxsize(500, 500)

    header = Label(app, text='The program was created by Ahmed Noah', font=('Arial', 15), bg='yellow', fg='blue')
    header.pack()

    pathLabel = Label(app, text='Enter the path to work on', font=('Arial', 15))
    pathLabel.pack()

    inputPath = StringVar()

    pathEntry = Entry(app, font=('Arial', 15), bd=3, textvariable=inputPath)
    pathEntry.pack()

    pathShowLabel = Label(app, text='', font=('Arial', 15))
    pathShowLabel.pack()

    inputCopy = BooleanVar()

    copyCB = Checkbutton(app, text='Copy the files', font=('Arial', 15), variable=inputCopy)
    copyCB.pack()

    renameList = Listbox(app, font=('Arial', 15))
    renameList.insert(END, 'Rename files')
    renameList.insert(END, 'Do not rename files')
    renameList.pack()

    enterButton = Button(app, text='Apply', font=('Arial', 15), command=apply)
    enterButton.pack()

    app.mainloop()
