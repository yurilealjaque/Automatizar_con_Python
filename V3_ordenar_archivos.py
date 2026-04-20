import os                 # Permite trabajar con carpetas, archivos y rutas del sistema operativo
import shutil             # Permite mover, copiar y gestionar archivos
import getpass            # Permite obtener información del usuario actual del sistema
import time               # Permite usar pausas de tiempo, por ejemplo sleep()

from tkinter import Tk, filedialog                 # Tk crea una ventana; filedialog permite abrir el selector de carpetas
from datetime import datetime                      # Permite trabajar con fechas y horas
from watchdog.observers import Observer            # Observa cambios en una carpeta en tiempo real
from watchdog.events import FileSystemEventHandler # Maneja eventos del sistema de archivos, por ejemplo cuando se crea un archivo

usuario = getpass.getuser()  # Guarda el nombre del usuario actual del computador

# Ruta donde están los archivos a ordenar
# ruta = "C:/Users/juanm/Desktop/auto_python"

# Crear carpetas en destino si no existen
# tipos = ["Imágenes", "PDFs", "Videos", "Documentos_Word", "Documentos_txt"]

ventana = Tk()           # Crea una ventana principal de Tkinter
ventana.withdraw()       # Oculta la ventana principal para que no aparezca una ventana vacía

ruta = filedialog.askdirectory(title="Seleccione la carpeta a ordenar")
# Abre una ventana para que el usuario seleccione la carpeta que desea organizar
# La ruta elegida se guarda en la variable "ruta"

extensiones = {
    ".jpg": "Imágenes",           # Si el archivo termina en .jpg, irá a la carpeta "Imágenes"
    ".png": "Imágenes",           # Si termina en .png, también irá a "Imágenes"
    ".pdf": "PDFs",               # Si termina en .pdf, irá a la carpeta "PDFs"
    ".mp4": "Videos",             # Si termina en .mp4, irá a la carpeta "Videos"
    ".docx": "Documentos_Word",   # Si termina en .docx, irá a "Documentos_Word"
    ".txt": "Documentos_txt"      # Si termina en .txt, irá a "Documentos_txt"
}
# Este diccionario funciona como una tabla de equivalencia:
# extensión del archivo -> carpeta de destino


def esperar_archivo_libre(ruta_archivo, intentos=10, espera=0.5):
    # Esta función intenta comprobar si un archivo está libre
    # Es útil cuando un archivo recién fue creado o aún está abierto por otro programa

    for _ in range(intentos):
        # Repite el intento varias veces
        # range(intentos) genera una secuencia desde 0 hasta intentos-1
        # "_" se usa cuando no necesitamos el valor del contador

        try:
            with open(ruta_archivo, "rb"):
                # Intenta abrir el archivo en modo lectura binaria ("rb")
                # Si logra abrirlo, significa que el archivo está disponible
                return True

        except (PermissionError, OSError):
            # Si ocurre un error de permisos o del sistema operativo,
            # probablemente el archivo aún está en uso o no está completamente listo
            time.sleep(espera)
            # Espera una pequeña cantidad de tiempo antes de volver a intentarlo

    return False
    # Si después de todos los intentos no se pudo abrir,
    # la función devuelve False


