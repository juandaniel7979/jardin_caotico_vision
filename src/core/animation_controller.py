# src/core/animation_controller.py
from PySide6.QtCore import QObject, QPropertyAnimation, Property

class AnimationController(QObject):
    def __init__(self, target_widget):
        super().__init__()
        self._offset = 0
        self.target = target_widget
        self.anim = QPropertyAnimation(self, b"offset")
        self.anim.setDuration(1000)
        self.anim.setStartValue(0)
        self.anim.setEndValue(300)

    def get_offset(self):
        return self._offset

    def set_offset(self, value):
        self._offset = value
        self.target.update()

    offset = Property(int, get_offset, set_offset)

    def play(self, direction="right"):
        self.anim.setDirection(
            QPropertyAnimation.Forward if direction in ["right", "down"] else QPropertyAnimation.Backward
        )
        self.anim.start()
