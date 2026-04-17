import os
import shutil
import getpass
from tkinter import Tk, filedialog
from datetime import datetime

# 1. IDENTIFICACIÓN DEL USUARIO
# getpass.getuser() obtiene el nombre de usuario de la sesión actual de Windows/Linux/Mac.
usuario = getpass.getuser() 

# 2. SELECCIÓN DE CARPETA MEDIANTE INTERFAZ GRÁFICA
# Creamos una instancia de Tkinter pero la ocultamos (withdraw) para que no se abra una ventana vacía.
ventana = Tk()
ventana.withdraw()

# Abre un cuadro de diálogo para que el usuario elija físicamente la carpeta a organizar.
ruta = filedialog.askdirectory(title="Seleccione la carpeta a organizar")

# 3. DICCIONARIO DE CONFIGURACIÓN
# Definimos qué extensión corresponde a qué tipo de carpeta. Facilita añadir nuevos tipos después.
extensiones = {
    ".jpg": "Imágenes",
    ".png": "Imágenes",
    ".pdf": "PDFs",
    ".mp4": "Vídeos",
    ".docx": "Documentos_Word",
    ".txt": "Documentos_txt"
}

# 4. CREACIÓN DE CARPETAS PRINCIPALES
# 'set(extensiones.values())' extrae los nombres de las carpetas sin repetir (Imágenes, PDFs, etc.)
for carpeta in set(extensiones.values()):
    ruta_carpeta = os.path.join(ruta, carpeta)
    
    # Si la carpeta (ej. "Imágenes") no existe en la ruta elegida, la crea.
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# 5. PROCESAMIENTO DE ARCHIVOS
# Listamos todo el contenido de la carpeta seleccionada.
for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    
    # Validamos que sea un archivo y no una carpeta para evitar errores.
    if os.path.isfile(ruta_archivo):
        # Separamos el nombre de la extensión (ej: 'foto', '.jpg')
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower() # Convertimos a minúsculas para que coincida con nuestro diccionario.
        
        # Si la extensión del archivo está en nuestro diccionario de configuración:
        if ext in extensiones:
            
            # 6. ORGANIZACIÓN POR FECHA (SUB-CARPETAS)
            # Obtenemos la fecha de última modificación del archivo físico.
            fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
            # Creamos un nombre de subcarpeta basado en año y mes (ej: "2024-05").
            subcarpeta_fecha = fecha_mod.strftime("%Y-%m") 

            # Definimos la ruta de la carpeta del tipo (ej: .../PDFs) y la subcarpeta de fecha.
            carpeta_tipo = os.path.join(ruta, extensiones[ext])
            carpeta_fecha = os.path.join(carpeta_tipo, subcarpeta_fecha)

            # Si la subcarpeta por fecha no existe dentro de la carpeta de tipo, la crea.
            if not os.path.exists(carpeta_fecha):
                os.makedirs(carpeta_fecha)

            # 7. MOVIMIENTO FINAL
            # Definimos la ruta completa de destino incluyendo el nombre del archivo.
            destino = os.path.join(carpeta_fecha, archivo)
            
            # Movemos el archivo desde su origen a la nueva carpeta organizada.
            shutil.move(ruta_archivo, destino)

            # 8. REGISTRO DE ACTIVIDAD (LOG)
            # Abrimos (o creamos) un archivo .txt en modo 'append' (a) para añadir líneas sin borrar lo anterior.
            with open(os.path.join(ruta, "log_movimientos.txt"), "a", encoding="utf-8") as log: 
                # Registramos: Fecha/Hora actual - Usuario que lo hizo - Qué archivo se movió y hacia dónde.
                log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Movido: {archivo} -> {destino}\n")