import cv2
import numpy as np
import os
import argparse
from tkinter import filedialog, Tk
import sys

def select_file(title="Seleccionar archivo", filetypes=None, save_file=False):
    """
    Muestra un diálogo para seleccionar archivo.
    
    Args:
        title (str): Título de la ventana de diálogo
        filetypes (list): Lista de tipos de archivo permitidos
        save_file (bool): True para diálogo de guardar, False para abrir
    
    Returns:
        str: Ruta del archivo seleccionado o None si se cancela
    """
    root = Tk()
    root.withdraw()  # Ocultar ventana principal
    
    try:
        if save_file:
            file_path = filedialog.asksaveasfilename(
                title=title,
                filetypes=filetypes,
                defaultextension=".txt"
            )
        else:
            file_path = filedialog.askopenfilename(
                title=title,
                filetypes=filetypes
            )
        
        return file_path if file_path else None
    except Exception as e:
        print(f"Error al seleccionar archivo: {e}")
        return None
    finally:
        root.destroy()

def get_video_path(path=None):
    """
    Obtiene la ruta del video de entrada.
    
    Args:
        path (str): Ruta especificada por línea de comandos o None
    
    Returns:
        str: Ruta válida del video o None si se cancela
    """
    video_filetypes = [
        ('Videos', '*.avi *.mp4 *.mov *.mkv'),
        ('Todos los archivos', '*.*')
    ]
    
    # Si no hay path, intentar UI
    if not path:
        print("Por favor seleccione el archivo de video...")
        path = select_file("Seleccionar video", video_filetypes)
        if not path:
            return None
    
    # Si es solo nombre de archivo, buscar en directorio actual
    if os.path.dirname(path) == "":
        path = os.path.join(os.getcwd(), path)
    
    # Verificar que existe
    if not os.path.exists(path):
        print(f"Error: No se encontró el archivo: {path}")
        return None
        
    return path

def get_output_path(path=None, video_path=None):
    """
    Obtiene la ruta del archivo de salida.
    
    Args:
        path (str): Ruta especificada por línea de comandos o None
        video_path (str): Ruta del video de entrada para nombre por defecto
    
    Returns:
        str: Ruta válida para el archivo de salida o None si se cancela
    """
    # Si no hay path especificado, usar nombre del video
    if not path and video_path:
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        path = os.path.join(os.getcwd(), f"{base_name}.txt")
    
    # Si aún no hay path, pedir con UI
    if not path:
        print("Por favor seleccione dónde guardar el archivo de salida...")
        path = select_file(
            "Guardar archivo de salida",
            [('Archivo de texto', '*.txt')],
            save_file=True
        )
        if not path:
            return None
            
    # Asegurar extensión .txt
    if not path.lower().endswith('.txt'):
        path += '.txt'
        
    return path

def video_to_oled_data(video_path, output_txt_path, width=128, height=64):
    """
    Convierte un video binario en un archivo .txt con código compatible para usar en un .ino.
    """
    # Abrir el video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("No se pudo abrir el video.")
        return

    # Calcular bytes por fila
    bytes_per_row = (width + 7) // 8
    total_bytes = bytes_per_row * height

    frame_count = 0
    try:
        with open(output_txt_path, 'w') as f:
            f.write("// Datos generados desde el video\n")
            f.write(f"// Cada frame es una matriz de {width}x{height} ({bytes_per_row} bytes por fila, {height} filas)\n\n")
            f.write(f"const unsigned char video_frames[][{total_bytes}] PROGMEM = {{\n")

            print("Procesando frames...")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                resized_frame = cv2.resize(frame, (width, height))
                gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
                _, binary_frame = cv2.threshold(gray_frame, 128, 1, cv2.THRESH_BINARY)

                packed_frame = np.packbits(binary_frame, axis=1)
                packed_frame = packed_frame[:, :bytes_per_row]
                frame_bytes = packed_frame.flatten()

                f.write("    {")
                f.write(", ".join(f"0x{byte:02X}" for byte in frame_bytes))
                f.write("},\n")

                frame_count += 1
                # Mostrar progreso
                if frame_count % 10 == 0:
                    print(f"Frames procesados: {frame_count}", end='\r')

            f.write("};\n\n")
            f.write(f"// Total de frames: {frame_count}\n")
            f.write(f"const uint16_t FRAME_COUNT = {frame_count};\n")
            f.write(f"const uint8_t DISPLAY_WIDTH = {width};\n")
            f.write(f"const uint8_t DISPLAY_HEIGHT = {height};\n")

    except Exception as e:
        print(f"\nError durante el procesamiento: {e}")
        return

    finally:
        cap.release()

    print(f"\nProcesamiento completado:")
    print(f"- Frames procesados: {frame_count}")
    print(f"- Archivo de salida: {output_txt_path}")

def main():
    parser = argparse.ArgumentParser(description='Convierte un video a datos para OLED')
    parser.add_argument('input', nargs='?', help='Archivo de video (opcional)')
    parser.add_argument('-o', '--output', help='Archivo de salida (opcional)')
    parser.add_argument('-w', '--width', type=int, default=128, help='Ancho (default: 128)')
    parser.add_argument('-he', '--height', type=int, default=64, help='Alto (default: 64)')
    parser.add_argument('--no-gui', action='store_true', help='Deshabilitar interfaz gráfica')

    args = parser.parse_args()

    # Si no-gui está activado y no hay input, mostrar ayuda
    if args.no_gui and not args.input:
        parser.print_help()
        return

    # Obtener ruta del video
    video_path = args.input if args.no_gui else get_video_path(args.input)
    if not video_path:
        print("No se especificó archivo de video.")
        return

    # Obtener ruta de salida
    output_path = args.output if args.no_gui else get_output_path(args.output, video_path)
    if not output_path:
        print("No se especificó archivo de salida.")
        return

    # Ejecutar conversión
    video_to_oled_data(video_path, output_path, args.width, args.height)

if __name__ == "__main__":
    main()