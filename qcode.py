import qrcode
import image
qr=qrcode.QRCode(
    version =15,   #qrcode version
    box_size=10,   #size of the qrcode
    border=8       #border of the qrcode
    
)
data="peace is always beautiful"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("code.png")