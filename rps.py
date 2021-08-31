import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from PIL import Image
from PIL import ImageTk
import tkinter.font as TkFont
import math
from tkinter.ttk import *

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Reflect File (*.refl)", "*.refl"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Reflect Code Editor - {os.path.basename(filepath)}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".refl",
        filetypes=[("Reflect File (*.refl)", "*.refl"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Reflect Code Editor - {os.path.basename(filepath)}")

def add_highlighter():
#    txt_edit.highlight_pattern("word", "red")
#    txt_edit.tag_add("start", "2.8", "1.13")
   txt_edit.tag_add("start", "1.11","1.20")
   txt_edit.tag_config("start", background= "black", foreground= "white")

window = tk.Tk()
window.title("Reflect Code Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
font = TkFont.Font(family="Sans Serif", size=15)

txt_edit = tk.Text(window,font=font)
txt_edit.tag_configure("start", background="black",foreground='red')


fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2,bg='black')
btn_open = tk.Button(fr_buttons, text="Open", command=open_file,bg='white',fg='black',bd=0,font=font)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file,bg='white',fg='black',bd=0,font=font)
highlight = tk.Button(fr_buttons, text="Highlight", command=add_highlighter,bg='white',fg='black',bd=0,font=font)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
highlight.grid(row=2, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()