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
```

# 📂 Organizador Automático de Archivos con Python

Este proyecto es una aplicación desarrollada en Python que permite **organizar archivos automáticamente** dentro de una carpeta seleccionada por el usuario.

El programa clasifica los archivos según su extensión, crea carpetas por categoría, genera subcarpetas por fecha de modificación y registra cada movimiento en un archivo de log. Además, monitorea la carpeta en tiempo real para detectar archivos nuevos y ordenarlos automáticamente.

Esta versión corresponde a una **evolución del script original**, incorporando mejoras orientadas a una experiencia más amigable para el usuario y pensadas para trabajar mejor como **aplicación ejecutable**.

---

## 🚀 Características principales

- Selección de carpeta mediante ventana gráfica.
- Organización automática por tipo de archivo.
- Creación de subcarpetas por año y mes de modificación.
- Registro de movimientos en `log_movimientos.txt`.
- Monitoreo en tiempo real usando `Observer` de `watchdog`.
- Interfaz gráfica simple para visualizar la carpeta vigilada.
- Botón para detener la vigilancia y cerrar la aplicación.
- Ejecución del sistema de vigilancia en un hilo independiente.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Tkinter**
- **Watchdog**
- **Threading**
- **os**
- **shutil**
- **datetime**
- **time**
- **getpass**

---

## 📌 Extensiones soportadas

| Extensión | Carpeta destino |
|----------|------------------|
| `.jpg`   | `Imágenes` |
| `.png`   | `Imágenes` |
| `.pdf`   | `PDFs` |
| `.mp4`   | `Videos` |
| `.docx`  | `Documentos_Word` |
| `.txt`   | `Documentos_txt` |

---

## ⚙️ Funcionamiento general

El flujo general del programa es el siguiente:

1. El usuario ejecuta la aplicación.
2. Se abre una ventana para seleccionar la carpeta a organizar.
3. El sistema crea las carpetas principales si no existen.
4. Se ordenan los archivos que ya estaban dentro de la carpeta.
5. Se activa un observador que vigila la carpeta en tiempo real.
6. Cuando se detecta un archivo nuevo, este se clasifica y mueve automáticamente.
7. La ventana principal muestra la carpeta vigilada y permite detener la aplicación con un botón.

---

## 🆕 Principales diferencias respecto a la versión anterior

Esta versión mantiene la lógica principal del script original, pero incorpora varios cambios importantes.

### 1. Ya no depende de `Ctrl + C` para cerrar el programa

**Antes**

La versión anterior funcionaba como un script más orientado a consola.
Después de iniciar la vigilancia, el programa quedaba corriendo y debía detenerse manualmente con:

```bash
Ctrl + C
```

**Ahora**

La nueva versión incorpora una ventana gráfica con un botón para detener la vigilancia y cerrar la aplicación de forma más cómoda.

```python
Button(ventana, text="Detener vigilancia y salir", command=detener_vigilancia).pack(pady=10)
```

**Ventaja**

Esto mejora mucho la experiencia del usuario y hace que el proyecto se sienta más como una aplicación que como un script de consola.

---

### 2. Se muestra una interfaz gráfica visible durante la ejecución

**Antes**

La ventana de Tkinter solo se usaba para seleccionar la carpeta y luego el programa seguía funcionando sin interfaz visible.

**Ahora**

Después de seleccionar la carpeta, la ventana vuelve a mostrarse con:

- el título de la aplicación,
- el texto de la carpeta vigilada,
- un botón para salir.

```python
ventana.deiconify()
ventana.title("Vigilancia de carpeta")
ventana.geometry("400x150")
```

**Ventaja**

El usuario puede ver claramente qué carpeta está siendo monitoreada y controlar la ejecución desde una interfaz simple.

---

### 3. Se agregó threading para ejecutar la vigilancia en segundo plano

Una de las diferencias más importantes de esta versión es la incorporación de la librería `threading`.

**Antes**

La vigilancia se ejecutaba directamente en el flujo principal del programa.

**Ahora**

La vigilancia se inicia dentro de un hilo separado:

```python
hilo_vigilancia = threading.Thread(target=iniciar_Vigilancia, daemon=True)
hilo_vigilancia.start()
```

**¿Por qué se hizo esto?**

Porque ahora el programa tiene una interfaz gráfica con Tkinter, y esa interfaz necesita su propio ciclo principal:

```python
ventana.mainloop()
```

Si la vigilancia y la ventana corrieran en el mismo flujo principal, la interfaz podría bloquearse o dejar de responder.

**Ventaja**

Gracias al uso de hilos:

- la ventana sigue respondiendo normalmente,
- el observador sigue vigilando la carpeta,
- ambas tareas funcionan al mismo tiempo.

---

### 4. Se agregaron funciones específicas para iniciar y detener la vigilancia

**Antes**

El observador se iniciaba directamente con:

```python
observador.start()
```

y luego el programa quedaba esperando hasta que el usuario interrumpiera la ejecución.

**Ahora**

La lógica se separó en dos funciones:

```python
def iniciar_Vigilancia():
    observador.start()

