import qrcode
import os
def create_qr_code(data, fileName = 'qr_code.png'):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,


    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(fileName)
    print(f"QR code created successfully at the path {os.path.abspath(fileName)}")

if __name__ == '__main__':
    data = input("Enter the data to be encoded in QR code: ")
    fileName = input("Enter the name of the file to save the QR code: ")
    create_qr_code(data, fileName)
    
