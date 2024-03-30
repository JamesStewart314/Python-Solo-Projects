# /-----------------------------------------------------------------------------------------------------------------------------------\
#  This code is a QR Code Generator created in Python language - version 3.12 or higher - with dependencies on the "qrcode" library.
#                       To run it properly, make sure you have this package in your virtual environment.
#                                                 Code Created in ~ 01/28/2024 ~
# \-----------------------------------------------------------------------------------------------------------------------------------/

import qrcode


class QRCode:
    def __init__(self, *, scale: int, padding: int) -> None:
        self.qr = qrcode.QRCode(box_size=scale, border=padding)

    def create_qr(self, file_name: str, foreground_color: str | tuple[int, int, int], background_color: str | tuple[int, int, int], /) -> None:

        """
        This method generates the QR code image itself.

        :param file_name: String type parameter that corresponds to the desired name for the PNG file containing the QR code.
        :param foreground_color: String type parameter that specifies the desired color for the foreground of the qr code. 
        If you are unable to provide the color name, try entering a tuple containing three integers corresponding to the color's RGB code. 
        (e.g.: 'black', (128, 128, 128), 'White', etc)
        :param background_color: Analogous to the foreground color specifications, this parameter defines the background color only.
        :return: None.
        """

        user_info: str = input("Type the text that you want to convert into QR Code: ")

        try:
            self.qr.add_data(user_info)
            qr_image = self.qr.make_image(fill_color=foreground_color, back_color=background_color)
            qr_image.save(file_name)

            print(f"The QR Code was sucessfully Created! ({file_name})")
        except Exception as error:
            print(f"Error: {error}")
        

if __name__ == '__main__':
    
    # Test :
    myqr: QRCode = QRCode(scale=30, padding=2)
    myqr.create_qr('Sample.png', (57, 255, 20), 'black')
