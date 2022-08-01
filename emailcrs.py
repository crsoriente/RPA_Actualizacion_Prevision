#Envio de los archivos Excel a los emails de los interesados
from RPA.Email.ImapSmtp import ImapSmtp
class Emailcrs:
    def envio_de_archivos(fecha_actual, total_registros):
        #Agregar la ruta hacia los archivos que se generaron en reporte.py
        archivos = [
            "reporte_alerta_fonasa.xlsx",
            "reporte_otras_alertas.xlsx",
            "reporte_prevision_actualizada.xlsx",
            "reporte_paciente_fallecido.xlsx"
            ]
        #Agregar los datos de la cuenta de correo, para este caso se utilizó una cuenta gmail
        gmail_account = ""
        gmail_password = ""
        sender = gmail_account
        #Lista de personas a las cuales les debe llegar los archivos
        correos = [
            "", ""
            ]
        mail = ImapSmtp(smtp_server="smtp.gmail.com", smtp_port=587)
        mail.authorize(account=gmail_account, password=gmail_password)
        
        #Agregar los datos del receptor, asunto y mensaje que ira en el cuerpo del email
        mail.send_message(
            sender=gmail_account,
            recipients="",
            subject="",
            body="""
                    """
            ,
            html=True,
            attachments=archivos,
            cc=correos
        )