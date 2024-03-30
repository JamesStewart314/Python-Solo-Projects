# /-----------------------------------------------------------------------------------------------------------------------------------\
#                          This code is a Email Sender created in Python language - version 3.12 or higher
#
#               Even though it was designed for sending emails, a crucial step in the code was compromised due to the new
#                          security guidelines adopted by Google, unfortunately making its execution unfeasible.
#                                                     Code Created in ~ 02/19/2024 ~
# \-----------------------------------------------------------------------------------------------------------------------------------/


import Credentials
from Credentials import Email_Dict

import smtplib
import ssl

from ssl import SSLContext

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def create_image_attachment(image_path: str) -> MIMEImage:

    # It takes as an input parameter a path containing an
    # image and returns a MIMEImage containing the content 
    # of the image.

    with open(image_path, 'rb') as image_file:
        mime_image: MIMEImage = MIMEImage(image_file.read())
        mime_image.add_header('Content-Disposition', f"attachment; filename={image_path}")

        return mime_image


def send_email(from_email: Email_Dict, *, to_email: str, email_subject: str, email_body: str, images: str | list[str] | None = None) -> None:

    """
    
     Creates and sends the email to a recipient with the content
    provided in the function parameters.

    :param from_email: A TypedDict containing the sender's email
     and the corresponding email password.
    :param to_email: A string containing the recipient's email.
    :param email_subject: String containing the email's subject.
    :param email_body: A string with the main textual content of
     the email.
    :param images: A string with the path of the image to be 
     attached to the email, or a list of strings with the paths 
     of each image to be attached.

     :return: None.
    
    """
    
    temp_host: str = 'smtp.gmail.com'
    temp_port: int = 587

    temp_context: SSLContext = ssl.create_default_context()

    # with smtplib.SMTP_SSL(...)
    with smtplib.SMTP(host=temp_host, port=temp_port) as smtp_server:

        # Trying to log in :
        print("\033[33m• Logging In...\033[0m")

        smtp_server.ehlo()
        smtp_server.starttls(context=temp_context)
        smtp_server.login(from_email.get('email'), from_email.get('password'))

        # Preparing the Email :
        print('\033[32mSucessful!\033[0m Attempting to Send the Email...')
        message: MIMEMultipart = MIMEMultipart()
        message['From'] = from_email.get('email')
        message['To'] = to_email
        message['Subject'] = email_subject
        message.attach(MIMEText(email_body, 'plain'))

        # If User Provided Any Images :
        if images:
            if isinstance(images, str):
                # Just One Image :
                image_file: MIMEImage = create_image_attachment(images)
                message.attach(image_file)
            else:
                # More than One Image to Process :
                for image in map(create_image_attachment, images):
                    message.attach(image)
        
        smtp_server.sendmail(from_addr=from_email.get('email'), to_addrs=to_email, msg=message.as_string())

        # Sucess Message :
        print("\033[34mDone!!!\033[0m")


if __name__ == '__main__':
    send_email(Credentials.MyEmail, 
               to_email='<Destiny Email>', 
               email_subject='This is an Email Test!!!', 
               email_body='Hello There!')
