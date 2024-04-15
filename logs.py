#Generacion de archivo de log para seguimeinto del funcionamiento del RPA
#Modificar la ruta de los archivos de ser necesario
import os.path
class Logs:
    
    def log_actualizar_prevision(rut, prevision_antes, prevision_despues, current_time, salud, grupo, salud_actualizada, grupo_actualizada):
        if os.path.isfile("actualizacion-prevision.txt"):
            f= open("actualizacion-prevision.txt","a")
            f.write("Rut: "+ rut + " Prevision Antes: "+ salud + " " + grupo + " " + prevision_antes + " - Prevision Actualizada: " + salud_actualizada + " "+ grupo_actualizada + " " + prevision_despues + "Tiempo finalizacion: " + current_time + "\n") 
            f.close()
        else:
            f= open("actualizacion-prevision.txt","w+")
            f.write("Rut: "+ rut + " Prevision Antes: "+ salud + " " + grupo + " " + prevision_antes + " - Prevision Actualizada: " + salud_actualizada + " "+ grupo_actualizada + " " + prevision_despues + "Tiempo finalizacion: " + current_time + "\n") 
            f.close()
    
    def log_rut_alerta(rut, mensaje, current_time) :
        if os.path.isfile("log-rut-con-alerta.txt"):
            f= open("log-rut-con-alerta.txt","a")
            f.write("Rut: "+ rut + "-Mensaje: "+ mensaje  + "-hora: " + current_time + "\n") 
            f.close()
        else:
            f= open("log-rut-con-alerta.txt","w+")
            f.write("Rut: "+ rut + "-Mensaje: "+ mensaje  + "-hora: " + current_time + "\n") 
            f.close()
    
    def log_rut_paciente_fallecido(rut, mensaje, current_time) :
        if os.path.isfile("log-rut-paciente_fallecido.txt"):
            f= open("log-rut-paciente_fallecido.txt","a")
            f.write("Rut: "+ rut + "-Mensaje: "+ mensaje  + "-Fecha y hora: " + current_time + "\n") 
            f.close()
        else:
            f= open("log-rut-paciente_fallecido.txt","w+")
            f.write("Rut: "+ rut + "- Mensaje: "+ mensaje  + "-Fecha y hora:" + current_time + "\n") 
            f.close()
