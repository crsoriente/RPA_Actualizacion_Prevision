#Generacion de reportes para ser enviados por email

from RPA.Excel.Files import Files
import os.path

class Reporte:

    def __init__(self, rut, nombre, apellido_paterno, apellido_materno, pasaporte, rut_profesional, nombre_profesional, servicio, fecha_cita, hora_cita):
        self.rut = rut
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.pasaporte = pasaporte
        self.rut_profesional = rut_profesional
        self.nombre_profesional = nombre_profesional
        self.servicio = servicio
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita 
    
    def reporte_paciente_alerta_fonasa(self, mensaje):
        #Agregar ruta donde se almacenaran los reprotes
        path=""
        workbook = "reporte_alerta_fonasa.xlsx"
        content=[[self.rut, self.nombre, self.apellido_paterno, self.apellido_materno, self.pasaporte, self.rut_profesional, self.nombre_profesional, self.servicio, self.fecha_cita, self.hora_cita, mensaje],]
        reporte = Files()
        cabecera_fonasa = [['RUT', 'NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'PASAPORTE', 'RUT PROFESIONAL', 'NOMBRE PROFESIONAL', 'SERVICIO', 'FECHA CITA', 'HORA CITA', 'MENSAJE'],]
        
        #Agregar la misma ruta que el path del archivo excel, de ser necesario
        if os.path.isfile("reporte_alerta_fonasa.xlsx"):
            
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
        else:
            reporte.create_workbook(path, fmt="xlsx")
            reporte.append_rows_to_worksheet(cabecera_fonasa)
            reporte.save_workbook(path+workbook)
            reporte.close_workbook()
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
    
    def reporte_paciente_alerta_fallecido(self, mensaje):
        path=""
        workbook = "reporte_paciente_fallecido.xlsx"
        content=[[self.rut, self.nombre, self.apellido_paterno, self.apellido_materno, self.pasaporte, self.rut_profesional, self.nombre_profesional, self.servicio, self.fecha_cita, self.hora_cita, mensaje],]
        reporte = Files()
        cabecera_fonasa = [['RUT', 'NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'PASAPORTE', 'RUT PROFESIONAL', 'NOMBRE PROFESIONAL', 'SERVICIO', 'FECHA CITA', 'HORA CITA', 'MENSAJE'],]

        if os.path.isfile("reporte_paciente_fallecido.xlsx"):
            
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
        else:
            reporte.create_workbook(path, fmt="xlsx")
            reporte.append_rows_to_worksheet(cabecera_fonasa)
            reporte.save_workbook(path+workbook)
            reporte.close_workbook()
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
    
    def reporte_paciente_sin_rut(self):
        path=""
        workbook = "reporte_paciente_sin_rut.xlsx"
        content=[[self.nombre, self.apellido_paterno, self.apellido_materno, self.pasaporte, self.rut_profesional, self.nombre_profesional, self.servicio, self.fecha_cita, self.hora_cita],]
        reporte = Files()
        cabecera_fonasa = [['NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'PASAPORTE', 'RUT PROFESIONAL', 'NOMBRE PROFESIONAL', 'SERVICIO', 'FECHA CITA', 'HORA CITA', 'MENSAJE'],]

        if os.path.isfile("reporte_paciente_sin_rut.xlsx"):
            
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
        else:
            reporte.create_workbook(path, fmt="xlsx")
            reporte.append_rows_to_worksheet(cabecera_fonasa)
            reporte.save_workbook(path+workbook)
            reporte.close_workbook()
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
    
    def reporte_prevision_actualizada(self, salud, grupo, salud_actualizada, grupo_actualizada, fecha_actualizacion, hora_actualizacion):
        
        path=""
        workbook = "reporte_prevision_actualizada.xlsx"
        prevision_antes = salud + " " + grupo
        prevision_actualizada = salud_actualizada + " " + grupo_actualizada
        content=[[self.rut, self.nombre, self.apellido_paterno, self.apellido_materno, self.pasaporte, prevision_antes, prevision_actualizada, fecha_actualizacion, hora_actualizacion],]
        reporte = Files()
        cabecera_fonasa = [['RUT', 'NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'PASAPORTE', 'PREVISION ANTES', 'PREVISION ACTUALIZADA', 'FECHA ACTUALIZACION', 'HORA ACTUALIZACION'],]

        if os.path.isfile("reporte_prevision_actualizada.xlsx"):
            
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
        else:
            reporte.create_workbook(path, fmt="xlsx")
            reporte.append_rows_to_worksheet(cabecera_fonasa)
            reporte.save_workbook(path+workbook)
            reporte.close_workbook()
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
    
    def reporte_otras_alertas(self, mensaje):
        
        path=""
        workbook = "reporte_otras_alertas.xlsx"
        content=[[self.rut, self.nombre, self.apellido_paterno, self.apellido_materno, self.pasaporte, self.rut_profesional, self.nombre_profesional, self.servicio, self.fecha_cita, self.hora_cita, mensaje],]
        reporte = Files()
        cabecera_fonasa = [['RUT', 'NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'PASAPORTE', 'RUT PROFESIONAL', 'NOMBRE PROFESIONAL', 'SERVICIO', 'FECHA CITA', 'HORA CITA', 'MENSAJE'],]

        if os.path.isfile("reporte_otras_alertas.xlsx"):
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
        else:
            reporte.create_workbook(path, fmt="xlsx")
            reporte.append_rows_to_worksheet(cabecera_fonasa)
            reporte.save_workbook(path+workbook)
            reporte.close_workbook()
            reporte.open_workbook(path+workbook)
            reporte.append_rows_to_worksheet(content)
            reporte.save_workbook()
            reporte.close_workbook()
        


