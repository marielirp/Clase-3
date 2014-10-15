def logError(msg):
   err = open("archivo.txt","a")
   err.write(msg)
   for linea in err:
		 print linea
   err.close()