"""
Componente visual que muestra el feed de la cámara con OpenCV.
Integra un sistema de frame broker y permite aplicar procesadores
(HandTracking, filtros, etc.) sobre el frame antes de dibujarlo.
"""

import cv2
import numpy as np
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPainter
from ..styles import COLORS, get_title_font


class CameraView(QLabel):
    """Widget que muestra el feed de la cámara con OpenCV en tiempo real."""

    def __init__(self, frame_broker, parent=None):
        super().__init__(parent)
        self.frame_broker = frame_broker
        self.current_processor = None  # Procesador activo (hand tracking, filtros, etc.)
        self.camera_active = False
        self.cap = None

        # Configuración visual inicial
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText("CAMERA OFF")

        font = get_title_font()
        font.setPointSize(28)
        self.setFont(font)

        self.setStyleSheet(f"""
            QLabel {{
                background-color: black;
                color: {COLORS['text'].name()};
                border: 3px solid {COLORS['accent_purple'].name()};
                border-radius: 12px;
            }}
        """)

        # Temporizador para refrescar frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.setInterval(30)  # ~33 fps

    # ──────────────────────────────────────────────
    # CONTROL DE CÁMARA
    # ──────────────────────────────────────────────
    def start_camera(self, camera_index=0):
        """Inicia la cámara (por defecto la webcam principal)."""
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            self.setText("❌ ERROR: Cámara no disponible")
            return

        self.camera_active = True
        self.setText("")
        self.timer.start()

    def stop_camera(self):
        """Detiene la cámara y limpia el feed."""
        self.camera_active = False
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.cap = None
        self.setText("CAMERA OFF")
        self.update()

    # ──────────────────────────────────────────────
    # ACTUALIZACIÓN DE FRAME
    # ──────────────────────────────────────────────
    def update_frame(self):
        """Captura y muestra el siguiente frame."""
        if not self.camera_active or not self.cap:
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        # Almacena el frame en el frame_broker
        self.frame_broker.set_latest_frame(frame)

        # Procesar si hay procesador activo (e.g. hand tracking)
        if self.current_processor:
            frame = self.current_processor.process(frame)

        # Convertir BGR (OpenCV) → RGB (Qt)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # Dibujar el frame sobre el widget
        painter = QPainter(self)
        painter.drawImage(self.rect(), qt_image)
        painter.end()

    # ──────────────────────────────────────────────
    # UTILIDADES
    # ──────────────────────────────────────────────
    def set_processor(self, processor):
        """Asigna el procesador actual (por ejemplo, hand tracking)."""
        self.current_processor = processor

    def get_camera_state(self):
        """Retorna True si la cámara está activa."""
        return self.camera_active
