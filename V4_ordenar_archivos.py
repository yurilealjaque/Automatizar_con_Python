import os
# Permite trabajar con el sistema operativo:
# crear carpetas, revisar archivos, unir rutas, listar contenido, etc.

import shutil
# Sirve para mover, copiar y administrar archivos y carpetas.

import getpass
# Permite obtener información del usuario actual del sistema operativo.

import time
# Se usa para manejar pausas de tiempo, por ejemplo time.sleep().

import threading
# Permite ejecutar tareas en hilos (threads).
# En este caso se usa para que la vigilancia corra en segundo plano
# mientras la ventana gráfica sigue funcionando.

from tkinter import Tk, filedialog, Button, Label
# Tk: crea la ventana principal.
# filedialog: abre el explorador para seleccionar carpetas.
# Button: crea botones en la interfaz.
# Label: crea textos visibles en la interfaz.

from datetime import datetime
# Permite trabajar con fechas y horas.

from watchdog.observers import Observer
# Observer es el “vigilante” que observa la carpeta en tiempo real.

from watchdog.events import FileSystemEventHandler
# Clase base que permite reaccionar a eventos del sistema de archivos,
# como por ejemplo cuando se crea un archivo nuevo.


usuario = getpass.getuser()
# Obtiene el nombre del usuario actual del computador.
# Esto se usa después para registrar en el log quién ejecutó el programa.


# Ruta donde están los archivos a ordenar
# ruta = "C:/Users/juanm/Desktop/auto_python"
# Esta línea está comentada.
# Significa que en vez de dejar una ruta fija escrita manualmente,
# el programa le pedirá al usuario que seleccione una carpeta.


# Crear carpetas en destino si no existen
# tipos = ["Imágenes", "PDFs", "Videos", "Documentos_Word", "Documentos_txt"]
# Esta lista también quedó comentada.
# Probablemente era una idea inicial para definir las carpetas manualmente,
# pero luego se reemplazó por el diccionario "extensiones".


ventana = Tk()
# Crea la ventana principal de Tkinter.

ventana.withdraw()
# Oculta temporalmente la ventana principal.
# Esto se hace para que primero aparezca solo el selector de carpeta
# y no una ventana vacía detrás.


ruta = filedialog.askdirectory(title="Seleccione la carpeta a ordenar")
# Abre una ventana del explorador para que el usuario elija la carpeta.
# La ruta seleccionada se guarda en la variable "ruta".


extensiones = {
    ".jpg": "Imágenes",
    ".png": "Imágenes",
    ".pdf": "PDFs",
    ".mp4": "Videos",
    ".docx": "Documentos_Word",
    ".txt": "Documentos_txt"
}
# Este diccionario define la lógica de clasificación del programa.
# La clave es la extensión del archivo.
# El valor es el nombre de la carpeta donde se moverá ese archivo.
#
# Ejemplo:
# si el archivo termina en ".pdf", irá a la carpeta "PDFs".
#
# Esto hace que el programa pueda decidir rápidamente
# dónde guardar cada archivo según su tipo.


def esperar_archivo_libre(ruta_archivo, intentos=10, espera=0.5):
    # Esta función verifica si un archivo está libre para ser usado.
    # Es útil porque un archivo recién creado puede estar todavía:
    # - copiándose,
    # - abierto por otro programa,
    # - bloqueado por el sistema.
    #
    # Parámetros:
    # ruta_archivo: ruta completa del archivo a comprobar.
    # intentos: número máximo de veces que intentará abrirlo.
    # espera: tiempo de espera entre intentos.

    for _ in range(intentos):
        # Repite el intento varias veces.
        # "_" significa que el contador no se usará directamente.

        try:
            with open(ruta_archivo, "rb"):
                # Intenta abrir el archivo en modo lectura binaria.
                # Si se logra abrir, se asume que el archivo ya está disponible.
                return True

        except (PermissionError, OSError):
            # Si aparece alguno de estos errores, significa que
            # probablemente el archivo sigue en uso o todavía no está listo.
            time.sleep(espera)
            # Espera un poco antes de volver a intentarlo.

    return False
    # Si después de todos los intentos no se pudo abrir,
    # la función devuelve False.


