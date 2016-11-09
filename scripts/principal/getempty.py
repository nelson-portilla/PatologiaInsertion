import os,sys
import insertar
import glob
from time import time
global lista
lista=[]
#matriz=[[None] * 7 for i in range(2)]

#recibe ../../informes-patologia-html/r03/r03-058.txt.html
def listar(file):
	try:
		lista.append(file)
	except Exception, e:
		print "Ha fallado al listar los vacios",str(e)
		sys.exit(1)

def crearfolder(folder):
	try:
		folder=str(folder)[30:]
		# print "ESTE FOLDER",folder
		if not os.path.exists('../listas_de_vacios/'+folder):
			os.makedirs('../listas_de_vacios/'+folder)
	except OSError as exc: # Guard against race condition
		if exc.errno != errno.EEXIST:
			raise
	except Exception, e:
		raise

def escribirlista(folder):
	global lista
	try:
		outputtxt=open(folder+'/lista_vacios.txt', 'a')
		# outputtxt.write("Numero de archivos vacios: "+str(len(lista)))
		# outputtxt.write("\n")	
		for item in lista:
			outputtxt.write(item)
			outputtxt.write("\n")
		outputtxt.close()
		lista=[]
		# print "==> Escribiendo lista vacios : ",folder+" ..OK"
		
	except Exception, e:
		print "Ha fallado al listar los vacios",str(e)
		sys.exit(1)

if __name__ == '__main__':
	None