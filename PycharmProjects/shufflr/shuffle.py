import tkinter as tk
import random

root = tk.Tk()
root.title('Furry Generator')
root.iconbitmap("creative-icon.ico")
root.configure(bg='pink')
root.geometry("500x300")

def furryClick():
    with open("aesthetics.txt") as f:
        aeslines = f.readlines()
    with open("animals.txt") as f:
        animallines = f.readlines()

    label = tk.Label(text="This furry is a " + random.choice(animallines) + "with " + random.choice(aeslines) + "aesthetic.", bg="pink")
    label.pack()

furryButton = tk.Button(root, text="Furrify!", command=furryClick, fg="black", bg="paleturquoise")
furryButton.pack()

root.mainloop()
