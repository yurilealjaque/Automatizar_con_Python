import os
# Importa el módulo os, que permite interactuar con el sistema operativo.
# Aquí se usa para:
# - listar archivos dentro de una carpeta
# - unir rutas
# - separar nombre y extensión
# - renombrar archivos


carpeta = "C:/Users/"
# Guarda en una variable la ruta de la carpeta donde están los archivos.
# Esa será la carpeta que el programa va a revisar.


prefijo = "imagen_"
# Define el texto base que tendrán los nuevos nombres.
# Por ejemplo: imagen_001.jpg, imagen_002.png, etc.


extensiones = (".jpg", ".png")
# Crea una tupla con las extensiones permitidas.
# El programa solo procesará archivos que terminen en .jpg o .png.


archivos = []
# Crea una lista vacía.
# Aquí se van a guardar los nombres de los archivos que sí cumplan la condición.


for f in os.listdir(carpeta):
    # Recorre todos los elementos dentro de la carpeta.
    # os.listdir(carpeta) devuelve una lista con los nombres de archivos y carpetas.
    # En cada vuelta del bucle, "f" representa uno de esos nombres.

    if f.endswith(extensiones):
        # Verifica si el nombre del archivo termina en alguna de las extensiones
        # indicadas en la tupla: ".jpg" o ".png".
        #
        # endswith() puede recibir una tupla de sufijos,
        # por eso funciona bien para revisar varios tipos de archivo a la vez.

        archivos.append(f)
        # Si cumple la condición, agrega ese nombre de archivo a la lista "archivos".


for i, nombre_actual in enumerate(archivos, start=1):
    # Recorre la lista de archivos filtrados.
    #
    # enumerate() permite obtener dos cosas al mismo tiempo:
    # - i: un contador automático
    # - nombre_actual: el nombre del archivo actual
    #
    # start=1 hace que la numeración comience en 1 y no en 0.
    #
    # Ejemplo:
    # primera vuelta  -> i = 1, nombre_actual = "fotoA.jpg"
    # segunda vuelta  -> i = 2, nombre_actual = "fotoB.png"

    extension_actual = os.path.splitext(nombre_actual)[1]
    # Divide el nombre del archivo en dos partes:
    # - la parte antes del punto
    # - la extensión
    #
    # os.path.splitext("fotoA.jpg") devuelve:
    # ("fotoA", ".jpg")
    #
    # [1] significa que toma la segunda parte, o sea la extensión.
    #
    # Resultado:
    # extension_actual = ".jpg" o ".png"

    nuevo_nombre = f"{prefijo}{i:03}{extension_actual}"
    # Construye el nuevo nombre del archivo usando un f-string.
    #
    # prefijo        -> "imagen_"
    # i:03           -> formatea el número con 3 dígitos
    # extension_actual -> mantiene la extensión original
    #
    # Ejemplos:
    # i = 1  -> "001"
    # i = 7  -> "007"
    # i = 25 -> "025"
    #
    # Entonces, si i = 1 y la extensión es ".jpg":
    # nuevo_nombre = "imagen_001.jpg"

    ruta_actual = os.path.join(carpeta, nombre_actual)
    # Une la ruta de la carpeta con el nombre actual del archivo.
    #
    # Ejemplo:
    # carpeta = "C:/Users/juanm/Desktop/auto_python"
    # nombre_actual = "fotoA.jpg"
    #
    # Resultado:
    # ruta_actual = "C:/Users/juanm/Desktop/auto_python/fotoA.jpg"

    ruta_nueva = os.path.join(carpeta, nuevo_nombre)
    # Une la misma carpeta con el nuevo nombre que se quiere asignar.
    #
    # Ejemplo:
    # ruta_nueva = "C:/Users/juanm/Desktop/auto_python/imagen_001.jpg"

    os.rename(ruta_actual, ruta_nueva)
    # Renombra el archivo.
    # En la práctica:
    # - toma el archivo que está en ruta_actual
    # - le cambia el nombre al indicado en ruta_nueva
    #
    # Como la carpeta es la misma, realmente no lo mueve,
    # solo le cambia el nombre.