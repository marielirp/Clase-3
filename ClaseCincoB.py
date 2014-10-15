def abrir(archivo):
	f = open(archivo)
	for linea in f:
		 print linea
	f.close()