def ordenar_archivos(ruta):
    # Esta función recorre todos los archivos de la carpeta seleccionada
    # y los mueve a subcarpetas según su extensión y fecha de modificación

    for archivo in os.listdir(ruta):
        # os.listdir(ruta) devuelve todos los elementos dentro de la carpeta:
        # archivos y subcarpetas
        # "archivo" es el nombre de cada elemento encontrado

        ruta_archivo = os.path.join(ruta, archivo)
        # Une la ruta de la carpeta con el nombre del archivo
        # Ejemplo: "C:/carpeta" + "foto.jpg" -> "C:/carpeta/foto.jpg"

        if os.path.isfile(ruta_archivo) and archivo != "log_movimientos.txt":
            # Verifica dos cosas:
            # 1) Que realmente sea un archivo y no una carpeta
            # 2) Que no sea el archivo de log, para evitar moverlo también

            if not esperar_archivo_libre(ruta_archivo):
                # Si el archivo NO está libre, entra aquí
                print(f"No se pudo acceder a {archivo} porque está siendo utilizado")
                # Muestra un mensaje indicando que el archivo está ocupado
                continue
                # Salta al siguiente archivo del bucle, sin procesar este

            nombre, ext = os.path.splitext(archivo)
            # Divide el nombre del archivo en dos partes:
            # nombre -> parte antes de la extensión
            # ext -> extensión, por ejemplo ".pdf"

            ext = ext.lower()
            # Convierte la extensión a minúsculas
            # Así evita problemas si viene como ".JPG" o ".Pdf"

            if ext in extensiones:
                # Comprueba si la extensión del archivo está registrada
                # en el diccionario "extensiones"

                # Obtener la fecha de última modificación
                fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
                # os.path.getmtime(ruta_archivo) obtiene la fecha de modificación en formato timestamp
                # datetime.fromtimestamp(...) la convierte a una fecha legible de Python

                subcarpeta_fecha = fecha_mod.strftime("%Y-%m")
                # Convierte la fecha a formato "año-mes"
                # Ejemplo: abril de 2025 -> "2025-04"

                # Crear la subcarpeta si no existe
                carpeta_tipo = os.path.join(ruta, extensiones[ext])
                # Construye la ruta de la carpeta principal por tipo
                # Ejemplo: "C:/Archivos/Imágenes"

                carpeta_fecha = os.path.join(carpeta_tipo, subcarpeta_fecha)
                # Construye la subcarpeta por fecha
                # Ejemplo: "C:/Archivos/Imágenes/2025-04"

                if not os.path.exists(carpeta_fecha):
                    # Verifica si esa carpeta aún no existe
                    os.makedirs(carpeta_fecha)
                    # Si no existe, la crea
                    # makedirs puede crear carpetas intermedias si hace falta

                # Ruta destino final
                destino = os.path.join(carpeta_fecha, archivo)
                # Construye la ruta completa donde se moverá el archivo
                # Ejemplo: "C:/Archivos/Imágenes/2025-04/foto.jpg"

                shutil.move(ruta_archivo, destino)
                # Mueve físicamente el archivo desde su ubicación actual al destino

                with open(os.path.join(ruta, "log_movimientos.txt"), "a", encoding="utf-8") as log:
                    # Abre (o crea si no existe) un archivo log llamado "log_movimientos.txt"
                    # "a" significa modo append: agrega información al final sin borrar lo anterior
                    # encoding="utf-8" asegura compatibilidad con tildes y caracteres especiales

                    log.write(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Movido: {archivo} -> {destino}\n"
                    )
                    # Escribe una línea en el log con:
                    # - fecha y hora actual
                    # - usuario del sistema
                    # - nombre del archivo movido
                    # - ruta de destino


class ManejadorEventos(FileSystemEventHandler):
    # Esta clase hereda de FileSystemEventHandler
    # Sirve para reaccionar cuando ocurren eventos en la carpeta observada

    def on_created(self, event):
        # Este método se ejecuta automáticamente cuando se crea un nuevo elemento
        # dentro de la carpeta vigilada

        if not event.is_directory:
            # Verifica que lo creado no sea una carpeta
            # Solo nos interesa reaccionar cuando aparece un archivo nuevo

            print(f"Nuevo archivo detectado: {event.src_path}")
            # Muestra en pantalla la ruta del nuevo archivo detectado

            ordenar_archivos(ruta)
            # Cada vez que aparece un archivo nuevo,
            # vuelve a ejecutar el proceso de ordenación


for carpeta in set(extensiones.values()):
    # extensiones.values() devuelve los nombres de carpetas destino:
    # "Imágenes", "PDFs", etc.
    # set(...) elimina duplicados, porque "Imágenes" aparece más de una vez

    ruta_carpeta = os.path.join(ruta, carpeta)
    # Construye la ruta completa para cada carpeta destino

    if not os.path.exists(ruta_carpeta):
        # Si la carpeta aún no existe
        os.makedirs(ruta_carpeta)
        # La crea


ordenar_archivos(ruta)
# Ejecuta una primera organización de todos los archivos
# que ya estaban dentro de la carpeta antes de iniciar la vigilancia

manejador_eventos = ManejadorEventos()
# Crea un objeto de la clase que manejará los eventos

observador = Observer()
# Crea el observador que vigilará la carpeta

observador.schedule(manejador_eventos, ruta, recursive=False)
# Le indica al observador:
# - qué manejador usar
# - qué carpeta vigilar
# - recursive=False significa que solo vigila esa carpeta,
#   no las subcarpetas internas

observador.start()
# Inicia la vigilancia en tiempo real

print(f"Vigilando la carpeta: {ruta}")
# Muestra qué carpeta se está observando

print("Presiona Ctrl+C para detener el programa")
# Instrucción para detener manualmente el programa desde consola

try:
    # Se usa try para poder capturar la interrupción del usuario con Ctrl+C

    while True:
        # Bucle infinito para mantener el programa en ejecución
        time.sleep(1)
        # Espera 1 segundo en cada vuelta
        # Esto evita que el programa consuma recursos innecesariamente

except KeyboardInterrupt:
    # Se ejecuta cuando el usuario presiona Ctrl+C

    print("Deteniendo vigilancia")
    # Mensaje de cierre

    observador.stop()
    # Detiene el observador

observador.join()
# Espera a que el hilo del observador termine correctamente antes de cerrar el programa