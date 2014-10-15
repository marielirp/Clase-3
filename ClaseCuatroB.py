from ClaseCuatroA import logger
@logger
def sigma(*args):
	return sum([i for i in args])


def logger(fn):
	def wrapper(*args):
		for i, arg in enumerate(args):
			print "argu:%d:%d" % (i , arg)
		return fn(*args)
	return wrapper





