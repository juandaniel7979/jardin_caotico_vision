# src/ui/main_window.py
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve
from src.modules.hand_tracking.ui import HandTrackingWidget
from src.modules.base_module import BaseModule
from src.core.frame_broker import FrameBroker

self.frame_broker = FrameBroker()
self.camera_view = CameraView(self.frame_broker)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jardín Caótico Vision")

        self.stack = QStackedWidget()
        self.modules = {}
        self.current_index = 0

        # Crear módulos
        self.register_module("hand_tracking", HandTrackingWidget())
        # (Luego podrás agregar otros módulos como body_tracking, filters, etc.)

        # Controles laterales
        self.buttons_container = QWidget()
        layout = QVBoxLayout()
        for name in self.modules.keys():
            btn = QPushButton(name.replace("_", " ").title())
            btn.clicked.connect(lambda checked, mode=mode_name: self.switch_mode(mode))

            layout.addWidget(btn)
        self.buttons_container.setLayout(layout)

        # Layout general
        central = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        main_layout.addWidget(self.buttons_container)
        central.setLayout(main_layout)
        self.setCentralWidget(central)

        # dentro de MainWindow.__init__
        camera_menu = self.menuBar().addMenu("Cámara")
        select_camera_action = camera_menu.addAction("Seleccionar cámara...")
        select_camera_action.triggered.connect(self.select_camera)

        # agrega este método
        def select_camera(self):
            dialog = CameraSelector(self)
            if dialog.exec():
                cam_index = dialog.selected_camera_index()
                if cam_index is not None:
                    print(f"📷 Usando cámara {cam_index}")
                    self.frame_broker.set_camera_index(cam_index)

    def register_module(self, name, widget: BaseModule):
        self.modules[name] = widget
        self.stack.addWidget(widget)

    def switch_to_module(self, name):
        """Animación de transición entre módulos (como un muro desplazándose)."""
        new_index = list(self.modules.keys()).index(name)
        old_widget = self.stack.currentWidget()
        new_widget = self.stack.widget(new_index)

        # Animación tipo “muro deslizante”
        animation = QPropertyAnimation(self.stack, b"geometry")
        animation.setDuration(800)
        animation.setEasingCurve(QEasingCurve.InOutCubic)

        rect = self.stack.geometry()
        offscreen = QRect(rect.x() + rect.width(), rect.y(), rect.width(), rect.height())

        animation.setStartValue(rect)
        animation.setEndValue(offscreen)
        animation.finished.connect(lambda: self.finish_switch(new_index))
        animation.start()

    def finish_switch(self, new_index):
        self.stack.setCurrentIndex(new_index)
