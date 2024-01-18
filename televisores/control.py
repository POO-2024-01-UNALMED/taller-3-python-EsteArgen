from __future__ import annotations

class Control:
    # def __init__(self) -> None: # Se puede eliminar
    #     self._tv = None    # Se puede eliminar

    def enlazar(self, tv: TV):
        self._tv = tv
        tv.setControl(self)

    def turnOn(self) -> None:
        self._tv.turnOn()

    def turnOff(self) -> None:
        self._tv.turnOff()

    def canalUp(self) -> None:
        self._tv.canalUp()
    
    def canalDown(self) -> None:
        self._tv.canalDown()

    def volumenUp(self) -> None:
        self._tv.volumenUp()

    def volumenDown(self) -> None:
        self._tv.volumenDown()

    def setCanal(self, canal: int) -> None:
        self._tv.setCanal(canal)

    def setVolumen(self, volumen: int) -> None:
        self._tv.setVolumen(volumen)

    def getTv(self) -> TV:
        return self._tv
    
    def setTv(self, tv: TV) -> None:
        self._tv = tv
    