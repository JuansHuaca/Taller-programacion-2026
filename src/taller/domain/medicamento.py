from __future__ import annotations

from abc import ABC, abstractmethod

from .lote import Lote


class Medicamento(ABC):
    """Clase base abstracta para todos los medicamentos.

    Demuestra:
    - Abstracción: expone una interfaz común mediante el método abstracto.
    - Encapsulamiento: atributos protegidos con propiedades.
    - Composición: depende de una instancia de Lote inyectada.
    """

    def __init__(self, nombre: str, precio: float, stock: int, lote: Lote) -> None:
        self._nombre: str = nombre
        self._precio: float = precio
        self._stock: int = stock
        self._lote: Lote = lote

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float) -> None:
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = value

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        if value < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = value

    @property
    def lote(self) -> Lote:
        return self._lote

    @lote.setter
    def lote(self, value: Lote) -> None:
        if not isinstance(value, Lote):
            raise TypeError("El lote debe ser una instancia de Lote.")
        self._lote = value

    @abstractmethod
    def validar_venta(self, cantidad: int) -> bool:
        """Valida si una venta es permitida para el medicamento."""
        raise NotImplementedError
