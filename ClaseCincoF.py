def leer(archivo):
	esc = open("archivo.txt","a")
	lee = open("archivo.txt","r")
	for linea in inp.readlines():
	   esc.write(linea)
	   print "1 archivo copiado..."
	esc.close()
	lee.close()