def ordenar_archivos(ruta):
    # Esta función recorre todos los elementos de la carpeta seleccionada
    # y organiza los archivos según:
    # 1) su extensión
    # 2) su fecha de última modificación

    for archivo in os.listdir(ruta):
        # os.listdir(ruta) devuelve todo lo que hay dentro de la carpeta:
        # archivos y subcarpetas.
        # "archivo" será el nombre de cada elemento encontrado.

        ruta_archivo = os.path.join(ruta, archivo)
        # Une la ruta base con el nombre del archivo.
        #
        # Ejemplo:
        # ruta = "C:/MisArchivos"
        # archivo = "foto.jpg"
        # resultado = "C:/MisArchivos/foto.jpg"

        if os.path.isfile(ruta_archivo) and archivo != "log_movimientos.txt":
            # Aquí se verifica:
            # 1) que el elemento sea realmente un archivo y no una carpeta
            # 2) que no sea el archivo de log
            #
            # ¿Por qué excluye el log?
            # Porque el programa genera ese archivo de registro y no tiene sentido
            # que intente moverlo también.

            if not esperar_archivo_libre(ruta_archivo):
                # Si el archivo no está libre, entra aquí.

                print(f"No se pudo acceder a {archivo} porque está siendo utilizado")
                # Muestra un mensaje en consola avisando que el archivo está bloqueado.

                continue
                # Salta al siguiente archivo sin seguir procesando este.

            nombre, ext = os.path.splitext(archivo)
            # Divide el nombre del archivo en dos partes:
            # nombre: la parte antes de la extensión
            # ext: la extensión, por ejemplo ".pdf"

            ext = ext.lower()
            # Convierte la extensión a minúsculas.
            # Esto evita problemas si el archivo viene como ".JPG", ".Pdf", etc.

            if ext in extensiones:
                # Comprueba si la extensión del archivo existe dentro del diccionario.
                # Solo si la encuentra, el archivo será organizado.

                fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
                # os.path.getmtime(ruta_archivo) devuelve la fecha de última modificación
                # del archivo en formato timestamp.
                # datetime.fromtimestamp(...) la convierte a una fecha legible.

                subcarpeta_fecha = fecha_mod.strftime("%Y-%m")
                # Convierte la fecha al formato año-mes.
                #
                # Ejemplo:
                # si el archivo fue modificado en abril de 2025,
                # el resultado será "2025-04"

                carpeta_tipo = os.path.join(ruta, extensiones[ext])
                # Construye la ruta de la carpeta principal según el tipo de archivo.
                #
                # Ejemplo:
                # si ext = ".pdf", extensiones[ext] = "PDFs"
                # resultado: "C:/MisArchivos/PDFs"

                carpeta_fecha = os.path.join(carpeta_tipo, subcarpeta_fecha)
                # Construye la subcarpeta por fecha.
                #
                # Ejemplo:
                # "C:/MisArchivos/PDFs/2025-04"

                if not os.path.exists(carpeta_fecha):
                    # Verifica si la carpeta de destino aún no existe.

                    os.makedirs(carpeta_fecha)
                    # Si no existe, la crea.
                    # makedirs puede crear toda la ruta necesaria.

                destino = os.path.join(carpeta_fecha, archivo)
                # Construye la ruta final donde quedará el archivo.
                #
                # Ejemplo:
                # "C:/MisArchivos/PDFs/2025-04/documento.pdf"

                shutil.move(ruta_archivo, destino)
                # Mueve físicamente el archivo desde su ubicación actual
                # hacia la nueva carpeta de destino.

                with open(os.path.join(ruta, "log_movimientos.txt"), "a", encoding="utf-8") as log:
                    # Abre el archivo log_movimientos.txt en modo append ("a").
                    # Si no existe, se crea.
                    # Si existe, agrega nuevas líneas al final.
                    # encoding="utf-8" permite manejar bien tildes y caracteres especiales.

                    log.write(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Movido: {archivo} -> {destino}\n"
                    )
                    # Escribe en el log:
                    # - fecha y hora actual
                    # - usuario del sistema
                    # - archivo movido
                    # - ruta de destino
                    #
                    # Esto deja un registro histórico de cada movimiento.


class ManejadorEventos(FileSystemEventHandler):
    # Esta clase hereda de FileSystemEventHandler.
    # Eso significa que puede “escuchar” eventos del sistema de archivos
    # y reaccionar cuando algo ocurra en la carpeta observada.

    def on_created(self, event):
        # Este método se ejecuta automáticamente cuando se crea
        # un nuevo elemento en la carpeta vigilada.

        if not event.is_directory:
            # Verifica que el elemento creado NO sea una carpeta.
            # Solo nos interesa reaccionar cuando aparece un archivo nuevo.

            print(f"Nuevo archivo detectado: {event.src_path}")
            # Muestra en consola la ruta del nuevo archivo detectado.

            ordenar_archivos(ruta)
            # Cada vez que llega un archivo nuevo,
            # vuelve a llamar a la función principal para organizarlo.


