class Auto():
    """Clase de abstraccion"""
    gasolina=0
    def __init__(gasolina):
       Auto.gasolina = gasolina 
       print "Tenemos", gasolina, "litros"
       
    @staticmethod
    def arrancar(gasolina):
        if gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"
    
    @staticmethod
    def moverse(gasolina):
            if gasolina > 0:
               gasolina -= 1
               print "Quedan", gasolina, "litros"
            else:
               print "No hay gasolina para moverse..."

