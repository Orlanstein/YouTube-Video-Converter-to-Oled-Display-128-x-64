import sys
import os

# Añadimos el directorio raíz al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VideoProcessing.VIdeoDownloader import descargar_video
from VideoProcessing.VideoToBinaryVideo import convert_video_to_binary_bw
from VideoProcessing.BinVidToCodeTxt import video_to_oled_data

# Descarga el video
descargar_video("https://www.youtube.com/watch?v=rwKhWgYKXME")

# Rutas de entrada y salida
ruta_video_descargado = os.getcwd() + "/Video/VideoDownloaded/DownloadedVideo.mp4"
# Añadimos el nombre del archivo de salida a la ruta
ruta_videoReescalado_BW = os.getcwd() + "/Video/VideoReescaled/video_bw_128x64.avi"  # <- Añadido nombre del archivo
# Ruta salida del txt
ruta_txt_salida = os.getcwd() + "/Output/arrayVideoOLED.txt"

# Reescala y convierte a blanco y negro
convert_video_to_binary_bw(ruta_video_descargado, ruta_videoReescalado_BW)

#Covierte video en BW y reescalado a un txt
video_to_oled_data(ruta_videoReescalado_BW, ruta_txt_salida)