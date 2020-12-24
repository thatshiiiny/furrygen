import tkinter as tk
import random
import webbrowser

root = tk.Tk()
root.title('Furrygen')
root.iconbitmap("creative-icon.ico")
root.configure(bg='pink')
root.geometry("550x200")

animalFrame = tk.LabelFrame(root, text="Animal", bg="pink", padx=5, pady=5)
animalFrame.pack(padx=5, pady=5, side=tk.LEFT)

fishCheck = tk.Checkbutton(animalFrame, text="Fish", fg="black", bg="pink", selectcolor="paleturquoise")
fishCheck.pack(side=tk.BOTTOM, anchor="w")
birdCheck = tk.Checkbutton(animalFrame, text="Bird", fg="black", bg="pink", selectcolor="paleturquoise")
birdCheck.pack(side=tk.BOTTOM, anchor="w")
amphiCheck = tk.Checkbutton(animalFrame, text="Amphibian", fg="black", bg="pink", selectcolor="paleturquoise")
amphiCheck.pack(side=tk.BOTTOM, anchor="w")
reptileCheck = tk.Checkbutton(animalFrame, text="Reptile", fg="black", bg="pink", selectcolor="paleturquoise")
reptileCheck.pack(side=tk.BOTTOM, anchor="w")
mammalCheck = tk.Checkbutton(animalFrame, text="Mammal", fg="black", bg="pink", selectcolor="paleturquoise")
mammalCheck.pack(side=tk.BOTTOM, anchor="w")

optionsFrame = tk.LabelFrame(root, text="Options", bg="pink", padx=5, pady=5)
optionsFrame.pack()

def nameField():
    print(chkValue.get())

chkValue = tk.BooleanVar()
chkValue.set(False)

nameCheck = tk.Checkbutton(optionsFrame, text="Type Name?", command=nameField, variable=chkValue, bg="pink")
nameCheck.pack()

def furryClick():
    with open("aesthetics.txt") as f:
        aeslines = f.readlines()
    with open("animals.txt") as f:
        animallines = f.readlines()
    with open("colors.txt") as f:
        colorlines = f.readlines()
    furryLabel = tk.Label(text="This furry is a " + random.choice(colorlines) + " " + random.choice(
        animallines) + "with " + random.choice(aeslines) + "aesthetic.", bg="pink", fg="darkmagenta")
    furryLabel.pack()

furryButton = tk.Button(root, text="Furrify!", command=furryClick, fg="black", bg="paleturquoise", relief="raised")
furryButton.pack(anchor=tk.N)

def creditClick():
    top = tk.Toplevel()
    top.configure(bg='lightblue')

    creditText = tk.Text(top, height=3, width=50)
    creditText.pack()
    creditText.insert(tk.END, "Created by Shiiiny\nAesthetics taken from aesthetics.fandom.com. ")

    wikiButton = tk.Button(top, text="Aesthetic Wiki", command=wikiClick, bg="lightblue")
    wikiButton.pack()

    tk.mainloop()

    top.mainloop()
    
creditButton = tk.Button(root, text="Credits", command=creditClick, fg="black", bg="paleturquoise", relief="raised")
creditButton.pack(side=tk.LEFT, anchor=tk.SW)

def wikiClick():
    url = 'https://aesthetics.fandom.com/wiki/Aesthetics_Wiki'
    webbrowser.open(url)

root.mainloop()
