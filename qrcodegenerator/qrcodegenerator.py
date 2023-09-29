# pip install qrcode
# pip instal image

import qrcode
import image

qr_code = qrcode.QRCode(
    version=15,
    box_size=5,
    border=2
)

data = "google.com"

qr_code.add_data(data)
qr_code.make(fit=True)
img = qr_code.make_image(fill='black', back_color='white')
img.save('google_qrcode.jpg')
