from televisores.tv import TV
from televisores.marca import Marca
from televisores.control import Control


def testOnOffTV():

    marca = Marca("Hauwei")

    tv1 = TV(marca, False)
    tv1.turnOn()

    tv2 = TV(marca, True)
    tv2.turnOff()

    tv3 = TV(marca, True)
    tv3.turnOn()

    ok = False
    if tv1.getEstado() and \
            not(tv2.getEstado()) and \
            tv3.getEstado():
        ok = True

    assert ok, "Hay un problema con el encendido o apagado del televisor"


def testEnlazarControl():

    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()

    control.enlazar(tv)

    assert control.getTv() is not None, "Hay un error en el metodo enlazar y la asignacion del objeto televisor en el control"


def testEnlazarTV():

    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()

    control.enlazar(tv)

    assert tv.getControl() is not None, "Hay un error en el metodo enlazar y la asignacion del objeto televisor en el control"


def testCanal():

    marca = Marca("Ipple")

    tv1 = TV(marca, True)
    tv1.setCanal(80)
    tv1.canalDown()
    tv1.canalUp()
    tv1.canalDown()
    tv1.canalDown()
    tv1.turnOff()
    tv1.canalUp()

    tv2 = TV(marca, False)
    tv2.setCanal(70)
    tv2.canalUp()
    tv2.canalDown()
    tv2.turnOn()
    tv2.canalUp()
    tv2.canalUp()
    tv2.canalDown()
    tv2.canalUp()

    tv3 = TV(marca, True)
    tv3.setCanal(121)
    tv3.canalUp()

    tv4 = TV(marca, True)
    tv4.setCanal(0)
    tv4.canalUp()

    tv5 = TV(marca, True)
    tv5.canalDown()

    tv6 = TV(marca, True)
    tv6.setCanal(120)
    tv6.canalUp()

    tv7 = TV(marca, True)
    tv7.setCanal(35)
    tv7.canalDown()
    tv7.setCanal(200)

    ok = False
    if tv1.getCanal() == 78 and \
            tv2.getCanal() == 3 and \
            tv3.getCanal() == 2 and \
            tv4.getCanal() == 2 and \
            tv5.getCanal() == 1 and \
            tv6.getCanal() == 120 and \
            tv7.getCanal() == 34:
        ok = True

    assert ok, "Hay un problema con los metodos y restricciones del cambio de canales del televisor"


def testCanalEnlazar():
    
    marca = Marca("Ipple")

    tv1 = TV(marca, True)
    control1 = Control()
    control1.enlazar(tv1)
    control1.setCanal(60)
    control1.canalDown()
    control1.canalUp()
    control1.canalDown()
    control1.turnOff()
    control1.canalUp()

    tv2 = TV(marca, False)
    control2 = Control()
    control2.enlazar(tv2)
    control2.setCanal(20)
    control2.canalUp()
    control2.canalDown()
    control2.turnOn()
    control2.canalUp()
    control2.canalDown()
    control2.canalUp()

    tv3 = TV(marca, True)
    control3 = Control()
    control3.enlazar(tv3)
    control3.setCanal(122)
    control3.canalUp()
    control3.canalUp()

    tv4 = TV(marca, True)
    control4 = Control()
    control4.enlazar(tv4)
    control4.setCanal(-1)
    control4.canalUp()
    control4.canalDown()

    tv5 = TV(marca, True)
    control5 = Control()
    control5.enlazar(tv5)
    control5.canalDown()
    control5.canalUp()

    tv6 = TV(marca, True)
    control6 = Control()
    control6.enlazar(tv6)
    control6.setCanal(120)
    control6.canalUp()
    control6.canalDown()

    tv7 = TV(marca, True)
    control7 = Control()
    control7.enlazar(tv7)
    control7.setCanal(35)
    control7.canalUp()
    control7.setCanal(200)

    ok = False
    if tv1.getCanal() == 59 and \
            tv2.getCanal() == 2 and \
            tv3.getCanal() == 3 and \
            tv4.getCanal() == 1 and \
            tv5.getCanal() == 2 and \
            tv6.getCanal() == 119 and \
            tv7.getCanal() == 36:
        ok = True

    assert ok, "Hay un problema con los metodos y restricciones del cambio de canales del televisor desde el control"


