import tkinter as tk
from tkinter import messagebox
from tkinter.constants import DISABLED, HIDDEN, NORMAL
import qrcode as qr
import cv2 as cv

image = ""

##Check version/ test pop up
# tkinter._test()

#setup
window = tk.Tk()
window.title("QR Code Generator")
# window.geometry("200x150")
# 

#button functions
def test():
    tk.messagebox.showinfo("Test", e1.get())
    # cv.imshow("Image", img)

def genqr():
    img = qr.make(e1.get())
    e1.delete(0, 'end')
    B2.config(state= NORMAL)
    img.save("qr1.png")
    tk.messagebox.showinfo("QR Code", "Your qr code was made,\nYou can now preview it")

def open():
    try:
        img = cv.imread("qr1.png")
        cv.imshow("QR Code", img)
    except Exception as e:
        tk.messagebox.showerror("Error", "You need to generate a QR Code first")
        print(e)

L1 = tk.Label(window, text = "Text/ Url")
L1.grid(row = 0, column= 0)

e1 = tk.Entry(window)
e1.grid(row = 0, column = 1)

B1 = tk.Button(window, text = "Generate", command=genqr)
B1.grid(row = 1, column= 0)

B2 = tk.Button(window, text = "Preview", command= open, state= DISABLED, width = 15)
B2.grid(row = 1, column = 1)

#ensures that the window stays open untill the user or code closes it
window.mainloop()
