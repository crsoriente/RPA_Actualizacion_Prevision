#RPA para acutualizacion de prevision Version 1.0
#Librerias de python necesarias para el funcionameinto
import pandas as pd
import numpy as np
from RPA.Browser.Selenium import *
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
import shutil
import os
import os.path
#Librerias propias para el RPA
from logs import Logs
from AlertasTrakcare import Alertastrakcare
from obtener_pacientes import Agendamiento
from reporte import Reporte
from emailcrs import Emailcrs

#obtener fecha actual para usar como noombre de archivo
fecha_archivo = datetime.now().strftime('%Y-%m-%d')

#obtener lista de citas de trakcare
data = Agendamiento.get_agendamiento_una_fecha()

#Traspaso de los datos a un dataframe para crear el archivo Excel como resgistro
df = pd.DataFrame(data, columns=['CTPCP_Code', 'CTPCP_Desc', 'SER_Desc', 'PAPMI_ID', 'PAPER_PassportNumber', 'PAPMI_Name2', 'PAPER_Name2', 'PAPER_Name', 'PAPER_Name3', 
                                'APPT_AS_ParRef', 'APPT_RowId', 'APPT_ChildSub', 'APPT_AT_DR', 'APPT_PAPMI_DR', 'APPT_Status', 'APPT_Adm_DR', 
                                'APPT_DateComp', 'APPT_TimeComp', 'APPT_LastUpdateHospital_DR'])
#Campo de fecha de cita transformado a formato datetime
df['APPT_DateComp'] = pd.to_datetime(df['APPT_DateComp']).dt.date
#Campo de hora transformado a formato tiempo
df['APPT_TimeComp'] = pd.to_datetime(df['APPT_TimeComp'], format='%H:%M:%S').dt.time
df['APPT_ChildSub'] = df['APPT_ChildSub'].astype(np.int64)

#Archivo excel para respaldo de agenamientos de citas
print("Creando archivo de lista de agendamientio...")
nombre_archivo = 'Lista_Agendamiento_'+fecha_archivo+'.xlsx'
#Creacion de archivo Excel, agregar ruta donde se desea guardar el arhivo
df.to_excel("" + nombre_archivo, index=False)

#Total de filas a recorrer
print("Total Registros: " + str(df.index))

#Eliminacion de rut duplicados
df.drop_duplicates(subset=['PAPMI_ID'], inplace=True)

#Elemento de TrakCare
"""Frames"""
FrameMenu = 'id:eprmenu'
FrameMain = 'id:TRAK_main'

"""Botones"""
BotonLogon = 'Logon'
BotonLogout = '//*[@id="MainMenuLinksLogout"]'
BotonBuscar = 'xpath://*[@id="find1"]'
BotonActualizar = '//*[@id="update1"]'

"""Links"""
AdmisionAmbulatoria = 'name:LocListGroupz3'
RegitroPaciente = 'id:MainMenuItem52767'
NumeroRegistro = 'id:RegistrationNoz1'
ActualizarPrevision = '//*[@id="AccordionContentPAPerson.Edit6"]/table/tbody/tr[4]/td[2]/a'

"""Alertas"""
alerta_fallecido='Ha seleccionado un paciente fallecido. Seleccione "Aceptar" para continuar'
alerta_fonasa='ATENCIÓN: Datos obtenidos desde FONASA '
alerta_otros="""Categoría de Alerta:Administrativo"""

print("Abirendo TrakCare...")

#Abre TrakCare con Chrome en modo sandbox
browser = Selenium()
browser.auto_close=False
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Inicio a las: ", current_time)

#Login en TrakCare
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#Agregar la ruta donde está el chromedrive en executable_path
browser.open_browser('http://10.8.163.30/sdor/csp/logon.csp?LANGID=1', browser="Chrome", options=options, executable_path='')
#Borramos cualquier cookie que contega chrome para vaciar la memoria cache 
browser.delete_all_cookies()
#Ingresar el usuario y contraseña 
usuario = ''
userpass = ''
browser.input_text(locator='id:USERNAME', text=usuario)
browser.input_text(locator='id:PASSWORD', text=userpass)
browser.click_button(locator=BotonLogon)

