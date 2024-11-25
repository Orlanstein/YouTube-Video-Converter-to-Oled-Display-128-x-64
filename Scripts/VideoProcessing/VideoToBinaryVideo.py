import os
import cv2
from pathlib import Path

def get_file_path(file_name, base_dir=None):
    """
    Determina la ruta completa del archivo basado en el nombre o ruta proporcionada.
    
    Args:
        file_name (str): Nombre del archivo o ruta completa
        base_dir (str, optional): Directorio base para búsqueda de archivos
    
    Returns:
        Path: Objeto Path con la ruta completa del archivo
    """
    if base_dir is None:
        base_dir = os.getcwd()
    
    path = Path(file_name)
    
    # Si solo se proporcionó un nombre de archivo, buscar en el directorio base
    if not path.is_absolute():
        path = Path(base_dir) / path
        
    return path

def convert_video_to_binary_bw(input_path, output_path=None, width=128, height=64, threshold_value=128):
    """
    Convierte un video a blanco y negro binario con dimensiones específicas.
    
    Args:
        input_path (str): Ruta o nombre del archivo de entrada
        output_path (str, optional): Ruta o nombre del archivo de salida
        width (int): Ancho del video de salida
        height (int): Alto del video de salida
        threshold_value (int): Valor umbral para la conversión a binario
    """
    # Procesar la ruta de entrada
    input_file = get_file_path(input_path)
    
    # Si no existe el archivo de entrada
    if not input_file.exists():
        print(f"El archivo de entrada no existe: {input_file}")
        return
    
    # Si no se especifica ruta de salida, crear una en la misma carpeta
    if output_path is None:
        output_path = input_file.with_name(f"{input_file.stem}_128x64_BW.avi")
    else:
        output_path = get_file_path(output_path)
    
    # Crear el directorio de salida si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Abrir el video
    cap = cv2.VideoCapture(str(input_file))
    if not cap.isOpened():
        print("No se pudo abrir el video.")
        return

    # Obtener FPS o usar valor predeterminado
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print("FPS no detectado, usando valor predeterminado: 30 FPS.")
        fps = 30

    # Configurar el VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height), isColor=False)

    if not out.isOpened():
        print("No se pudo abrir el archivo de salida. Verifica la ruta o el codec.")
        return

    print("Procesando video...")
    frames_procesados = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Escalar el fotograma
        resized_frame = cv2.resize(frame, (width, height))
        
        # Convertir a escala de grises
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        
        # Convertir a binario (blanco y negro)
        _, binary_frame = cv2.threshold(gray_frame, threshold_value, 255, cv2.THRESH_BINARY)
        
        # Escribir el fotograma procesado
        out.write(binary_frame)
        frames_procesados += 1

    # Liberar recursos
    cap.release()
    out.release()
    print(f"Video convertido exitosamente:")
    print(f"- Frames procesados: {frames_procesados}")
    print(f"- Archivo guardado en: {output_path}")

if __name__ == "__main__":
    # Ejemplo de uso interactivo
    input_video = input("Ingresa la ruta o nombre del archivo de video de entrada: ")
    output_video = input("Ingresa la ruta o nombre del archivo de salida (Enter para usar nombre por defecto): ").strip()
    
    # Si no se especifica salida, usar None para generar nombre automático
    if not output_video:
        output_video = None
        
    convert_video_to_binary_bw(input_video, output_video)