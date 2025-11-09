# src/modules/hand_tracking/ui.py
from PySide6.QtWidgets import QVBoxLayout, QLabel
from src.modules.base_module import BaseModule

class HandTrackingWidget(BaseModule):
    def __init__(self):
        super().__init__("Hand Tracking")
        self.label = QLabel("Hand Tracking View Active")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def start(self):
        self.label.setText("Tracking iniciado...")

    def stop(self):
        self.label.setText("Tracking detenido")