#Seleccion el perfil de interconsulta
browser.click_element(locator=AdmisionAmbulatoria)
#Cambiamos al menu de TrakCare
browser.unselect_frame()
browser.select_frame(locator=FrameMenu)
sleep(5)
browser.click_element(locator=RegitroPaciente)
browser.unselect_frame()
#Cambiamos al area central de TrakCare
browser.select_frame(locator=FrameMain)
sleep(5)
#Llegando a los 100 registros cerrará el navegador y lo volverá abrir, recorrerá el dataframe utilizando la columna del rut
limite=100
for index, row in df.iterrows():
    print(str(index), end='\r')
    if(index >= limite):
        #Cuando se llega al limite de 100 registro cerramos el navegador y lo vovlemos abrir, esto por motivo de llenado de la cache de chrome
        limite+=100
        print("Cerrando navegador")
        browser.unselect_frame()
        browser.select_frame(locator=FrameMenu)
        browser.click_element(locator=BotonLogout)
        browser.handle_alert()
        browser.close_all_browsers()
        sleep(10)
        browser = Selenium()
        browser.auto_close=False
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Tiempo inicio =", current_time)

        #Login en TrakCare
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        #Agregar la ruta donde está el chromedrive en executable_path
        browser.open_browser('http://10.8.163.30/sdor/csp/logon.csp?LANGID=1', browser="Chrome", options=options,  executable_path='')
        
        browser.delete_all_cookies()
        usuario = ''
        userpass = ''
        browser.input_text(locator='id:USERNAME', text=usuario)
        browser.input_text(locator='id:PASSWORD', text=userpass)
        browser.click_button(locator=BotonLogon)

       #Seleccion de perfil de interconsulta
        browser.click_element(locator=AdmisionAmbulatoria)

        browser.unselect_frame()
        browser.select_frame(locator=FrameMenu)
        sleep(5)
        browser.click_element(locator=RegitroPaciente)
        browser.unselect_frame()
        browser.select_frame(locator=FrameMain)
   
    rut = row['PAPMI_ID']
    if rut:
        browser.wait_until_page_contains_element(locator='id:NationalID', timeout=10)
        #Ingresara el rut a buscar
        browser.input_text(locator='id:NationalID', text=rut)
        browser.click_element(locator=BotonBuscar)
        try:
            #Enlace a número de registro
            browser.click_element(locator=NumeroRegistro)
            sleep(5)
            #Capturamos la previsión antes de actualizar
            salud =  browser.get_value(locator='//*[@id="INSTDesc"]')
            grupo =  browser.get_value(locator='//*[@id="AUXITDesc"]')
            prevision_antes = browser.get_value(locator='//*[@id="PAPERRemark"]')
            #Actualizamos la previsión
            browser.click_element(locator=ActualizarPrevision)
            #Capturamos la previsión después de ser actualizada
            prevision_despues = browser.get_value(locator='//*[@id="PAPERRemark"]')
            salud_actualizada =  browser.get_value(locator='//*[@id="INSTDesc"]')
            grupo_actualizada =  browser.get_value(locator='//*[@id="AUXITDesc"]')
            #Actualizamos los datos del paciente
            browser.click_button(locator=BotonActualizar)
            #Aceptamos la alerta
            browser.handle_alert()
            now = datetime.now()
            #Se generan los datos para agregar al registro del archivo de agendamiento
            fecha_actualizacion = now.strftime("%d-%m-%Y")
            hora_actualizacion = now.strftime("%H:%M:%S")
            reporte_prevision = Reporte(row['PAPMI_ID'], row['PAPER_Name2'], row['PAPER_Name'], row['PAPER_Name3'], row['PAPER_PassportNumber'], row['CTPCP_Code'], 
                        row['CTPCP_Desc'], row['SER_Desc'], row['APPT_DateComp'], row['APPT_TimeComp'])
            reporte_prevision.reporte_prevision_actualizada(salud, grupo, salud_actualizada, grupo_actualizada, fecha_actualizacion, hora_actualizacion)
            #Volvemos al menu para buscar otro registro
            browser.unselect_frame()
            browser.select_frame(locator=FrameMenu)
            sleep(5)
            browser.click_element(locator='//*[@id="MainMenuLinksHome"]')
            browser.click_element(locator=RegitroPaciente)
            browser.unselect_frame()
            browser.select_frame(locator=FrameMain)
        #En caso de alerta al momento de buscar, hay un tipo de alerta    
        except UnexpectedAlertPresentException as mensaje:
            tipo_alerta=str(mensaje.alert_text).strip()
            #Si el paciente este fallecido
            if tipo_alerta == alerta_fallecido:
                #Generación de paciente fallecido
                reporte_fallecido = Reporte(row['PAPMI_ID'], row['PAPER_Name2'], row['PAPER_Name'], row['PAPER_Name3'], row['PAPER_PassportNumber'], row['CTPCP_Code'], 
                            row['CTPCP_Desc'], row['SER_Desc'], row['APPT_DateComp'], row['APPT_TimeComp'])
                reporte_fallecido.reporte_paciente_alerta_fallecido(tipo_alerta)
            #Alerta que arroja el sistema de acuerdo a FONASA
            elif alerta_fonasa in tipo_alerta:
                #Generación de reporte con alerta de FONASA
                reporte_fonasa = Reporte(row['PAPMI_ID'], row['PAPER_Name2'], row['PAPER_Name'], row['PAPER_Name3'], row['PAPER_PassportNumber'], row['CTPCP_Code'], 
                            row['CTPCP_Desc'], row['SER_Desc'], row['APPT_DateComp'], row['APPT_TimeComp'])
                reporte_fonasa.reporte_paciente_alerta_fonasa(tipo_alerta)
            else:
                #Alertas que son ditintas a las anteriores, como cambio de sexo o nombre
                reporte_otras = Reporte(row['PAPMI_ID'], row['PAPER_Name2'], row['PAPER_Name'], row['PAPER_Name3'], row['PAPER_PassportNumber'], row['CTPCP_Code'], 
                            row['CTPCP_Desc'], row['SER_Desc'], row['APPT_DateComp'], row['APPT_TimeComp'])
                reporte_otras.reporte_otras_alertas(tipo_alerta)
            #Volvemos al menu para continuar con el siguinte
            browser.unselect_frame()
            browser.select_frame(locator='id:eprmenu')
            sleep(5)
            browser.click_element(locator='//*[@id="MainMenuLinksHome"]')
            browser.click_element(locator='id:MainMenuItem52767')
            browser.unselect_frame()
            browser.select_frame(locator='id:TRAK_main')
            continue
    #En caso que no tenga rut el registro, se agrega a un reporte de personas sin rut pero con pasaporte.  
    else:
        reporte_sin_rut = Reporte(row['PAPMI_ID'], row['PAPER_Name2'], row['PAPER_Name'], row['PAPER_Name3'], row['PAPER_PassportNumber'], row['CTPCP_Code'], 
                            row['CTPCP_Desc'], row['SER_Desc'], row['APPT_DateComp'], row['APPT_TimeComp'])
        reporte_sin_rut.reporte_paciente_sin_rut()

#Logout de TrakCare
sleep(5)
browser.unselect_frame()
browser.select_frame(locator=FrameMenu)
browser.click_element(locator=BotonLogout)
browser.handle_alert()
browser.close_all_browsers()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Finalizo a las: ", current_time)

#Preparacion del archivo a ser enviado por email
print("Inicio de envio de archivos...")
total_registros = str(index)
fecha_actual = datetime.now().strftime('%d-%m-%Y')
Emailcrs.envio_de_archivos(fecha_actual, total_registros)
print("Finalizado envio de archivos")
print("Inicia la subida de archivos")


