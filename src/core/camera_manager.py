# src/core/camera_manager.py
import cv2
import threading
import time

class CameraManager(threading.Thread):
    def __init__(self, broker, camera_index=0):
        super().__init__(daemon=True)
        self.broker = broker
        self.camera_index = camera_index
        self.running = False

    def run(self):
        cap = cv2.VideoCapture(self.camera_index)
        if not cap.isOpened():
            print("⚠️ No se pudo abrir la cámara")
            return

        self.running = True
        while self.running:
            ret, frame = cap.read()
            if not ret:
                continue
            self.broker.set_frame(frame)
            time.sleep(0.02)  # ~50 fps

        cap.release()

    def stop(self):
        self.running = False
