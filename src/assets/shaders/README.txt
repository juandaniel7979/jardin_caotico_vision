Directorio de shaders GLSL

Este directorio contendrá shaders GLSL (OpenGL Shading Language) para
aplicar efectos visuales en tiempo real sobre el feed de video.

Efectos planificados:
- CRT (efecto de monitor de tubo de rayos catódicos)
- Ruido/static
- Distorsión/glitch
- Efectos de color y post-procesamiento
- Overlays y efectos de graffiti

Formato:
- Archivos .glsl o .frag (fragment shaders)
- Archivos .vert (vertex shaders, si es necesario)

Los shaders se cargarán y aplicarán usando PySide6/Qt o OpenGL
para renderizado en tiempo real sobre los frames de video.

