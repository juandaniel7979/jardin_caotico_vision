from PySide6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton, QLabel
import cv2

class CameraSelector(QDialog):
    """Ventana emergente para elegir cámara disponible."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar cámara")
        self.resize(300, 150)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Selecciona una cámara:"))

        self.combo = QComboBox()
        layout.addWidget(self.combo)

        self.refresh_button = QPushButton("🔄 Buscar cámaras")
        self.ok_button = QPushButton("Aceptar")
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.ok_button)

        self.refresh_button.clicked.connect(self.scan_cameras)
        self.ok_button.clicked.connect(self.accept)

        self.scan_cameras()

    def scan_cameras(self):
        """Escanea cámaras disponibles (0–5)."""
        self.combo.clear()
        for i in range(6):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                self.combo.addItem(f"Cámara {i}")
                cap.release()
        if self.combo.count() == 0:
            self.combo.addItem("❌ Ninguna cámara detectada")

    def selected_camera_index(self):
        text = self.combo.currentText()
        if "Cámara" in text:
            return int(text.split()[-1])
        return None
