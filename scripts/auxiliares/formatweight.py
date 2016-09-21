import os,sys

##FUNCION PARA FORMATEAR UNA ARCHIVO CON LISTA DE ARCHIVOS
##	A UNA LISTA DE TUPLAS PESO Y NOMBRE.
###	Las Posiciones de los arreglos cambia dependiendo de
###	la lista de entrada.
def formatear():
	try:
		rutain="/home/registro/Documentos/Repositorios/PatologiaInsertion/listaconpesos/listazmaster.txt"
		rutaout="/home/registro/Documentos/Repositorios/PatologiaInsertion/listaconpesos/listazmaster_formateado.txt"
		inputtxt=open(rutain, 'r')
		outputtxt=open(rutaout, 'w')

		for linea in inputtxt:
			linea=linea.rstrip()			
			#if linea[:5]=="-rw-r":
			if True:
				print "formating..."								
				lista=linea.split()			
				peso=lista[3]				
				nombre = lista [7]				
				outputtxt.write(peso)
				outputtxt.write(" ")
				outputtxt.write(nombre)
				outputtxt.write("\n")
		inputtxt.close()
		outputtxt.close()
	except Exception, e:
		print "Ha fallado",str(e)
		sys.exit(1)

if __name__ == '__main__':
	formatear()