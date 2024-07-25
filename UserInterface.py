import customtkinter as ctk


def hello():
    print("Hello, World!!")


if __name__ == '__main__':
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')
    app = ctk.CTk()
    app.geometry('500x500')
    app.iconbitmap('green_folder.ico')
    app.title('File Categorizer User Interface')
    button = ctk.CTkButton(app, command=hello)
    button.pack(pady=80)
    app.mainloop()
