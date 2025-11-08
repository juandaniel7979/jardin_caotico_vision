"""
Gestión de cámaras, cv2 o MediaPipe.
Agregará captura OpenCV más adelante.
"""


class CameraManager:
    """Gestiona la captura de video desde cámaras usando OpenCV."""
    
    def __init__(self):
        """Inicializa el gestor de cámara."""
        self.camera_index = 0
        self.is_capturing = False
        # Más adelante: self.cap = None (cv2.VideoCapture)
    
    def start_capture(self, camera_index=0):
        """
        Inicia la captura de video desde una cámara.
        
        Args:
            camera_index: Índice de la cámara a usar (default: 0)
        
        Returns:
            bool: True si la captura se inició correctamente
        """
        self.camera_index = camera_index
        # Más adelante: implementar con cv2.VideoCapture
        self.is_capturing = True
        return True
    
    def stop_capture(self):
        """Detiene la captura de video."""
        # Más adelante: self.cap.release() si existe
        self.is_capturing = False
    
    def read_frame(self):
        """
        Lee un frame de la cámara.
        
        Returns:
            frame: Frame capturado (más adelante será numpy array)
        """
        # Más adelante: return self.cap.read()
        return None
    
    def is_opened(self):
        """
        Verifica si la cámara está abierta y funcionando.
        
        Returns:
            bool: True si la cámara está abierta
        """
        return self.is_capturing

# TODO (Cursor): implementar más adelante
