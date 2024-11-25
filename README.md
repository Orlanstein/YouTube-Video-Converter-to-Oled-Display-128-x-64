# YouTube Video Converter to OLED Display (128x64)

## Descripción del Proyecto
Este proyecto permite convertir videos de YouTube o videos locales en un formato de texto compatible con sketches de Arduino, específicamente optimizado para pantallas OLED de 128x64 píxeles.

## Características
- Conversión de videos de YouTube
- Conversión de videos locales
- Generación de archivos de texto para Arduino
- Compatibilidad con pantallas OLED 128x64

## Requisitos Previos
- Python 3.x
- Bibliotecas de Python:
  - pytube (para descargar videos de YouTube)
  - opencv-python (para procesamiento de video)
  - numpy (para manipulación de datos)

## Instalación
1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/YouTube-Video-Converter-to-Oled-Display-128-x-64.git
```

2. Instalar dependencias
```bash
pip install pytube opencv-python numpy
```

## Uso
### Conversión de video de YouTube
```python
python converter.py --youtube <URL_DEL_VIDEO>
```

### Conversión de video local
```python
python converter.py --local <RUTA_DEL_VIDEO>
```

## Configuración de Arduino
1. Copiar el archivo de texto generado a tu sketch
2. Cargar el archivo en la pantalla OLED utilizando las bibliotecas adecuadas

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o realiza un pull request.

## Licencia
[Especificar la licencia, por ejemplo: MIT License]