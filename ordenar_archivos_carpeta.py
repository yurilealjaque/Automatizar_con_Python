import os
import shutil


#ruta donde estaran los archivos que quieras ordenar( en la variable ruta deberas poner el path en donde quieres que se ordene los archivos)

ruta= "...."    #recordar cambiar este \ por este / (El símbolo \ (barra invertida o backslash) en Python es el carácter de escape. Se utiliza principalmente para incluir caracteres especiales en cadenas de texto (como saltos de línea \n o tabulaciones \t) o para indicar que una instrucción de código continúa en la siguiente línea.)


# crear una lista las cual servira para crear carpetas en destino si no existe
tipos=["Imágenes", "PDF", "Videos", "Documentos_word", "Documentos_txt", "Documentos_excel"] 

for carpeta in tipos:
    ruta_carpeta= os.path.join(ruta, carpeta) # 2 argumentos pide join(union de estos 2 argumentos) , la ruta donde quiero crear la carpeta y el nombre que e quiero dar a esa carpeta(recordar que el el bucle for la variable "carpeta " es donde se guardara la iteracion de cada elemento de la lista)  
    
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta) # makedirs crea directorios y este caso es lo que est aen el argumento (ruta_carpeta)
        

"""Aca empieza el segundo pasa que es meter cada archivo en su carpeta nueva"""
for archivo in os.listdir(ruta):

    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Imágenes", archivo)) #.move pide 2 argumentos que es , donde se encuentra el archivo que se quiere mover y a donde lo queremos mover (indicar 2 rutas)

    elif archivo.endswith(".pdf"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "PDF", archivo))

    elif archivo.endswith(".mp4"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Vídeos", archivo))

    elif archivo.endswith(".docx"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_Word", archivo))

    elif archivo.endswith(".txt"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_txt", archivo))
        
    elif archivo.endswith(".excel"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_excel", archivo))