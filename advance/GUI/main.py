import tkinter as tk
import os
screen = tk.Tk()

screen.geometry('400x300')

screen.title('File-handling')
  
screen.configure(bg='lightblue')

icon_path = r'images\logo.ico'

screen.iconbitmap(icon_path)

file_name = tk.Label(screen, text='Filename: ')
file_name.grid(column=0, row=0)

file_entry = tk.Entry(screen)
file_entry.grid(column=1, row=0)

file_ext = tk.Label(screen, text='Extention: ')
file_ext.grid(row=1, column=0)

ext_entry = tk.Entry(screen)
ext_entry.grid(row=1, column=1)

def save_file():
    file_name = file_entry.get()
    file_ext = ext_entry.get()
    file_path = f'{file_name}.{file_ext}'
    os.system(f'type nul > {file_path}')
    print(f'File saved as: {file_path}')

tk.Button(screen, text="Save", bg="black", fg="white", command=save_file).grid(row=2, column=1)
screen.mainloop()