import keyboard
import subprocess

# Definir la combinación de teclas (hotkey) para activar el script
HOTKEY_DC = "shift+d"
HOTKEY_OP = "shift+o"

# Ruta al archivo binario .exe que deseas ejecutar
EXE_PATH_DC = "C:\\Users\\<USER>\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
EXE_PATH_OP = "C:\\Users\\<USER>\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"

def executeDiscord():
    try:
        # Ejecutar el archivo binario .exe
        subprocess.run(EXE_PATH_DC, shell=True)
    except Exception as e:
        pass
        #print("Error al ejecutar el archivo .exe:", e)

def executeOpera():
    try:
        # Ejecutar el archivo binario .exe
        subprocess.run(EXE_PATH_OP, shell=True)
    except Exception as e:
        pass
        #print("Error al ejecutar el archivo .exe:", e)

# Agregar un listener para el atajo de teclado
keyboard.add_hotkey(HOTKEY_DC, executeDiscord)
keyboard.add_hotkey(HOTKEY_OP, executeOpera)

# Mantener el script en ejecución
keyboard.wait("esc")  # Esperar hasta que se presione la tecla "Esc" para salir del script