from typing import Optional


def validar_valor(texto: str) -> bool:
    try:
        return float(texto) > 0
    except ValueError:
        return False


def validar_texto_obrigatorio(texto: Optional[str]) -> bool:
    return bool(texto and texto.strip())
