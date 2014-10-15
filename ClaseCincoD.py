def logError(msg):
   err = open("archivo.txt","w")
   err.write(msg)
   err.close()