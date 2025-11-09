# src/modules/base_module.py
from PySide6.QtWidgets import QWidget

class BaseModule(QWidget):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def start(self):
        """Se llama cuando el módulo se activa."""
        pass

    def stop(self):
        """Se llama cuando el módulo se desactiva."""
        pass