def detener_vigilancia():
    observador.stop()
    observador.join()
    ventana.quit()
```

**Ventaja**

Esto mejora la organización del código y permite controlar el observador desde la interfaz gráfica.

---

### 5. El proyecto queda mejor preparado para usarse como ejecutable

Esta nueva versión tiene una estructura más adecuada para empaquetarse como aplicación.

**¿Por qué?**

Porque ahora:

- tiene interfaz visible,
- no depende de consola para cerrarse,
- tiene un botón de salida,
- separa la vigilancia del hilo principal,
- se comporta como una mini aplicación de escritorio.

**Ventaja**

Esto la hace más apropiada para convertirla en un `.exe` con herramientas como PyInstaller.

---

## 👁️ Rol de Observer en esta versión

El `Observer` sigue siendo una de las piezas más importantes del proyecto.

**¿Qué hace?**

Es el componente que vigila la carpeta seleccionada en tiempo real.

**¿Qué detecta?**

Detecta la creación de nuevos archivos dentro de la carpeta observada.

**¿Qué pasa cuando detecta un archivo nuevo?**

El manejador de eventos ejecuta:

```python
def on_created(self, event):
    if not event.is_directory:
        print(f"Nuevo archivo detectado: {event.src_path}")
        ordenar_archivos(ruta)
```

**Flujo de trabajo**

1. `Observer` vigila la carpeta.
2. Cuando entra un archivo nuevo, se dispara un evento.
3. `FileSystemEventHandler` recibe ese evento.
4. Se ejecuta `on_created()`.
5. Se vuelve a llamar a `ordenar_archivos(ruta)`.
6. El archivo se mueve automáticamente a su ubicación correcta.

**Diferencia importante en esta versión**

Ahora `Observer` no solo trabaja junto a la lógica del programa, sino también junto a una interfaz gráfica y un hilo secundario. Eso hace que esta versión tenga una arquitectura más completa.

---

## 🧵 Importancia de threading en esta nueva versión

La incorporación de `threading` es uno de los cambios más relevantes del proyecto.

**Función del hilo secundario**

```python
hilo_vigilancia = threading.Thread(target=iniciar_Vigilancia, daemon=True)
```

Este hilo permite que la vigilancia se ejecute en segundo plano mientras la ventana principal sigue activa.

**¿Qué resuelve?**

Evita que el monitoreo del sistema de archivos bloquee la interfaz de usuario.

**Resultado**

El programa puede:

- vigilar archivos en tiempo real,
- mantener una ventana activa,
- responder al botón de cierre,
- funcionar de manera más estable como aplicación.

---

## 📂 Estructura de organización generada

```
📁 Carpeta_Seleccionada
 ├── 📁 Imágenes
 │    └── 📁 2024-04
 │         └── foto1.jpg
 ├── 📁 PDFs
 │    └── 📁 2024-03
 │         └── documento.pdf
 ├── 📁 Videos
 │    └── 📁 2024-02
 │         └── video.mp4
 ├── 📁 Documentos_Word
 │    └── 📁 2024-01
 │         └── informe.docx
 ├── 📁 Documentos_txt
 │    └── 📁 2024-04
 │         └── notas.txt
 └── 📄 log_movimientos.txt
