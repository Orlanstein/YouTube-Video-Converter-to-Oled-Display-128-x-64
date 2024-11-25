# YouTube Video Converter to OLED Display (128x64)

## Descripción del Proyecto
Este proyecto permite convertir videos de YouTube o videos locales en un formato de texto compatible con sketches de Arduino, específicamente optimizado para pantallas OLED de 128x64 píxeles.

## Mejor rendimiento en esp32
Dadas las caracteristicas de memoria de los arduinos es mejor usar una esp32

### Ejemplo con el siguiente video:

https://www.youtube.com/watch?v=HBXNnXCm0gU

![ImagenVideoEjemplo](https://img.youtube.com/vi/HBXNnXCm0gU/0.jpg)

### Imagen de ejemplo
![Imagen 3](/Images/ExampleOfVideoInEsp32.png)


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
```bash
pip install customtkinter
```
```bash
pip install opencv-python
```
```bash
pip install yt-dlp
```

## Uso
### Conversión de video de YouTube

1. Pegar el enlace del link del video de youtube en el apartado correspondiente
2. Seleccionar la carpeta donde se guardara el archivo generado usando el boton de "examinar"

![Imagen 1](/Images/InterfazYoutube.png)



### Conversión de video local
![Imagen 2](/Images/InterfazVideoLocal.png)

## Configuración de la esp32 corriendo en Arduino IDE
1. Conectar el display oled a la esp32
   
   ![Imagen 3](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP32_OLED.png?w=873&quality=100&strip=all&ssl=1)

2. Copiar el siguiente archivo

```c
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1  // Si tu display no tiene pin RESET, usa -1
#define SCREEN_ADDRESS 0x3C  // Dirección I2C típica para SSD1306

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Datos generados desde el video
// Cada frame es una matriz de 128x64 (16 bytes por fila, 64 filas)

//PEGAR AQUI EL CONTENIDO GENERADO POR EL TXT

const uint16_t FRAME_DELAY = 33;  // ~30 FPS (33ms entre frames)
uint16_t currentFrame = 0;
unsigned long previousMillis = 0;

void setup() {
  // Inicializar el display
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.begin(9600);
    Serial.println(F("Error al inicializar SSD1306"));
    for(;;); // No continuar si hay error
  }
  
  display.clearDisplay();
  display.display();
}

void loop() {
  unsigned long currentMillis = millis();
  
  // Actualizar frame si ha pasado el tiempo necesario
  if(currentMillis - previousMillis >= FRAME_DELAY) {
    previousMillis = currentMillis;
    
    // Mostrar el frame actual
    display.clearDisplay();
    display.drawBitmap(0, 0, video_frames[currentFrame], SCREEN_WIDTH, SCREEN_HEIGHT, WHITE);
    display.display();
    
    // Avanzar al siguiente frame
    currentFrame = (currentFrame + 1) % FRAME_COUNT;
  }
}
```

3. Copiar el codigo del archivo generado en la parte donde dice el

```c
//PEGAR AQUI EL CONTENIDO GENERADO POR EL TXT
```

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o realiza un pull request.

## Licencia
[AGPL-3.0 license]
