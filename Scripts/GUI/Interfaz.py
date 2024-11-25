import customtkinter as ctk
from pathlib import Path
from tkinter import filedialog

class VideoConverter(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("Orlanstein OLED Display Video Converter")
        self.geometry("800x500")
        
        # Configurar el tema oscuro y colores
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.dark_gray = "#1a1a1a"
        self.darker_gray = "#151515"
        self.blue_accent = "#3b8ed0"
        
        #My personalized colo palettes
        self.jet_gray = "#2E2B2B"
        self.jetDarker_gray = "#2B2A2A"
        self.timberwolf_green = "#CDD0CE"
        self.blueCadet_gray = "#84A3B5"
        self.berkeley_blue = "#1E385E"
        self.honolulu_blue = "#1C7AC0"
        
        self.configure(fg_color=self.darker_gray)
        
        # Crear el layout principal
        self.setup_main_layout()
        
    def setup_main_layout(self):
        # Título principal
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=(20,10), fill="x")
        
        #Tittle into the window 
        title_label = ctk.CTkLabel(
            title_frame,
            text="Orlanstein OLED Display Video Converter",
            font=("Inter", 24, "bold"),
            text_color="#ffffff"
        )
        title_label.pack()
        
        # Subtítulo
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="Convertidor de videos para pantalla OLED 128x64",
            font=("Inter", 12),
            text_color="#888888"
        )
        
        subtitle_label.pack(pady=(5,0))
        
        # Frame principal
        main_frame = ctk.CTkFrame(self, fg_color=self.darker_gray)
        main_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Frame izquierdo para los botones de selección
        self.left_frame = ctk.CTkFrame(main_frame, fg_color=self.dark_gray, width=150)
        self.left_frame.pack(side="left", fill="y", padx=(0,2))
        self.left_frame.pack_propagate(False)
        
        # Botones de selección
        self.setup_selector_buttons()
        
        # Frame derecho para el contenido
        self.right_frame = ctk.CTkFrame(main_frame, fg_color=self.dark_gray)
        self.right_frame.pack(side="left", fill="both", expand=True)
        
        # Configurar contenido inicial (YouTube)
        self.setup_youtube_content()
        
    def setup_selector_buttons(self):
        # Estilo común para los botones
        button_styleYT = {
            "border_color": "self.blue_accent",
            "fg_color": self.blue_accent,
            "hover_color": self.blue_accent,
            "corner_radius": 6,
            "height": 40,
            "anchor": "center",
            "font": ("Inter", 13)
        }
        button_style = {
            "border_color": "self.blue_accent",
            "fg_color": "transparent",
            "hover_color": self.blue_accent,
            "corner_radius": 6,
            "height": 40,
            "anchor": "center",
            "font": ("Inter", 13)
        }
        
        # Frame para los botones
        button_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        button_frame.pack(pady=20, fill="x")
        
        # Botón YouTube
        self.youtube_btn = ctk.CTkButton(
            button_frame,
            text="YouTube",
            command=lambda: self.show_content("youtube"),
            **button_styleYT
        )
        self.youtube_btn.pack(fill="x", padx=10, pady=(0,5))
        
        # Botón PC Local
        self.local_btn = ctk.CTkButton(
            button_frame,
            text="PC Local",
            command=lambda: self.show_content("local"),
            **button_style
        )
        self.local_btn.pack(fill="x", padx=10)
        
    def setup_youtube_content(self):
        # Limpiar frame derecho
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        # Frame principal de contenido
        content_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        content_frame.pack(padx=40, pady=30, fill="both", expand=True)
        
        # URL del Video
        url_label = ctk.CTkLabel(
            content_frame,
            text="URL del Video",
            font=("Inter", 14, "bold"),
            text_color="#ffffff"
        )
        url_label.pack(anchor="w", pady=(0,5))
        
        self.url_entry = ctk.CTkEntry(
            content_frame,
            placeholder_text="Ingresa la URL del video de YouTube",
            height=40,
            width=400,
            fg_color=self.darker_gray,
            border_color=self.blue_accent,
            font=("Inter", 12)
        )
        self.url_entry.pack(fill="x", pady=(0,15))
        
        # Frame para selección de carpeta
        output_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        output_frame.pack(fill="x", pady=(0,20))
        
        output_label = ctk.CTkLabel(
            output_frame,
            text="Carpeta de salida",
            font=("Inter", 14, "bold"),
            text_color="#ffffff"
        )
        output_label.pack(anchor="w", pady=(0,5))
        
        self.output_entry = ctk.CTkEntry(
            output_frame,
            placeholder_text="Selecciona la carpeta de destino",
            height=40,
            fg_color=self.darker_gray,
            border_color=self.blue_accent,
            font=("Inter", 12),
            state="readonly"
        )
        self.output_entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        
        self.browse_output_btn = ctk.CTkButton(
            output_frame,
            text="Examinar",
            width=100,
            height=40,
            command=self.browse_output_folder
        )
        self.browse_output_btn.pack(side="right")
        
        # Botón de conversión
        self.convert_button = ctk.CTkButton(
            content_frame,
            text="Convertir Video",
            height=45,
            fg_color=self.blue_accent,
            font=("Inter", 13, "bold"),
            command=self.process_youtube
        )
        self.convert_button.pack(fill="x", pady=(20,0))
        
    def setup_local_content(self):
        # Limpiar frame derecho
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        # Frame principal de contenido
        content_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        content_frame.pack(padx=40, pady=30, fill="both", expand=True)
        
        # Frame para selección de archivo
        file_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        file_frame.pack(fill="x", pady=(0,20))
        
        file_label = ctk.CTkLabel(
            file_frame,
            text="Archivo de Video",
            font=("Inter", 14, "bold"),
            text_color="#ffffff"
        )
        file_label.pack(anchor="w", pady=(0,5))
        
        self.file_entry = ctk.CTkEntry(
            file_frame,
            placeholder_text="Selecciona el archivo de video",
            height=40,
            fg_color=self.darker_gray,
            border_color=self.blue_accent,
            font=("Inter", 12),
            state="readonly"
        )
        self.file_entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        
        self.browse_file_btn = ctk.CTkButton(
            file_frame,
            text="Examinar",
            width=100,
            height=40,
            command=self.browse_file
        )
        self.browse_file_btn.pack(side="right")
        
        # Frame para selección de carpeta de salida
        output_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        output_frame.pack(fill="x", pady=(0,20))
        
        output_label = ctk.CTkLabel(
            output_frame,
            text="Carpeta de salida",
            font=("Inter", 14, "bold"),
            text_color="#ffffff"
        )
        output_label.pack(anchor="w", pady=(0,5))
        
        self.local_output_entry = ctk.CTkEntry(
            output_frame,
            placeholder_text="Selecciona la carpeta de destino",
            height=40,
            fg_color=self.darker_gray,
            border_color=self.blue_accent,
            font=("Inter", 12),
            state="readonly"
        )
        self.local_output_entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        
        self.browse_local_output_btn = ctk.CTkButton(
            output_frame,
            text="Examinar",
            width=100,
            height=40,
            command=lambda: self.browse_output_folder("local")
        )
        self.browse_local_output_btn.pack(side="right")
        
        # Botón de conversión
        self.convert_local_button = ctk.CTkButton(
            content_frame,
            text="Convertir Video",
            height=45,
            fg_color=self.blue_accent,
            font=("Inter", 13, "bold"),
            command=self.process_local
        )
        self.convert_local_button.pack(fill="x", pady=(20,0))
    
    def show_content(self, content_type):
        if content_type == "youtube":
            self.setup_youtube_content()
            self.youtube_btn.configure(fg_color=self.blue_accent)
            self.local_btn.configure(fg_color= "transparent")
        else:
            self.setup_local_content()
            self.youtube_btn.configure(fg_color="transparent")
            self.local_btn.configure(fg_color=self.blue_accent)
            
    def browse_file(self):
        filetypes = (
            ('Videos', '*.mp4 *.avi *.mkv *.mov'),
            ('Todos los archivos', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Seleccionar video',
            filetypes=filetypes
        )
        
        if filename:
            self.file_entry.configure(state="normal")
            self.file_entry.delete(0, 'end')
            self.file_entry.insert(0, filename)
            self.file_entry.configure(state="readonly")
            
    def browse_output_folder(self, source="youtube"):
        folder = filedialog.askdirectory(
            title='Seleccionar carpeta de destino'
        )
        
        if folder:
            if source == "youtube":
                self.output_entry.configure(state="normal")
                self.output_entry.delete(0, 'end')
                self.output_entry.insert(0, folder)
                self.output_entry.configure(state="readonly")
            else:
                self.local_output_entry.configure(state="normal")
                self.local_output_entry.delete(0, 'end')
                self.local_output_entry.insert(0, folder)
                self.local_output_entry.configure(state="readonly")
    
    def process_youtube(self):
        # Aquí iría la lógica para procesar el video de YouTube
        pass
        
    def process_local(self):
        # Aquí iría la lógica para procesar el video local
        pass

if __name__ == "__main__":
    app = VideoConverter()
    app.mainloop()