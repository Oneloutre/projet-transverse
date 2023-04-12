import tkinter
from tkinter import *
import Ecran
def fullscreen():
    is_fullscreen=root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)
    set_background_image(backGround_path,10,10)

def set_background_image(backGround_path, width, height):
    canvas = root.canvas
    backGround = PhotoImage(file=backGround_path)
    backGround = backGround.subsample(backGround.width() // width, backGround.height() // height)
    canvas.create_image(0, 0, image=backGround, anchor="nw")
    canvas.image = backGround

root = tkinter.Tk()
root.title("VollEfrei")
root.iconphoto(False, tkinter.PhotoImage(file="assets/volley-transparent.png"))
can = tkinter.Canvas(root, width=1280, height=720)
backGround_path="assets/fond_decran_volleyefrei_2.png"
backGround = tkinter.PhotoImage(file=backGround_path)
width = backGround.width()
height = backGround.height()
can.create_image(width//2, height//2, image=backGround)
can.place(x=0,y=0)
can.pack()
root.geometry("%dx%d+0+0" % (width, height))

menuBar= Menu (root)
root.config(menu=menuBar)
menuRéglages = Menu(menuBar, tearoff=0)
menuParamètres=Menu(menuRéglages, tearoff=0)
menuEcran=Menu(menuParamètres,tearoff=0)
menuBar.add_cascade(label="Réglages",menu=menuRéglages)
menuRéglages.add_cascade(label="Paramètres",menu=menuParamètres)
menuRéglages.add_command(label="Fermer le jeu",command=quit)
menuParamètres.add_cascade(label="Ecran",menu=menuEcran)
menuParamètres.add_command(label="Touches")
menuEcran.add_command(label="Plein écran",command=fullscreen)

root.mainloop()
