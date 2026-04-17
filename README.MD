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

# 📂 Organizador de Archivos  (V2 ordenar_archivos)

Esta es una versión avanzada del script de automatización para organizar directorios. A diferencia de las versiones básicas, esta herramienta incluye una **interfaz gráfica** para seleccionar carpetas, organización automática por **fecha de modificación** y un **registro histórico** de movimientos.

## ✨ Nuevas Funcionalidades

-   **Selector de Carpetas (GUI):** No más rutas escritas a mano. Abre un cuadro de diálogo profesional para elegir tu carpeta.
-   **Organización Cronológica:** Los archivos se clasifican primero por tipo (PDF, Imágenes, etc.) y luego en subcarpetas por mes (ej. `2024-05`).
-   **Sistema de Auditoría (Logs):** Genera un archivo `.txt` que registra qué usuario movió qué archivo y en qué momento.
-   **Seguridad de Usuario:** Detecta automáticamente qué usuario del sistema está ejecutando la acción.

## 🛠️ Requisitos

-   **Python 3.x**
-   **Librerías estándar:** `os`, `shutil`, `getpass`, `tkinter`, `datetime`.
    -   *Nota: Todas vienen preinstaladas con Python, no necesitas usar `pip install`.*

## ⚙️ Cómo utilizarlo

1.  **Ejecuta el script:**
    ```bash
    python organizador_avanzado.py
    ```
2.  **Selecciona la ruta:** Se abrirá una ventana emergente. Busca y selecciona la carpeta que deseas limpiar.
3.  **Procesamiento:** El script creará las carpetas necesarias y moverá los archivos automáticamente.
4.  **Revisa el Log:** En la carpeta seleccionada aparecerá un archivo llamado `log_movimientos.txt` con el historial del proceso.

## 📊 Estructura de Salida

El script transformará un desorden de archivos en una estructura como esta:

```text
📁 Carpeta_Seleccionada
 ├── 📁 Imágenes
 │    └── 📁 2024-04
 │         └── foto1.jpg
 ├── 📁 PDFs
 │    └── 📁 2024-03
 │         └── documento.pdf
 └── 📄 log_movimientos.txt