from tkinter import *


def set_path():
    x = path.get()
    pathShowLabel.config(text=x)


if __name__ == '__main__':
    app = Tk()
    app.title('File Categorizer')
    app.minsize(500, 500)
    app.maxsize(500, 500)

    header = Label(app, text='The program was created by Ahmed Noah', font=('Arial', 15), bg='yellow', fg='blue')
    header.pack()

    pathLabel = Label(app, text='Enter the path to work on', font=('Arial', 15))
    pathLabel.pack()

    path = StringVar()

    pathEntry = Entry(app, font=('Arial', 15), bd=3, textvariable=path)
    pathEntry.pack()

    enterButton = Button(app, text='Enter', font=('Arial', 15), command=set_path)
    enterButton.pack()

    pathShowLabel = Label(app, text='', font=('Arial', 15))
    pathShowLabel.pack()

    app.mainloop()
