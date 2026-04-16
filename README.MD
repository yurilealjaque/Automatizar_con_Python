# 📂 Organizador Automático de Archivos(ordenar_archivos_carpeta)

Este es un script sencillo y potente desarrollado en **Python** para automatizar la limpieza de carpetas. Su función principal es escanear un directorio específico y clasificar los archivos sueltos en carpetas organizadas según su tipo (Imágenes, documentos, videos, etc.).

## 🚀 Características

- **Clasificación por extensión:** Mueve archivos automáticamente a carpetas predefinidas.
- **Gestión de directorios:** Si la carpeta de destino no existe (ej. "PDF"), el script la crea automáticamente antes de mover los archivos.
- **Fácil configuración:** Solo requiere definir la ruta de la carpeta que deseas ordenar.

## 🛠️ Requisitos

- **Python 3.x** instalando en tu sistema.
- No requiere librerías externas (utiliza `os` y `shutil`, que vienen integradas en Python).

## ⚙️ Cómo usarlo

1. **Clona o descarga** este archivo en tu computadora.
2. **Configura la ruta:** Abre el script y localiza la variable `ruta`.
3. **Ingresa tu path:** Sustituye los puntos suspensivos por la dirección de la carpeta a organizar.
   > **Importante:** Recuerda cambiar las barras invertidas `\` por barras normales `/` para evitar errores de caracteres de escape en Python.
   
   ```python
   ruta = "C:/Usuarios/Nombre/Descargas"