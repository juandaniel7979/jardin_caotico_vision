# src/modules/hand_tracking/core.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from .base_module import BaseModule

class HandTrackingModule(BaseModule):
    def __init__(self, frame_broker):
        super().__init__(frame_broker)
        self.ui_widget = QWidget()
        layout = QVBoxLayout(self.ui_widget)
        layout.addWidget(QLabel("Hand Tracking - opciones placeholder"))

    def start(self):
        self.active = True
        # inicializar modelos cuando quieras (MediaPipe)

    def stop(self):
        self.active = False

    def process(self, frame):
        # por ahora devuelve None; más adelante devuelve overlay
        return None

    def get_ui(self):
        return self.ui_widget
