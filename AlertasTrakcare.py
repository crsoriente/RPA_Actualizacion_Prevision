#Gestion de las disitnas alertas de Trakcare
from RPA.Browser.Selenium import *
from selenium.common.exceptions import UnexpectedAlertPresentException
from logs import Logs
from datetime import datetime


class Alertastrakcare:
    #En caso de paciente fallecido
    def alerta_paciente_fallecido(browser):
        print("Paciente fallecido")
        browser.click_element(locator='xpath://*[@id="find1"]')
        browser.handle_alert()
        browser.click_element(locator='id:RegistrationNoz1')
        browser.handle_alert()
        salud =  browser.get_value(locator='//*[@id="INSTDesc"]')
        grupo =  browser.get_value(locator='//*[@id="AUXITDesc"]')
        prevision_antes = browser.get_value(locator='//*[@id="PAPERRemark"]')
        browser.click_element(locator='//*[@id="AccordionContentPAPerson.Edit6"]/table/tbody/tr[4]/td[2]/a')
        browser.click_button(locator='//*[@id="update1"]')
        browser.handle_alert()

    #En caso de alerta fonasa
    def alerta_paciente_fonasa(browser, rut):
        alerta_falta ='Error al guardar registro de paciente: Paciente debe tener'
        browser.alert_should_not_be_present()
        print("Paciente fonasa")
        browser.click_element(locator='//*[@id="AccordionContentPAPerson.Edit6"]/table/tbody/tr[4]/td[2]/a')
        browser.handle_alert()
        browser.click_button(locator='//*[@id="update1"]')
        mensaje=browser.handle_alert()
        if alerta_falta in mensaje:
            browser.unselect_frame()
            browser.select_frame(locator='id:eprmenu')
            browser.click_element(locator='//*[@id="MainMenuLinksHome"]')
            now = datetime.now()
            current_time = now.strftime("%d-%m-%Y %H:%M:%S") 
            Logs.log_rut_alerta(rut, mensaje, current_time)
    
    #En alerta en caso de actualizacion de telefono
    def alerta_actualizar_telefono(browser, rut, mensaje):
        browser.alert_should_not_be_present()
        mensaje = str(mensaje)
        browser.click_element(locator='//*[@id="AccordionContentPAPerson.Edit6"]/table/tbody/tr[4]/td[2]/a')
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M:%S") 
        Logs.log_rut_alerta(rut, mensaje, current_time)
        
       
        
