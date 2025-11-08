"""
Panel de modos (hand/body/filter/draw).
Botones tipo "ladrillo" con colores verde/rojo según estado.
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QButtonGroup
from PySide6.QtCore import Qt, Signal
from ..styles import COLORS, get_button_font


class ModePanel(QWidget):
    """Panel de selección de modos con botones tipo ladrillo."""
    
    # Señal emitida cuando se cambia el modo
    mode_changed = Signal(str)
    
    MODES = {
        'hand': 'Hand Tracking',
        'body': 'Body Tracking',
        'filters': 'Filters',
        'draw': 'Draw Mode'
    }
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_mode = None
        
        # Layout vertical
        layout = QVBoxLayout(self)
        layout.setSpacing(12)  # Espaciado uniforme
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Grupo de botones (solo uno seleccionado a la vez)
        self.button_group = QButtonGroup(self)
        self.buttons = {}
        
        # Crear botones para cada modo
        for mode_key, mode_label in self.MODES.items():
            button = QPushButton(mode_label)
            button.setCheckable(True)
            button.setMinimumHeight(60)  # Altura tipo "ladrillo"
            
            # Estilo inicial (inactivo - rojo glitch)
            self._update_button_style(button, False)
            
            # Conectar señal
            button.clicked.connect(lambda checked, m=mode_key: self._on_mode_selected(m))
            
            # Agregar al grupo y al layout
            self.button_group.addButton(button)
            self.buttons[mode_key] = button
            layout.addWidget(button)
        
        # Espaciador al final
        layout.addStretch()
        
        # Botón de control de cámara (separado)
        self.camera_button = QPushButton("▶ Iniciar Cámara")
        self.camera_button.setMinimumHeight(60)
        self._update_camera_button_style(False)
        self.camera_button.clicked.connect(self._toggle_camera)
        layout.addWidget(self.camera_button)
        
        self.camera_running = False
    
    def _update_button_style(self, button, is_active):
        """Actualiza el estilo de un botón según su estado."""
        if is_active:
            # Verde radioactivo cuando está activo
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {COLORS['primary'].name()};
                    color: {COLORS['background'].name()};
                    border: 2px solid {COLORS['primary'].name()};
                    border-radius: 8px;
                    padding: 15px 20px;
                    font-size: 18px;
                    font-weight: bold;
                    font-family: 'VT323', monospace;
                }}
                QPushButton:hover {{
                    background-color: {COLORS['primary'].name()};
                    border-color: {COLORS['primary'].name()};
                    opacity: 0.9;
                }}
            """)
        else:
            # Rojo glitch cuando está inactivo
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {COLORS['secondary'].name()};
                    color: {COLORS['text'].name()};
                    border: 2px solid {COLORS['secondary'].name()};
                    border-radius: 8px;
                    padding: 15px 20px;
                    font-size: 18px;
                    font-weight: bold;
                    font-family: 'VT323', monospace;
                }}
                QPushButton:hover {{
                    background-color: {COLORS['secondary'].name()};
                    border-color: {COLORS['secondary'].name()};
                    opacity: 0.9;
                }}
            """)
    
    def _update_camera_button_style(self, is_running):
        """Actualiza el estilo del botón de cámara."""
        if is_running:
            self.camera_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {COLORS['primary'].name()};
                    color: {COLORS['background'].name()};
                    border: 2px solid {COLORS['primary'].name()};
                    border-radius: 8px;
                    padding: 15px 20px;
                    font-size: 18px;
                    font-weight: bold;
                    font-family: 'VT323', monospace;
                }}
                QPushButton:hover {{
                    opacity: 0.9;
                }}
            """)
        else:
            self.camera_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {COLORS['accent_purple'].name()};
                    color: {COLORS['text'].name()};
                    border: 2px solid {COLORS['primary'].name()};
                    border-radius: 8px;
                    padding: 15px 20px;
                    font-size: 18px;
                    font-weight: bold;
                    font-family: 'VT323', monospace;
                }}
                QPushButton:hover {{
                    background-color: {COLORS['primary'].name()};
                    color: {COLORS['background'].name()};
                }}
            """)
    
    def _on_mode_selected(self, mode):
        """Maneja la selección de un modo."""
        # Actualizar estado de todos los botones
        for mode_key, button in self.buttons.items():
            is_active = (mode_key == mode)
            button.setChecked(is_active)
            self._update_button_style(button, is_active)
        
        # Actualizar modo actual y emitir señal
        self.current_mode = mode
        self.mode_changed.emit(mode)
    
    def _toggle_camera(self):
        """Alterna el estado de la cámara."""
        self.camera_running = not self.camera_running
        if self.camera_running:
            self.camera_button.setText("⏸ Detener Cámara")
        else:
            self.camera_button.setText("▶ Iniciar Cámara")
        
        self._update_camera_button_style(self.camera_running)
    
    def get_camera_state(self):
        """Retorna el estado actual de la cámara."""
        return self.camera_running
    
    def set_mode(self, mode):
        """Establece un modo específico."""
        if mode in self.buttons:
            self._on_mode_selected(mode)
    
    def get_current_mode(self):
        """Retorna el modo actualmente activo."""
        return self.current_mode

# TODO (Cursor): añadir animación de cambio de color al cambiar modo
# TODO (Cursor): actualizar panel de opciones de la derecha según el modo activo
# TODO (Cursor): permitir personalizar etiquetas o íconos en cada modo
