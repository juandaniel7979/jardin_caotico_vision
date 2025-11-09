"""
Diseño general de la aplicación (paneles, distribución).
"""

from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from .styles import apply_theme, create_crt_overlay_widget
from .widgets.camera_view import CameraView
from .widgets.mode_panel import ModePanel
from src.core.frame_broker import FrameBroker


class MainWindow(QWidget):
    """Ventana principal de la aplicación Graffiti Vision."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Graffiti Vision")
        self.setMinimumSize(1280, 720)
        
        # Aplicar tema
        apply_theme(self)
        
        # Layout principal horizontal
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(8)
        
        # Panel izquierdo: CameraView (60%)
        self.frame_broker = FrameBroker()
        self.camera_view = CameraView(self.frame_broker)
        self.camera_view.setObjectName("camera")
        apply_theme(self.camera_view)
        main_layout.addWidget(self.camera_view, stretch=60)
        
        # Panel derecho: ModePanel (40%)
        self.mode_panel = ModePanel()
        self.mode_panel.setObjectName("mode_panel")
        apply_theme(self.mode_panel)
        main_layout.addWidget(self.mode_panel, stretch=40)
        
        # Conectar señales
        self.mode_panel.mode_changed.connect(self._on_mode_changed)
        
        # Conectar botón de cámara (usando un timer para verificar estado)
        from PySide6.QtCore import QTimer
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self._check_camera_state)
        self.camera_timer.start(100)  # Verificar cada 100ms
        
        # Aplicar efecto CRT en el fondo (debe estar detrás de los widgets)
        self.crt_overlay = create_crt_overlay_widget(self)
        self.crt_overlay.resize(self.size())
        self.crt_overlay.lower()  # Enviar al fondo
        self.crt_overlay.show()
    
    def resizeEvent(self, event):
        """Ajusta el overlay CRT cuando cambia el tamaño de la ventana."""
        super().resizeEvent(event)
        if hasattr(self, 'crt_overlay'):
            self.crt_overlay.resize(self.size())
    
    def _on_mode_changed(self, mode):
        """Maneja el cambio de modo."""
        print(f"Modo cambiado a: {mode}")
        # Aquí se implementará la lógica de cada modo
    
    def _check_camera_state(self):
        """Verifica el estado de la cámara y actualiza."""
        camera_running = self.mode_panel.get_camera_state()
        if camera_running and not self.camera_view.camera_active:
            self.camera_view.start_camera()
        elif not camera_running and self.camera_view.camera_active:
            self.camera_view.stop_camera()

# TODO (Cursor): agregar barra superior más adelante con título grande y efectos glitch
# TODO (Cursor): agregar zona inferior para graffitis animados