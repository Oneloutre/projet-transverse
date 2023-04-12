import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("VollEfrei")
root.iconphoto(False, tkinter.PhotoImage(file="assets/volley-transparent.png"))
can = tkinter.Canvas(root, width=1280, height=720)
backGround = tkinter.PhotoImage(file="assets/fond_decran_volleyefrei_2.png")
width = backGround.width()
height = backGround.height()
can.create_image(width//2, height//2, image=backGround)
can.place(x=0,y=0)
root.geometry("%dx%d+0+0" % (width, height))
menuBar= Menu (root)
menuRéglages = Menu(menuBar, tearoff=0)
menuParamètres=Menu(menuRéglages, tearoff=0)
menuBar.add_cascade(label="Réglages",menu=menuRéglages)
menuRéglages.add_cascade(label="Paramètres",menu=menuParamètres)
menuRéglages.add_command(label="Fermer le jeu",command=quit)
menuParamètres.add_command(label="Ecran")
menuParamètres.add_command(label="Touches")
root.config(menu=menuBar)


root.mainloop()
