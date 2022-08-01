#Archivo de coneccion hacia la base de datos de trakcare de respaldo
#Todos estos datos se deben solicitar a TrakCare
import jaydebeapi

def connectar():
    url = ""
    driver = ''
    user = ""
    password = ""
    jarfile = ""

    try:
        conn = jaydebeapi.connect(driver, url, [user, password], jarfile)
        return conn
    except:
        print(conn)


