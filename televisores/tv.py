from __future__ import annotations

class TV:
    _numTV = 0

    def __init__(self, marca: Marca, estado: bool) -> None:
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        # self._control = None # Se puede eliminar

        TV._numTV += 1
    
    @classmethod
    def getNumTV(cls) -> int:
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numTV: int) -> None:
        cls._numTV = numTV

    def turnOn(self) -> None:
        self._estado = True

    def turnOff(self) -> None:
        self._estado = False

    def canalUp(self) -> None:
        self.setCanal(self._canal + 1)

    def canalDown(self) -> None:
        self.setCanal(self._canal - 1)

    def volumenUp(self) -> None:
        self.setVolumen(self._volumen + 1)

    def volumenDown(self) -> None:
        self.setVolumen(self._volumen - 1)

    def getMarca(self) -> Marca:
        return self._marca
    
    def getCanal(self) -> int:
        return self._canal
    
    def getPrecio(self) -> int:
        return self._precio
    
    def getVolumen(self) -> int:
        return self._volumen

    def getControl(self) -> Control:
        return self._control
    
    def getEstado(self) -> bool:
        return self._estado
    
    def setMarca(self, marca: Marca) -> None:
        self._marca = marca
    
    def setCanal(self, canal: int) -> None:
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def setPrecio(self, precio: int) -> None:
        self._precio = precio

    def setVolumen(self, volumen: int) -> None:
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def setControl(self, control: Control) -> None:
        self._control = control