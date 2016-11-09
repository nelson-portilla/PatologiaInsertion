import os,sys
import progressBar as progress
import subprocess

#Clase para obtener la lista de los archivos vacios dentro del master_formateado
def crear():
	try:
		p = subprocess.Popen(['wc', '-l', '../listaconpesos/master_formateado.txt'], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
		result, err = p.communicate()
		total_lineas=int(result.strip().split()[0])
		number=0
		file=open('../listaconpesos/master_formateado.txt', 'r')
		out=open('../listaconpesos/master_vacios.txt', 'w')
		for linea in file:
			lista=linea.split()
			progress.printProgress(number, total_lineas, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
			if(int(lista[0])<1000):
				out.write(lista[1])
				out.write("\n")
			number+=1
		file.close()
		out.close()

	except Exception, e:
		print "Ha fallado",str(e)
		sys.exit(1)

if __name__ == '__main__':
	
	crear()