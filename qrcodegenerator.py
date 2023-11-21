import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size=10,
    border = 5
    )

#Here i have used my github repository link
data = "https://github.com/sricodings"

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill_color = "black",back_color ="white")
image.save("qrcode.png")
