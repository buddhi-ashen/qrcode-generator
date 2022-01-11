import qrcode
import image

qr = qrcode.QRCode(
    version = 15, # 15 means the version of qr code 
    box_size = 10,  # 10 means for the box that contain qr code
    border = 5 # 5 means the white color border around qr code 
)

data = "https://www.python.org/"
# data means the link or the source for the qr code 
# it must be put between double qoute

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white")
img.save ("test.png")
