"""
Componente del feed de cámara.
Versión inicial: placeholder con texto central.
Más adelante se reemplazará con video OpenCV.
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from ..styles import COLORS, get_title_font


class CameraView(QLabel):
    """Widget que muestra el feed de la cámara (placeholder por ahora)."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Configurar texto
        self.setText("CAMERA FEED")
        self.setAlignment(Qt.AlignCenter)
        
        # Configurar fuente
        font = get_title_font()
        font.setPointSize(48)
        self.setFont(font)
        
        # Configurar colores y estilo
        self.setStyleSheet(f"""
            QLabel {{
                background-color: black;
                color: {COLORS['text'].name()};
                border: 3px solid {COLORS['accent_purple'].name()};
                border-radius: 12px;
            }}
        """)
        
        # Estado de la cámara (para compatibilidad con código existente)
        self.camera_active = False
        self.frame_count = 0
    
    def start_camera(self):
        """Inicia la cámara (simulado)."""
        self.camera_active = True
        self.frame_count = 0
        # El texto se mantiene igual por ahora
        self.update()
    
    def stop_camera(self):
        """Detiene la cámara."""
        self.camera_active = False
        self.update()

# TODO (Cursor): más adelante, reemplazar esto por frames de OpenCV
# TODO (Cursor): animar entrada o aplicar overlay de shader morado
