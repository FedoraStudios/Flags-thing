from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Flags")
root.geometry("600x400")
root.configure(bg = "dark grey")

GetFlagName = Entry(root)
ShowFlag = Label(root)

GaldaronFlag = (Image.open("Galdaron empire flag.jpg"))
ResizedGaldaronFlag = GaldaronFlag.resize((300,205), Image.ANTIALIAS)
NewResizedGaldaronFlag = ImageTk.PhotoImage(ResizedGaldaronFlag)
#the flags above and below this comment were made my Emir R. Frias-Suzuki on 7/4/2019 and has copyright over them
LionarFlag = (Image.open("Lionar Kingdom flag.jpg"))
ResizedLionarFlag = LionarFlag.resize((300,205), Image.ANTIALIAS)
NewResizedLionarFlag = ImageTk.PhotoImage(ResizedGaldaronFlag)

CanadaFlag = (Image.open("Canada.jpg"))
ResizedCanadaFlag = CanadaFlag.resize((300,205), Image.ANTIALIAS)
NewResizedCanadaFlag = ImageTk.PhotoImage(ResizedCanadaFlag)

GermanyFlag = (Image.open("Germany.jpg"))
ResizedGermanyFlag = GermanyFlag.resize((300,205), Image.ANTIALIAS)
NewResizedGermanyFlag = ImageTk.PhotoImage(ResizedGermanyFlag)

FranceFlag = (Image.open("France.jpg"))
ResizedFranceFlag = FranceFlag.resize((300,205), Image.ANTIALIAS)
NewResizedFranceFlag = ImageTk.PhotoImage(ResizedFranceFlag)


FlagsDictionary = {"Galdaron":NewResizedGaldaronFlag,
                   "Lionar":NewResizedLionarFlag,
                   "Canada":NewResizedCanadaFlag,
                   "Germany":NewResizedGermanyFlag,
                   "France":NewResizedFranceFlag,
                   }

def ShowFlags():
    try:
        FlagName = GetFlagName.get()
        print(FlagName)
        ShowFlag['image'] = FlagsDictionary[FlagName]
        
    except:
        messagebox.showinfo("Sorry", "This Flag is not avaliable")
        
btn = Button(root, text="Show Country Flag", command=ShowFlags)
GetFlagName.place(relx = 0.5, rely = 0.1, anchor=CENTER)
btn.place(relx = 0.5, rely = 0.16, anchor=CENTER)
ShowFlag.place(relx = 0.5, rely = 0.5, anchor=CENTER)

root.mainloop()