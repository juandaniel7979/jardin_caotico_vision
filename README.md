# Graffiti Vision

Aplicación de cámara con seguimiento de manos, cuerpo, filtros y dibujo. Interfaz moderna con estilo graffiti/retro.

## Características

- 🎨 Interfaz con tema graffiti/retro
- 👋 Modo Hand Tracking (pendiente)
- 🕺 Modo Body Tracking (pendiente)
- 🎨 Modo Filters (pendiente)
- ✏️ Modo Draw (pendiente)
- 📹 Vista de cámara con placeholder al 60%
- ✨ Fondo animado con graffitis

## Estructura del Proyecto

```
/camera_app/
│
├── src/
│   ├── main.py                # Punto de entrada
│   ├── ui/
│   │   ├── layout.py          # Diseño general (paneles, distribución)
│   │   ├── styles.py          # Paleta de colores, fuentes, shaders visuales
│   │   ├── widgets/
│   │   │   ├── camera_view.py # Componente del feed de cámara
│   │   │   ├── mode_panel.py  # Panel de modos (hand/body/filter/draw)
│   │   │   └── graffiti_bg.py # Capa de fondo con graffitis animados
│   │
│   ├── modules/
│   │   ├── hand_tracking/
│   │   │   ├── core.py
│   │   │   └── ui.py
│   │   ├── body_tracking/
│   │   │   ├── core.py
│   │   │   └── ui.py
│   │   └── filters/
│   │       ├── core.py
│   │       └── ui.py
│   │
│   ├── core/
│   │   ├── camera_manager.py  # Gestión de cámaras, cv2 o MediaPipe
│   │   ├── video_renderer.py  # Renderizado en tiempo real
│   │   └── utils.py
│   │
│   └── assets/
│       ├── graffiti_textures/
│       ├── fonts/
│       ├── icons/
│       └── shaders/
│
├── requirements.txt
└── README.md
```

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación:
```bash
python src/main.py
```

### Interfaz

- **Panel izquierdo**: Selección de modos y control de cámara
- **Panel derecho**: Vista de cámara con fondo animado de graffitis

### Controles

- Seleccionar un modo (Hand/Body/Filter/Draw) para activarlo
- Usar el botón "Iniciar Cámara" para activar/desactivar el feed
- La cámara muestra un placeholder animado (60% implementado)

## Estado del Proyecto

- ✅ Interfaz base completa
- ✅ Estilos y tema graffiti/retro
- ✅ Panel de modos funcional
- ✅ Vista de cámara placeholder (60%)
- ✅ Fondo animado con graffitis
- ⏳ Integración con OpenCV/MediaPipe (pendiente)
- ⏳ Módulos de tracking (pendiente)
- ⏳ Filtros y efectos (pendiente)

## Stack Tecnológico

- **Python 3.8+**
- **PySide6**: Framework de interfaz gráfica
- **NumPy**: Operaciones numéricas (preparado para OpenCV)

