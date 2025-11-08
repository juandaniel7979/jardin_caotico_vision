"""
Punto de entrada principal de la aplicación Graffiti Vision.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui.layout import MainWindow as MainWidget


def main():
    """Función principal de la aplicación."""
    # Configurar aplicación
    app = QApplication(sys.argv)
    app.setApplicationName("Graffiti Vision")
    app.setOrganizationName("Graffiti Vision")
    
    # Crear ventana principal
    main_window = QMainWindow()
    main_window.setWindowTitle("Graffiti Vision")
    
    # Crear widget principal y establecerlo como central
    main_widget = MainWidget()
    main_window.setCentralWidget(main_widget)
    
    # Mostrar ventana
    main_window.show()
    
    # Ejecutar aplicación
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
