import qrcode as qr

try:
    img = qr.make(str(input("Mesage to turn to qr code: ")))
    print("Qr code saved")
except:
    print("Qr code creation error failed, Please try again")
    
img.save("qr2.png")