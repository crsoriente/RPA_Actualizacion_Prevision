#Obtención de los pacientes del día
from msilib.schema import Error
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from conexion import connectar

class Agendamiento:
    
    def get_agendamiento_una_fecha():
        connshadow = connectar()
        cursor = connshadow.cursor()
        now = datetime.now()
        tiempo_inicio = now.strftime("%H:%M:%S")
        fecha_actual = now.strftime("%Y-%m-%d")
        print("Inicio consulta: " + tiempo_inicio)
        fecha = (fecha_actual,)
        cursor.execute("""SELECT CTPCP_Code, CTPCP_Desc, SER_Desc, PAPMI_ID, PAPER_PassportNumber, PAPMI_Name2, PAPER_Name2, PAPER_Name, PAPER_Name3, APPT_AS_ParRef, APPT_RowId, APPT_ChildSub, APPT_AT_DR, APPT_PAPMI_DR, 
		                APPT_Status, APPT_Adm_DR, APPT_DateComp, APPT_TimeComp, APPT_LastUpdateHospital_DR 
                        FROM SQLUser.RB_Appointment
                        INNER JOIN PA_PatMas ON APPT_PAPMI_DR  = PA_PatMas.PAPMI_RowId1
                        INNER JOIN PA_Person ON PA_Person.PAPER_RowId  = PA_PatMas.PAPMI_PAPER_DR
                        INNER JOIN RBC_Services ON APPT_RBCServ_DR = RBC_Services.SER_RowId
                        JOIN CT_CareProv ON RBC_Services.SER_CTCP_DR = CT_CareProv.CTPCP_RowId1
                        WHERE APPT_LastUpdateHospital_DR= AND APPT_DateComp = ? """, fecha)

        patmas = cursor.fetchall()
        cursor.close()
        connshadow.close()
        now = datetime.now()
        tiempo_finalizacion = now.strftime("%H:%M:%S")
        print("Finalizacion consulta: " + tiempo_finalizacion)
        return patmas
    
    