```

---

## 📥 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Instalar dependencias

```bash
pip install watchdog
```

> `tkinter` normalmente viene incluido con Python en la mayoría de instalaciones.

---

## ▶️ Ejecución

```bash
python nombre_del_archivo.py
```

Al ejecutar el programa:

1. Seleccionas una carpeta.
2. Se organizan los archivos existentes.
3. Se abre una ventana mostrando la carpeta vigilada.
4. El sistema queda observando nuevos archivos en tiempo real.
5. Puedes cerrar todo con el botón **"Detener vigilancia y salir"**.

---

## 🧠 Conceptos de Python aplicados

Este proyecto permite practicar:

- manejo de archivos y carpetas,
- rutas con `os.path`,
- diccionarios,
- funciones,
- manejo de excepciones,
- clases y herencia,
- programación orientada a eventos,
- interfaces gráficas con Tkinter,
- hilos con `threading`,
- monitoreo del sistema de archivos con `Observer`.

---

## 📈 Evolución del proyecto

### Versión anterior
- más orientada a consola,
- cierre manual con teclado,
- sin interfaz visible permanente.

### Versión actual
- más orientada a aplicación,
- interfaz simple y funcional,
- botón de salida,
- uso de hilos,
- mejor base para generar ejecutables.

Esto demuestra un avance desde un script automatizado hacia una solución más cercana a una aplicación de escritorio.

---

## 📚 Posibles mejoras futuras

- Agregar soporte para más extensiones.
- Evitar sobrescribir archivos con nombres repetidos.
- Mostrar notificaciones cuando se detecten archivos nuevos.
- Permitir configurar extensiones y carpetas desde la interfaz.
- Empaquetar oficialmente el proyecto como `.exe`.
- Agregar icono y nombre de aplicación más formal.
```