def testVolumen():

    marca = Marca("Mitorola")

    tv1 = TV(marca, True)
    tv1.setVolumen(5)
    tv1.volumenDown()
    tv1.volumenUp()
    tv1.volumenDown()
    tv1.volumenDown()
    tv1.turnOff()
    tv1.volumenUp()

    tv2 = TV(marca, False)
    tv2.setVolumen(3)
    tv2.volumenUp()
    tv2.volumenDown()
    tv2.turnOn()
    tv2.volumenUp()
    tv2.volumenUp()
    tv2.volumenDown()
    tv2.volumenUp()

    tv3 = TV(marca, True)
    tv3.setVolumen(9)
    tv3.volumenUp()

    tv4 = TV(marca, True)
    tv4.setVolumen(-2)
    tv4.volumenDown()

    tv5 = TV(marca, True)
    tv5.setVolumen(0)
    tv5.volumenDown()

    tv6 = TV(marca, True)
    tv6.setVolumen(7)
    tv6.volumenUp()

    tv7 = TV(marca, True)
    tv7.setVolumen(4)
    tv7.volumenDown()
    tv7.setVolumen(15)

    ok = False
    if tv1.getVolumen() == 3 and \
            tv2.getVolumen() == 3 and \
            tv3.getVolumen() == 2 and \
            tv4.getVolumen() == 0 and \
            tv5.getVolumen() == 0 and \
            tv6.getVolumen() == 7 and \
            tv7.getVolumen() == 3:
        ok = True

    assert ok, "Hay un problema con los metodos y restricciones del cambio de volumen del televisor"


def testVolumenEnlazar():

    marca = Marca("Mitorola")

    tv1 = TV(marca, True)
    control1 = Control()
    control1.enlazar(tv1)
    control1.setVolumen(6)
    control1.volumenDown()
    control1.volumenUp()
    control1.volumenDown()
    control1.turnOff()
    control1.volumenUp()

    tv2 = TV(marca, False)
    control2 = Control()
    control2.enlazar(tv2)
    control2.setVolumen(2)
    control2.volumenUp()
    control2.volumenDown()
    control2.turnOn()
    control2.volumenUp()
    control2.volumenDown()
    control2.volumenUp()

    tv3 = TV(marca, True)
    control3 = Control()
    control3.enlazar(tv3)
    control3.setVolumen(8)
    control3.volumenDown()

    tv4 = TV(marca, True)
    control4 = Control()
    control4.enlazar(tv4)
    control4.setVolumen(-1)
    control4.volumenUp()
    control4.volumenDown()

    tv5 = TV(marca, True)
    control5 = Control()
    control5.enlazar(tv5)
    control5.setVolumen(0)
    control5.volumenDown()
    control5.volumenUp()

    tv6 = TV(marca, True)
    control6 = Control()
    control6.enlazar(tv6)
    control6.setVolumen(7)
    control6.volumenUp()
    control6.volumenDown()

    tv7 = TV(marca, True)
    control7 = Control()
    control7.enlazar(tv7)
    control7.setVolumen(3)
    control7.volumenUp()
    control7.setVolumen(26)

    ok = False
    if tv1.getVolumen() == 5 and \
            tv2.getVolumen() == 2 and \
            tv3.getVolumen() == 0 and \
            tv4.getVolumen() == 1 and \
            tv5.getVolumen() == 1 and \
            tv6.getVolumen() == 6 and \
            tv7.getVolumen() == 4:
        ok = True

    assert ok, "Hay un problema con los metodos y restricciones del cambio de canales del televisor desde el control"
