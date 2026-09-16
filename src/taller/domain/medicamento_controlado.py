from __future__ import annotations

from .lote import Lote
from .medicamento import Medicamento


class MedicamentoControlado(Medicamento):
    """Medicamento con requisitos adicionales de control.

    Demuestra Herencia al extender la clase abstracta Medicamento.
    """

    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        lote: Lote,
        registro_medico: str,
    ) -> None:
        super().__init__(nombre=nombre, precio=precio, stock=stock, lote=lote)
        self.registro_medico: str = registro_medico

    @property
    def registro_medico(self) -> str:
        return self._registro_medico

    @registro_medico.setter
    def registro_medico(self, value: str) -> None:
        if not value.strip():
            raise ValueError("El registro médico es obligatorio.")
        self._registro_medico = value.strip()

    def validar_venta(self, cantidad: int) -> bool:
        """Valida la venta sólo si el registro médico fue informado."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")

        if not self.registro_medico:
            return False

        return self.stock >= cantidad
