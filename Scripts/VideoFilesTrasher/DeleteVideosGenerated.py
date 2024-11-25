import sys
import os

# Añadimos el directorio raíz al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ruta_video_descargado = os.getcwd() + "/Video/VideoDownloaded/DownloadedVideo.mp4"
ruta_videoReescalado_BW = os.getcwd() + "/Video/VideoReescaled/video_bw_128x64.avi"

def eliminar_archivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)  # Elimina el archivo
        print(f"Archivo {ruta} eliminado correctamente.")
    else:
        print(f"El archivo {ruta} no existe.")

def eliminar_Video():
    if os.path.exists(ruta_video_descargado):
        os.remove(ruta_video_descargado)  # Elimina el archivo
        print(f"Archivo {ruta_video_descargado} eliminado correctamente.")
    else:
        print(f"El archivo {ruta_video_descargado} no existe.")
        
def eliminar_VideoReescalado_BW():
    if os.path.exists(ruta_videoReescalado_BW):
        os.remove(ruta_videoReescalado_BW)  # Elimina el archivo
        print(f"Archivo {ruta_videoReescalado_BW} eliminado correctamente.")
    else:
        print(f"El archivo {ruta_videoReescalado_BW} no existe.")
    
# Eliminar los archivos después del procesamiento
eliminar_archivo(ruta_video_descargado)
eliminar_archivo(ruta_videoReescalado_BW)