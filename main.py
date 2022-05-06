#

#
#
#
#

from tkinter import *
from tkinter import messagebox

import subprocess

def manupdate():
        subprocess.run(["sudo", "-S", "apt", "update"])
        subprocess.run(["sudo", "-S", "apt", "-y", "upgrade"])
        subprocess.run(["sudo", "-S", "apt", "-y", "autoremove"])
        subprocess.run(["sudo", "-S", "apt", "-y", "install", "update-manager-core"])   # sudo apt install update-manager-core
        messagebox.showinfo('Update', 'Update udført')
def upgrade():
        svar = messagebox.askokcancel('Upgrade', 'Er du sikker på om du vil fortsætte')
        if svar:
            messagebox.showinfo('upgraderer', 'upgradering igang')
            subprocess.run(["sudo", "-S", "do-release-upgrade", "-d"]) #sudo do-release-upgrade
            messagebox.showinfo('upgraderer', 'upgradering færdig')
def luk():
    window.destroy()

window = Tk()

window.geometry('500x300')
window.title("Force Ubuntu Update til System Upgrade")

lbl = Label(window, text="Dette lille program kører nogle ting i terminal.")
lbl.grid(column=0, row=0)

btnupd = Button(window, text="Refrech / Update", command=manupdate)
btnupd.grid(column=0, row=1)

btnupg = Button(window, text="Upgrade", command=upgrade)
btnupg.grid(column=1, row=1)

btnluk = Button(window, text="Luk", command=luk)
btnluk.grid(column=2, row=1)


window.mainloop()