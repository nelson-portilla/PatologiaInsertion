import os,sys
import progressBar as progress
import subprocess

#Clase de emparejamiento entre master y listas_de_vacios para obtener lista de archivos faltantes.
def buscar(nombre):
	try:		
		salida_system = os.popen('echo | grep -c "'+ nombre +'" ../listaconpesos/master_formateado.txt').read()
		coincidencias=int(salida_system)
		out=open('../listas_de_vacios/estan_en_master.txt', 'a')
		if coincidencias!=0:
			out.write(nombre)
			out.write("\n")
		out.close()

	except Exception, e:
		print "Ha fallado",str(e),nombre
		sys.exit(1)

if __name__ == '__main__':
	p = subprocess.Popen(['wc', '-l', '../listas_de_vacios/lista_vacios.txt'], stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE)
	result, err = p.communicate()
	total_lineas=int(result.strip().split()[0])
	number=0	

	lista_vacios=open('../listas_de_vacios/lista_vacios.txt', 'r')
	for linea in lista_vacios:
		buscar(linea[:-6])		
		progress.printProgress(number, total_lineas, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
		number+=1

	# buscar("m16-739.txt.html")