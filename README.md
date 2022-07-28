# RPA Actualizacion Prevision
Desarrollado por el departamento TIC del CRS Cordillera Oriente

## Que hace este RPA?
RPA (Robotic Process Automation) es un robot programado para actualizar la previsión de los usuarios, de una institución de salud, buscando mantener actualizados los datos.
## Para que es util el RPA?
ES útil para mantener al día los datos de previsión de los usuarios de una institución de salud, utilizado el sistema de información hospitalario (HIS), simulando la interacción de un usuario con el sistema HIS.
## Requisitos
- Python: versión 3.8 en adelante
- Sistema Operativo: Windows 10 o Ubuntu 20.04 en adelante
- Librerías de Python
  - PIP:**instalación** https://pypi.org/project/pip/  **manual** https://pip.pypa.io/en/stable/installation/
  - RPA FRAMEWORK: https://rpaframework.org/ **pip install rpaframework==13.0.0**
  - JayDeBeApi: https://pypi.org/project/JayDeBeApi/ **pip install JayDeBeApi**
  - Pandas: https://pandas.pydata.org/ **pip install pandas**
  - Selenium: https://pypi.org/project/selenium/ **pip install selenium**
- Datos de usuario para acceder al sistema TrakCare con permisos de admisión ambulatoria
- Datos de usuario y contraseña para acceder a la base de datos de respaldo de TrakCare
## Instalación
1. Crear entorno virtual de python 
2. Realizar la instalación de las librerías mencionadas en los requisitos, con el comando PIP
3. Copiar los archivos dentro del entorno virtual
4. Configurar el archivo de conexion.py con los datos solicitados
5. Configurar la query SQL en obtener_pacientes.py con el código de establecimiento y fecha
6. Agregar los datos del usuario que se utilizara para ingresar a TrakCare
7. Configurar las rutas para los reportes de Excel en reporte.py
8. Configurar los datos de la cuenta que se utilizara para enviar los archivos y los usuarios que deben recibir los reportes en emailcrs.py






