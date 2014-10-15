from __future__ import print_function

def leer_f(archivo):

	f = open(archivo)
	for linea in f:
		print(linea)

	f.close()

def wfile(archivo):
	f=open(archivo,'w')
	f.write("en lugar de la mancha...")
	f.close()

def rfile(archivo):
	f =open(archivo)
	print(f.readline())

def rfile(archivo):
	f =open(archivo)
	print(f.readlines())

def existe_archivo(archivo):
	if os.path.exist(archivo):
		print(u"si es un archivo valido")
	else:
		print("no soy capaz de encontrar el archivo")
	