for carpeta in set(extensiones.values()):
    # extensiones.values() devuelve los nombres de las carpetas destino:
    # "Imágenes", "PDFs", "Videos", etc.
    #
    # set(...) elimina duplicados.
    # Esto es importante porque "Imágenes" aparece dos veces
    # (para .jpg y .png), y no queremos intentar crearla dos veces.

    ruta_carpeta = os.path.join(ruta, carpeta)
    # Construye la ruta completa de cada carpeta principal.

    if not os.path.exists(ruta_carpeta):
        # Si la carpeta no existe todavía...

        os.makedirs(ruta_carpeta)
        # ...la crea.


ordenar_archivos(ruta)
# Ejecuta una organización inicial.
# Esto significa que antes de empezar a vigilar en tiempo real,
# el programa ordena primero todos los archivos que ya estaban en la carpeta.


manejador_eventos = ManejadorEventos()
# Crea una instancia de la clase que manejará los eventos detectados.

observador = Observer()
# Crea el objeto Observer.
# Este será el vigilante que estará atento a la carpeta.

observador.schedule(manejador_eventos, ruta, recursive=False)
# Le dice al observador:
# - qué manejador de eventos usar
# - qué carpeta vigilar
# - recursive=False: que no vigile las subcarpetas internas
#
# O sea, solo vigila la carpeta principal seleccionada.


def iniciar_Vigilancia():
    # Esta función inicia el observador.
    # Se separa en una función para poder ejecutarla dentro de un hilo.

    observador.start()
    # Pone al observador a trabajar.
    # Desde este momento empieza la vigilancia en tiempo real.


def detener_vigilancia():
    # Esta función detiene el sistema de vigilancia y cierra la aplicación.

    observador.stop()
    # Le indica al observador que deje de vigilar.

    observador.join()
    # Espera a que el observador termine correctamente.
    # Esto evita cierres bruscos del hilo del observer.

    ventana.quit()
    # Cierra el bucle principal de la ventana gráfica.
    # En la práctica, hace que la aplicación se cierre.


ventana.deiconify()
# Vuelve a mostrar la ventana principal.
# Antes estaba oculta por withdraw().

ventana.title("Vigilancia de carpeta")
# Define el título que aparecerá en la barra superior de la ventana.

ventana.geometry("400x150")
# Define el tamaño inicial de la ventana:
# 400 píxeles de ancho por 150 de alto.


Label(ventana, text=f"Vigilando la carpeta: \n{ruta}", wraplength=350).pack(pady=10)
# Crea una etiqueta de texto en la ventana.
# Muestra al usuario qué carpeta está siendo vigilada.
#
# \n genera un salto de línea.
# wraplength=350 hace que el texto se ajuste si la ruta es muy larga.
# .pack(pady=10) coloca el elemento en la ventana con un margen vertical de 10.

Button(ventana, text="Detener vigilancia y salir", command=detener_vigilancia).pack(pady=10)
# Crea un botón en la ventana.
# Cuando el usuario hace clic, se ejecuta la función detener_vigilancia.
# Es decir:
# - se detiene el observer
# - se espera a que termine
# - se cierra la ventana


hilo_vigilancia = threading.Thread(target=iniciar_Vigilancia, daemon=True)
# Crea un hilo secundario que ejecutará iniciar_Vigilancia.
#
# ¿Por qué usar un hilo?
# Porque si observador.start() corriera directamente en el hilo principal,
# podría interferir con la interfaz gráfica.
#
# target=iniciar_Vigilancia:
# indica qué función ejecutará el hilo.
#
# daemon=True:
# significa que este hilo es “daemon”, o sea, está subordinado al programa principal.
# Si la aplicación principal termina, este hilo también se cerrará.

hilo_vigilancia.start()
# Inicia el hilo secundario.
# Desde este momento, la vigilancia corre en segundo plano.


ventana.mainloop()
# Inicia el bucle principal de la interfaz gráfica.
# Esto mantiene la ventana abierta y esperando interacción del usuario.
#
# Mientras esta línea está ejecutándose:
# - la ventana sigue viva
# - el botón funciona
# - el hilo de vigilancia sigue observando la carpeta