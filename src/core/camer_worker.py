# src/core/camera_worker.py
import cv2
import threading
import time

class CameraWorker(threading.Thread):
    """Captura frames de la cámara en un hilo separado."""
    def __init__(self, frame_broker, cam_index=0):
        super().__init__(daemon=True)
        self.frame_broker = frame_broker
        self.cam_index = cam_index
        self.running = False
        self.cap = None

    def run(self):
        """Loop principal de captura."""
        self.cap = cv2.VideoCapture(self.cam_index)
        if not self.cap.isOpened():
            print(f"⚠️ No se pudo abrir la cámara {self.cam_index}")
            return

        self.running = True
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame_broker.set_latest_frame(frame)
            time.sleep(0.01)  # evita uso excesivo de CPU

        self.cap.release()

    def stop(self):
        self.running = False

    def set_camera_index(self, index):
        """Permite cambiar de cámara en tiempo real."""
        self.cam_index = index
        self.stop()
        time.sleep(0.2)
        self.start()
