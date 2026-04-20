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
 
```
 
# 📂 Organizador Automático de Archivos con Python (V3 ordenar_archivos)

Este proyecto es un **organizador automático de archivos** desarrollado en Python.  
Su función principal es **clasificar archivos según su extensión** y moverlos a carpetas específicas, creando además subcarpetas por **año y mes de última modificación**.

Además, el programa queda **vigilando en tiempo real** la carpeta seleccionada. Esto significa que no solo organiza los archivos que ya existen al inicio, sino que también detecta nuevos archivos apenas son agregados y los ordena automáticamente.

---

## 🚀 Características

- Selección de carpeta mediante ventana gráfica.
- Clasificación automática por tipo de archivo.
- Creación de carpetas por categoría:
  - Imágenes
  - PDFs
  - Videos
  - Documentos Word
  - Archivos TXT
- Creación de subcarpetas por fecha (`YYYY-MM`).
- Registro de movimientos en un archivo `log_movimientos.txt`.
- Monitoreo en tiempo real de nuevos archivos usando `watchdog`.
- Validación para evitar mover archivos que estén en uso.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Tkinter** → para seleccionar la carpeta
- **Watchdog** → para monitorear cambios en tiempo real
- **Observer** → componente que vigila continuamente la carpeta
- **FileSystemEventHandler** → clase que permite reaccionar a eventos del sistema de archivos
- **os / shutil / datetime / time / getpass** → para gestión de archivos, rutas, fechas y usuario del sistema

---

## 📌 Extensiones soportadas

El programa actualmente organiza los siguientes tipos de archivos:

| Extensión | Carpeta destino |
|----------|------------------|
| `.jpg`   | `Imágenes` |
| `.png`   | `Imágenes` |
| `.pdf`   | `PDFs` |
| `.mp4`   | `Videos` |
| `.docx`  | `Documentos_Word` |
| `.txt`   | `Documentos_txt` |

---

## ⚙️ ¿Cómo funciona?

El flujo general del programa es el siguiente:

1. El usuario ejecuta el script.
2. Se abre una ventana para seleccionar la carpeta a organizar.
3. El programa revisa todos los archivos existentes en esa carpeta.
4. Cada archivo se clasifica según su extensión.
5. Se crea una carpeta principal según el tipo de archivo.
6. Dentro de esa carpeta, se crea una subcarpeta con formato `año-mes` según la fecha de modificación.
7. El archivo es movido a su nueva ubicación.
8. El movimiento queda registrado en `log_movimientos.txt`.
9. Luego, el programa activa un observador en tiempo real.
10. Si se agrega un archivo nuevo, este se detecta automáticamente y se ordena sin intervención del usuario.

---

## 👁️ Enfoque especial: `Observer` y monitoreo en tiempo real

Una de las partes más importantes de este proyecto es el uso de **`Observer`**, perteneciente a la librería `watchdog`.

### ¿Qué es `Observer`?

`Observer` es el componente encargado de **vigilar una carpeta constantemente** mientras el programa está en ejecución.  
Su función no es mover archivos ni clasificarlos directamente, sino **estar atento a cambios** dentro del sistema de archivos.

En este proyecto, el `Observer` detecta cuándo se crea un nuevo archivo dentro de la carpeta seleccionada.

---

### ¿Por qué es importante?

Sin `Observer`, el script solo podría:

- ejecutarse una vez,
- ordenar los archivos existentes,
- terminar.

Con `Observer`, el programa pasa a comportarse como un sistema **dinámico y automatizado**, porque:

- permanece activo,
- sigue escuchando cambios,
- reacciona cuando aparece un archivo nuevo,
- vuelve a ejecutar la lógica de organización.

En otras palabras, `Observer` convierte este proyecto de un simple script de ordenamiento a una herramienta de **automatización en tiempo real**.

---

### ¿Cómo trabaja junto a `FileSystemEventHandler`?

El funcionamiento se basa en dos piezas:

#### 1. `Observer`
Es el vigilante.  
Se queda observando la carpeta.

#### 2. `FileSystemEventHandler`
Es el manejador de eventos.  
Define qué hacer cuando ocurre algo en la carpeta.

En este caso, se usa el método:

```python
def on_created(self, event):