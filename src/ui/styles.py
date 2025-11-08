"""
Paleta de colores, fuentes, shaders visuales.
Tema: Graffiti Vision - Estilo retro/graffiti
"""

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont, QPainter, QPen, QBrush
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
import random

# Paleta de colores - Tema Graffiti Vision
COLORS = {
    'background': QColor(0x14, 0x0b, 0x1a),      # #140b1a - Fondo base
    'primary': QColor(0x39, 0xff, 0x14),         # #39ff14 - Verde activo
    'secondary': QColor(0xff, 0x00, 0x3c),       # #ff003c - Rojo glitch
    'accent_purple': QColor(0x5a, 0x00, 0x9d),  # #5a009d - Acento morado
    'text': QColor(0xe0, 0xe0, 0xe0),            # #e0e0e0 - Texto
}

def apply_theme(widget):
    """Aplica el tema graffiti a un widget."""
    widget.setStyleSheet(f"""
        QWidget {{
            background-color: {COLORS['background'].name()};
            color: {COLORS['text'].name()};
            font-family: 'VT323', monospace;
            border-radius: 8px;
        }}
        
        QWidget#camera {{
            background-color: {COLORS['background'].name()};
            border: 2px solid {COLORS['accent_purple'].name()};
            border-radius: 12px;
        }}
        
        QWidget#mode_panel {{
            background-color: {COLORS['background'].name()};
            border: 2px solid {COLORS['accent_purple'].name()};
            border-radius: 12px;
        }}
        
        QPushButton {{
            background-color: {COLORS['accent_purple'].name()};
            color: {COLORS['text'].name()};
            border: 2px solid {COLORS['primary'].name()};
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            min-height: 40px;
        }}
        
        QPushButton:hover {{
            background-color: {COLORS['primary'].name()};
            border-color: {COLORS['primary'].name()};
            color: {COLORS['background'].name()};
        }}
        
        QPushButton:pressed {{
            background-color: {COLORS['secondary'].name()};
            border-color: {COLORS['secondary'].name()};
        }}
        
        QPushButton:checked {{
            background-color: {COLORS['primary'].name()};
            border-color: {COLORS['primary'].name()};
            color: {COLORS['background'].name()};
        }}
        
        QPushButton:checked:hover {{
            background-color: {COLORS['primary'].name()};
            border-color: {COLORS['primary'].name()};
            color: {COLORS['background'].name()};
            border-width: 3px;
        }}
        
        QLabel {{
            color: {COLORS['text'].name()};
            font-family: 'VT323', monospace;
        }}
        
        QLabel#title {{
            font-size: 32px;
            font-weight: bold;
            color: {COLORS['primary'].name()};
        }}
        
        QLabel#subtitle {{
            font-size: 18px;
            color: {COLORS['text'].name()};
        }}
    """)
    
    # Aplicar sombras suaves a los paneles principales usando QGraphicsDropShadowEffect
    if hasattr(widget, 'objectName'):
        obj_name = widget.objectName()
        if obj_name in ['camera', 'mode_panel']:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)
            shadow.setXOffset(0)
            shadow.setYOffset(4)
            shadow.setColor(QColor(0, 0, 0, 150))  # Sombra negra semi-transparente
            widget.setGraphicsEffect(shadow)

def apply_shadow(widget):
    """Aplica una sombra suave a un widget."""
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setXOffset(0)
    shadow.setYOffset(4)
    shadow.setColor(QColor(0, 0, 0, 150))
    widget.setGraphicsEffect(shadow)

def get_title_font():
    """Retorna la fuente para títulos."""
    font = QFont('VT323', 32)
    font.setBold(True)
    return font

def get_subtitle_font():
    """Retorna la fuente para subtítulos."""
    font = QFont('VT323', 18)
    return font

def get_button_font():
    """Retorna la fuente para botones."""
    font = QFont('VT323', 16)
    font.setBold(True)
    return font

def create_crt_overlay_widget(parent=None):
    """
    Crea un widget overlay con textura visual tipo CRT.
    
    Returns:
        QWidget: Widget con efecto CRT que se puede superponer
    """
    class CRTOverlay(QWidget):
        """Widget overlay con efecto CRT (monitor de tubo de rayos catódicos)."""
        
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
            self.setAttribute(Qt.WA_NoSystemBackground, True)
            self.scanline_offset = 0
            self.static_noise = []
            self.init_static()
            
            # Timer para animar las líneas de escaneo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_animation)
            self.timer.start(50)  # 20 FPS para animación suave
        
        def init_static(self):
            """Inicializa el ruido estático."""
            self.static_noise = []
            for _ in range(50):
                self.static_noise.append({
                    'x': random.randint(0, 1000),
                    'y': random.randint(0, 800),
                    'size': random.randint(1, 3),
                    'alpha': random.randint(10, 40)
                })
        
        def update_animation(self):
            """Actualiza la animación de las líneas de escaneo."""
            self.scanline_offset += 2
            if self.scanline_offset > 4:
                self.scanline_offset = 0
            
            # Actualizar ruido estático ocasionalmente
            if random.random() < 0.1:
                for noise in self.static_noise:
                    noise['x'] = random.randint(0, self.width() if self.width() > 0 else 1000)
                    noise['y'] = random.randint(0, self.height() if self.height() > 0 else 800)
            
            self.update()
        
        def paintEvent(self, event):
            """Pinta el efecto CRT."""
            if not self.isVisible():
                return
                
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing, False)
            
            # Líneas de escaneo horizontales (efecto CRT)
            scanline_color = QColor(0, 255, 0, 8)  # Verde muy tenue
            painter.setPen(QPen(scanline_color, 1))
            
            for y in range(0, self.height(), 3):
                painter.drawLine(0, y + self.scanline_offset, self.width(), y + self.scanline_offset)
            
            # Vignette (oscurecimiento en los bordes)
            vignette_color = QColor(0, 0, 0, 30)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(vignette_color))
            
            # Gradiente radial simulado con múltiples círculos
            center_x, center_y = self.width() // 2, self.height() // 2
            max_radius = max(self.width(), self.height())
            
            for i in range(5):
                alpha = 30 - (i * 5)
                if alpha > 0:
                    vignette_color.setAlpha(alpha)
                    painter.setBrush(QBrush(vignette_color))
                    radius = max_radius * 0.6 + (i * max_radius * 0.1)
                    painter.drawEllipse(
                        int(center_x - radius), int(center_y - radius),
                        int(radius * 2), int(radius * 2)
                    )
            
            # Ruido estático sutil
            noise_color = QColor(255, 255, 255)
            for noise in self.static_noise[:20]:  # Solo mostrar algunos puntos
                if 0 <= noise['x'] < self.width() and 0 <= noise['y'] < self.height():
                    noise_color.setAlpha(noise['alpha'])
                    painter.setPen(QPen(noise_color, noise['size']))
                    painter.drawPoint(noise['x'], noise['y'])
            
            # Línea de escaneo brillante (efecto de barrido)
            if random.random() < 0.3:
                scanline_bright = QColor(0, 255, 0, 15)
                painter.setPen(QPen(scanline_bright, 2))
                scan_y = int(self.height() * 0.3 + self.scanline_offset * 10) % self.height()
                painter.drawLine(0, scan_y, self.width(), scan_y)
    
    return CRTOverlay(parent)
