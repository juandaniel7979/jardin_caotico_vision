# src/core/frame_broker.py
import threading

class FrameBroker:
    """Gestiona el último frame disponible entre módulos."""
    def __init__(self):
        self._lock = threading.Lock()
        self._latest_frame = None

    def set_latest_frame(self, frame):
        with self._lock:
            self._latest_frame = frame

    def get_latest_frame(self):
        with self._lock:
            return self._latest_frame
