"""
Capa de fondo con graffitis animados.
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer, QPoint, QRect
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
import random
import math


class GraffitiBackground(QWidget):
    """Widget que muestra un fondo animado con estilo graffiti."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_OpaquePaintEvent)
        
        # Partículas/graffitis animados
        self.particles = []
        self.init_particles()
        
        # Timer para animación
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)  # 20 FPS
        
        # Colores graffiti
        self.colors = [
            QColor(255, 100, 50),   # Naranja
            QColor(50, 200, 255),   # Azul
            QColor(255, 50, 150),   # Rosa
            QColor(100, 255, 100),  # Verde
            QColor(255, 255, 50),   # Amarillo
        ]
    
    def init_particles(self, count=15):
        """Inicializa las partículas de graffiti."""
        self.particles = []
        for _ in range(count):
            particle = {
                'x': random.randint(0, 1000),
                'y': random.randint(0, 800),
                'size': random.randint(20, 60),
                'speed_x': random.uniform(-1, 1),
                'speed_y': random.uniform(-1, 1),
                'color_idx': random.randint(0, 4),
                'rotation': random.uniform(0, 360),
                'rotation_speed': random.uniform(-2, 2),
            }
            self.particles.append(particle)
    
    def update_animation(self):
        """Actualiza la animación de las partículas."""
        if not self.isVisible():
            return
            
        width = self.width()
        height = self.height()
        
        for particle in self.particles:
            # Actualizar posición
            particle['x'] += particle['speed_x']
            particle['y'] += particle['speed_y']
            particle['rotation'] += particle['rotation_speed']
            
            # Rebote en los bordes
            if particle['x'] < 0 or particle['x'] > width:
                particle['speed_x'] *= -1
            if particle['y'] < 0 or particle['y'] > height:
                particle['speed_y'] *= -1
            
            # Mantener dentro de los límites
            particle['x'] = max(0, min(width, particle['x']))
            particle['y'] = max(0, min(height, particle['y']))
        
        self.update()
    
    def paintEvent(self, event):
        """Pinta el fondo con graffitis animados."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Fondo semi-transparente
        painter.fillRect(self.rect(), QColor(20, 20, 30, 200))
        
        # Dibujar partículas/graffitis
        for particle in self.particles:
            color = self.colors[particle['color_idx']]
            color.setAlpha(80)  # Semi-transparente
            
            painter.save()
            painter.translate(particle['x'], particle['y'])
            painter.rotate(particle['rotation'])
            
            # Dibujar formas abstractas estilo graffiti
            pen = QPen(color, 3)
            painter.setPen(pen)
            painter.setBrush(QBrush(color, Qt.BrushStyle.NoBrush))
            
            size = particle['size']
            # Dibujar estrella/pentágono
            points = []
            for i in range(5):
                angle = (i * 2 * math.pi / 5) - math.pi / 2
                x = size * 0.5 * math.cos(angle)
                y = size * 0.5 * math.sin(angle)
                points.append(QPoint(int(x), int(y)))
            
            painter.drawPolygon(points)
            
            # Dibujar círculo interno
            painter.drawEllipse(-size // 4, -size // 4, size // 2, size // 2)
            
            painter.restore()
        
        # Dibujar líneas de conexión entre partículas cercanas
        for i, p1 in enumerate(self.particles):
            for p2 in self.particles[i+1:]:
                dist = math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)
                if dist < 150:
                    color = self.colors[p1['color_idx']]
                    color.setAlpha(30)
                    pen = QPen(color, 1)
                    painter.setPen(pen)
                    painter.drawLine(int(p1['x']), int(p1['y']), 
                                   int(p2['x']), int(p2['y']))
    
    def resizeEvent(self, event):
        """Ajusta las partículas cuando cambia el tamaño."""
        super().resizeEvent(event)
        # Ajustar partículas que estén fuera de los límites
        for particle in self.particles:
            particle['x'] = max(0, min(self.width(), particle['x']))
            particle['y'] = max(0, min(self.height(), particle['y']))
