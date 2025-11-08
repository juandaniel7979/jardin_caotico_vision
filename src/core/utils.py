"""
Utilidades generales.
Para funciones auxiliares de logs, color, tiempo, etc.
"""

import logging
from datetime import datetime
from typing import Tuple, Optional


def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
    """
    Configura un logger con formato estándar.
    
    Args:
        name: Nombre del logger
        level: Nivel de logging (default: INFO)
    
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger


def get_timestamp() -> str:
    """
    Retorna un timestamp formateado.
    
    Returns:
        str: Timestamp en formato YYYY-MM-DD HH:MM:SS
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convierte un color hexadecimal a RGB.
    
    Args:
        hex_color: Color en formato hexadecimal (ej: "#39ff14")
    
    Returns:
        Tuple con valores RGB (r, g, b)
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convierte valores RGB a color hexadecimal.
    
    Args:
        r: Componente rojo (0-255)
        g: Componente verde (0-255)
        b: Componente azul (0-255)
    
    Returns:
        str: Color en formato hexadecimal
    """
    return f"#{r:02x}{g:02x}{b:02x}"


def clamp_value(value: float, min_val: float, max_val: float) -> float:
    """
    Limita un valor entre un mínimo y máximo.
    
    Args:
        value: Valor a limitar
        min_val: Valor mínimo
        max_val: Valor máximo
    
    Returns:
        float: Valor limitado
    """
    return max(min_val, min(max_val, value))


def format_fps(fps: float) -> str:
    """
    Formatea un valor de FPS para mostrar.
    
    Args:
        fps: Frames por segundo
    
    Returns:
        str: FPS formateado (ej: "30.0 FPS")
    """
    return f"{fps:.1f} FPS"

# TODO (Cursor): implementar más adelante
