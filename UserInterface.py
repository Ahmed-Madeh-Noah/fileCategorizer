import customtkinter as ctk

if __name__ == '__main__':
    ctk.set_appearance_mode('System')
    ctk.set_default_color_theme('green')
    app = ctk.CTk()
    app.geometry('500x500')
    app.iconbitmap('green_folder.ico')
    app.title('File Categorizer User Interface')
    app.mainloop()
