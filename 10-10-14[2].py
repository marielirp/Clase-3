class Helo():
    pass


class Auto():
    """Esta clase va arrancar un auto segun su gasolina"""
    
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"


    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"

    def moverse(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No hay gasolina para moverse..."


mi_auto=Auto(5)
#Gasolina ingresada
print mi_auto.gasolina
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()
mi_auto.moverse()





    
