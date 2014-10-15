class Auto():
    """Esta clase va arrancar un auto segun su gasolina"""
    
    gasolina = 0
   
    """ Class Abtraccion """          
    def __init__(self, gasolina):
        Auto.gasolina = gasolina
        """self.gasolina = gasolina"""
        print "Tenemos", gasolina, "litros"
 
    @classmethod
    def arrancar(cls,gasolina):
       
        if gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"
    
    @classmethod
    def moverse(cls,gasolina):
        
        if self.gasolina > 0:
           self.gasolina -= 1
           print "Quedan", gasolina, "litros"
        else:
            print "No hay gasolina para moverse..."
        
    
