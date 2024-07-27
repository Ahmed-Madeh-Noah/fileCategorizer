from tkinter import *
from tkinter import messagebox


def apply(ignore=False):
    path = inputPath.get().strip()
    if path:
        pathShowLabel.config(text=f' {inputPath.get()} {inputCopy.get()} {rename.get()}')
    elif not ignore:
        messagebox.showerror('Error', 'Please enter a valid path')


if __name__ == '__main__':
    FONT = ('Arial', 10, 'bold')
    BG = 'lightblue'
    app = Tk()
    app.title('File Categorizer')
    app.minsize(300, 200)
    app.maxsize(600, 400)
    app.configure(bg=BG)

    header = Label(app, text='The program was created by Ahmed Noah', font=FONT, bg=BG, fg='blue')
    header.pack()

    pathLabel = Label(app, text='Enter the path to work on', font=FONT, bg=BG)
    pathLabel.pack()

    inputPath = StringVar()

    pathEntry = Entry(app, font=FONT, bd=3, textvariable=inputPath)
    pathEntry.pack()

    pathShowLabel = Label(app, text='', font=FONT, bg=BG)
    pathShowLabel.pack()

    inputCopy = BooleanVar(value=True)

    copyCB = Checkbutton(app, text='Leave a copy', font=FONT, variable=inputCopy, bg=BG)
    copyCB.pack()

    rename = BooleanVar(value=False)
    notRenameRB = Radiobutton(text='Do Not Rename', font=FONT, variable=rename, value=False, bg=BG)
    notRenameRB.pack()
    renameRB = Radiobutton(text='Rename', font=FONT, variable=rename, value=True, bg=BG)
    renameRB.pack()

    enterButton = Button(app, text='Apply', font=FONT, command=apply, bg=BG)
    enterButton.pack()

    apply(True)
    app.mainloop()
