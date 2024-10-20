import qrcode
from PIL import Image 

import qrcode.constants 
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://chatgpt.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="#00FFFF",back_color="black")
img.save("chat gpt.png")
