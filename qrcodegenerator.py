import qrcode
import numpy as np
import cv2

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://github.com/sricodings"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

width, height = img.size
new_img = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        pixel = img.getpixel((x, y))
        new_img[y, x] = pixel

cv2.imwrite("qrcode.png", new_img)

print("QR code generated and saved as 'qrcode.png'")
