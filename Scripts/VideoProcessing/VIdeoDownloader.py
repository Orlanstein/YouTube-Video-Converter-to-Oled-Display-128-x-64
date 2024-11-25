import yt_dlp
import os
from pathlib import Path

def descargar_video(link, ruta_guardado=None):
    """
    Descarga un video de YouTube en formato MP4.
    
    Args:
        link (str): URL del video de YouTube
        ruta_guardado (str, optional): Ruta donde guardar el video. Si no se especifica,
                                     se usa la carpeta actual.
    """
    try:
        # Si no se proporciona una ruta, usar la carpeta actual
        if ruta_guardado is None:
            ruta_guardado = os.getcwd() + "/Video/VideoDownloaded"
        
        # Convertir la ruta a objeto Path y asegurar que existe
        ruta = Path(ruta_guardado)
        if not ruta.exists():
            print(f"La ruta {ruta_guardado} no existe. Usando la carpeta actual.")
            ruta = Path(os.getcwd())
        
        # Configurar las opciones de descarga
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': str(ruta / 'DownloadedVideo.%(ext)s'),
        }
        
        # Realizar la descarga
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("¡Video descargado exitosamente!")
        print(f"Guardado en: {ruta}")
        
    except Exception as e:
        print(f"Error durante la descarga: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar el link del video
    link = input("Ingresa el URL del video de YouTube: ")
    
    # Preguntar si desea especificar una ruta
    respuesta = input("¿Deseas especificar una ruta de guardado? (s/n): ").lower()
    
    if respuesta == 's':
        ruta = input("Ingresa la ruta completa donde deseas guardar el video: ")
        descargar_video(link, ruta)
    else:
        descargar_video(link)