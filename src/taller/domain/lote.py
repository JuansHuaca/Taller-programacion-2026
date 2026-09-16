from __future__ import annotations


class Lote:
    """Representa el lote asociado a un medicamento."""

    def __init__(self, codigo_lote: str, fecha_vencimiento: str) -> None:
        self.codigo_lote: str = codigo_lote
        self.fecha_vencimiento: str = fecha_vencimiento

    def __repr__(self) -> str:
        return (
            f"Lote(codigo_lote={self.codigo_lote!r}, "
            f"fecha_vencimiento={self.fecha_vencimiento!r})"
        )
