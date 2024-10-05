# import qrcode.constants
# import qrcode.image
# import qrcode.image.pil
# import qrcode.image.svg
# import qrcode.util
import this
""" 
def generate_qr():
    qr_data = input("Enter the text or URL for the QR Code: ")
    file_name = input("Enter the file name: ")
    # generate/make a QR
    qr = qrcode.QRCode(
        version=1,
        error_correct=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR Code saved as {file_name}")
 """
# zen of python
print(this)