"""
UI para el módulo de seguimiento de manos.
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from ...ui.styles import COLORS, apply_theme


class HandTrackingUI(QWidget):
    """Interfaz de usuario para opciones de seguimiento de manos."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Layout vertical
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Label placeholder
        label = QLabel("Hand Tracking Options Placeholder")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(f"""
            QLabel {{
                color: {COLORS['text'].name()};
                font-family: 'VT323', monospace;
                font-size: 20px;
                padding: 20px;
                background-color: {COLORS['background'].name()};
                border: 1px solid {COLORS['accent_purple'].name()};
                border-radius: 8px;
            }}
        """)
        layout.addWidget(label)
        
        # Aplicar tema
        apply_theme(self)
