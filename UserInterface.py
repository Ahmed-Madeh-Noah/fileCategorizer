from tkinter import *

if __name__ == '__main__':
    app = Tk()
    app.title('File Categorizer')
    app.minsize(500, 500)
    header = Label(app, text='This program was made by Ahmed Noah', bg='yellow', fg='red',
                   font=('Times New Roman', 12, 'bold'))
    header.pack()
    app.mainloop()
