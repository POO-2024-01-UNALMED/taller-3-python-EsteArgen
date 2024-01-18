from televisores.tv import TV
from televisores.marca import Marca
from televisores.control import Control


def testAtributosMarca():

    marca1 = Marca("Ipple")
    marca2 = Marca("Mitorola")

    marca2.setNombre("Hauwei")

    ok = False
    if marca1.getNombre() == "Ipple" and \
            marca2.getNombre() == "Hauwei":
        ok = True

    assert ok, "Hay un problema con los metodos get/set o con el valor de los atributos de Marca"


def testAtributosTV():

    marca1 = Marca("Mitorola")
    marca2 = Marca("Ipple")

    control = Control()

    tv1 = TV(marca1, False)
    tv2 = TV(marca1, True)

    tv2.setCanal(5)
    tv2.setPrecio(1000)
    tv2.setVolumen(3)
    tv2.setControl(control)
    tv2.setMarca(marca2)

    ok = False
    if tv1.getMarca().getNombre() == "Mitorola" and tv1.getCanal() == 1 and tv1.getVolumen() == 1 and tv1.getPrecio() == 500 and not(tv1.getEstado()) and \
            tv2.getMarca().getNombre() == "Ipple" and tv2.getCanal() == 5 and tv2.getVolumen() == 3 and tv2.getPrecio() == 1000 and tv2.getEstado() and tv2.getControl() is not None:
        ok = True

    assert ok, "Hay un problema con los metodos get/set o con el valor de los atributos de TV"


def testAtributosControl():

    marca = Marca("Mitorola")
    tv = TV(marca, False)

    control = Control()

    control.setTv(tv)

    ok = False
    if control.getTv() is not None:
        ok = True

    assert ok, "Hay un problema con los metodos get/set o con el valor de los atributos de Control"


def testContadorTVs():

    TV.setNumTV(0)

    marca = Marca("Semsung")

    tv1 = TV(marca, True)
    tv2 = TV(marca, True)
    tv3 = TV(marca, True)
    tv4 = TV(marca, True)

    assert TV.getNumTV() == 4, "Hay problemas con los metodos get/set o con el valor del atributo de clase que cuenta el numero de objetos de tipo de TV creados"