🖼️ Renombrador Secuencial de Imágenes con Python
Este proyecto es un script sencillo en Python que permite renombrar imágenes automáticamente dentro de una carpeta específica.
El programa busca archivos con extensiones `.jpg` y `.png`, los recopila en una lista y luego los renombra de forma secuencial usando un prefijo definido por el usuario.
Por ejemplo, archivos como:
`foto\_perro.jpg`
`vacaciones.png`
`playa.jpg`
pueden pasar a llamarse:
`imagen\_001.jpg`
`imagen\_002.png`
`imagen\_003.jpg`
---
🚀 Características
Renombra imágenes automáticamente.
Soporta archivos `.jpg` y `.png`.
Usa un prefijo personalizable.
Mantiene la extensión original de cada archivo.
Aplica numeración secuencial con formato de 3 dígitos.
Funciona sobre una carpeta específica definida en el código.
---
🛠️ Tecnologías utilizadas
Python 3
os
---
📌 Extensiones soportadas
Extensión	Soportada
`.jpg`	Sí
`.png`	Sí
---
⚙️ ¿Cómo funciona?
El flujo del programa es el siguiente:
Se define la carpeta que contiene las imágenes.
Se define el prefijo que tendrán los nuevos nombres.
Se indican las extensiones válidas.
El programa recorre todos los archivos de la carpeta.
Filtra únicamente los que terminan en `.jpg` o `.png`.
Recorre esa lista de archivos válidos.
Genera un nuevo nombre secuencial para cada archivo.
Renombra cada imagen dentro de la misma carpeta.
---
🧠 Lógica del script
El script está dividido en dos partes principales:
1. Filtrado de archivos válidos
Primero, el programa revisa todos los elementos de la carpeta y selecciona solo aquellos que terminan en las extensiones permitidas.
```python
archivos = \[]

for f in os.listdir(carpeta):
    if f.endswith(extensiones):
        archivos.append(f)
```
Aquí:
`os.listdir(carpeta)` devuelve todo el contenido de la carpeta.
`f.endswith(extensiones)` revisa si el nombre termina en `.jpg` o `.png`.
`archivos.append(f)` guarda solo los archivos válidos.
2. Renombrado secuencial
Después, el programa recorre la lista filtrada y asigna nuevos nombres con numeración correlativa.
```python
for i, nombre\_actual in enumerate(archivos, start=1):
    extension\_actual = os.path.splitext(nombre\_actual)\[1]
    nuevo\_nombre = f"{prefijo}{i:03}{extension\_actual}"
    ruta\_actual = os.path.join(carpeta, nombre\_actual)
    ruta\_nueva = os.path.join(carpeta, nuevo\_nombre)
    os.rename(ruta\_actual, ruta\_nueva)
```
Aquí:
`enumerate(..., start=1)` genera una numeración desde 1.
`os.path.splitext(nombre\_actual)\[1]` obtiene la extensión original.
`f"{prefijo}{i:03}{extension\_actual}"` construye el nuevo nombre.
`os.rename()` realiza el cambio de nombre.
---
📄 Código del proyecto
```python
import os

carpeta = "C:/Users/"
prefijo = "imagen\_"
extensiones = (".jpg", ".png")

archivos = \[]

for f in os.listdir(carpeta):
    if f.endswith(extensiones):
        archivos.append(f)

for i, nombre\_actual in enumerate(archivos, start=1):
    extension\_actual = os.path.splitext(nombre\_actual)\[1]
    nuevo\_nombre = f"{prefijo}{i:03}{extension\_actual}"
    ruta\_actual = os.path.join(carpeta, nombre\_actual)
    ruta\_nueva = os.path.join(carpeta, nuevo\_nombre)
    os.rename(ruta\_actual, ruta\_nueva)
```
---
📂 Ejemplo práctico
Archivos originales
```
foto\_perro.jpg
vacaciones.png
playa.jpg
documento.pdf
```
Resultado después de ejecutar el script
```
imagen\_001.jpg
imagen\_002.png
imagen\_003.jpg
documento.pdf
```
> `documento.pdf` no cambia porque no forma parte de las extensiones definidas.
---
📥 Requisitos
Solo necesitas tener instalado:
Python 3
No requiere librerías externas.
---
▶️ Ejecución
Guarda el script en un archivo, por ejemplo:
```
renombrar\_imagenes.py
```
Luego ejecútalo con:
```bash
python renombrar\_imagenes.py
```
---
✏️ Personalización
Puedes modificar estos valores según tus necesidades:
Cambiar la carpeta de trabajo
```python
carpeta = "C:/Users/juanm/Desktop/auto\_python"
```
Cambiar el prefijo
```python
prefijo = "imagen\_"
```
Cambiar extensiones permitidas
```python
extensiones = (".jpg", ".png")
```
Por ejemplo, si quisieras usar otro prefijo:
```python
prefijo = "foto\_"
```
El resultado sería:
```
foto\_001.jpg
foto\_002.png
```
---
📚 Conceptos de Python aplicados
Este proyecto permite practicar:
variables,
listas,
bucles `for`,
condicionales,
uso del módulo `os`,
rutas de archivos,
separación de extensiones,
renombrado de archivos,
formateo de cadenas con f-strings,
`enumerate()`.
---
⚠️ Consideraciones importantes
1. El orden depende de `os.listdir()`
El programa renombra los archivos en el orden en que el sistema operativo los devuelve. Eso significa que el orden no siempre será necesariamente alfabético o visual.
2. Puede haber conflictos de nombres
Si ya existen archivos con nombres como `imagen\_001.jpg` o `imagen\_002.png`, pueden ocurrir conflictos al intentar renombrar.
3. El script renombra directamente
Este programa cambia los nombres reales de los archivos dentro de la carpeta. Por eso, se recomienda probarlo primero con una carpeta de prueba.
---
📈 Posibles mejoras futuras
Ordenar los archivos alfabéticamente antes de renombrarlos.
Agregar compatibilidad con más extensiones.
Evitar conflictos con nombres ya existentes.
Permitir elegir la carpeta con una ventana gráfica.
Agregar una vista previa antes de renombrar.
Convertirlo en una pequeña aplicación de escritorio.