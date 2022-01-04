# pip install qrcode pillow
# pip install image

import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
# karekod içinde saklamak istediğiniz verileri giriniz.
data = "https://github.com/nezirturhalli"
# Veriyi ekleme
qr.add_data(data)
qr.make(fit=True)
# Görüntü dosyasının oluşturulması
img = qr.make_image(fill_color=(8,153,206),back_color="white")
# Oluşturulan görüntü dosyasının kayıt biçimleri. İstediğiniz formatı seçebilirsiniz.:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.png")
