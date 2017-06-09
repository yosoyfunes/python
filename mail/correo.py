#!/usr/bin/env python
# -*- coding: utf-8 -*-

# URL de ejemplo
#http://recursospython.com/guias-y-manuales/smtp-enviar-email/

import sys

from email.mime.text import MIMEText
from smtplib import SMTP

def main():
    from_address = "correo@memosoft.net.ar"
#   to_address = "matiasanoniz@gmail.com"
    to_address = sys.argv[1] # Argumento pasado por linea de comando // [0] es el nombre del PATH // [1] el el 1er argumento
    message = "Correo de Prueba en Python"
    password = "453363015dsdHSfdSIWnlsdaJNCcs"
    
    mime_message = MIMEText(message, "plain")
#	mime_message = MIMEText(message, "html", _charset="utf-8")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Correo de prueba"
        
    smtp = SMTP()
    smtp.connect("mail.memosoft.net.ar", 587)

    smtp.login(from_address, password) #Clave
    
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()

#if __name__ == "__main__":

main()