import os,sys
import progressBar as progress
import subprocess

#Clase de emparejamiento entre master y listas_de_vacios para obtener lista de archivos faltantes.
def buscarenmaster(nombre):
	try:		
		salida_system = os.popen('echo | grep -c "'+ nombre +'" ../listaconpesos/master_formateado.txt').read()
		coincidencias=int(salida_system)
		out=open('../listas_de_vacios/SI_estan_en_master.txt', 'a')
		if coincidencias!=0:
			out.write(nombre)
			out.write("\n")
		out.close()

	except Exception, e:
		print "Ha fallado",str(e),nombre
		sys.exit(1)

def buscarenliliana (nombre) :
	salida_system = os.popen('echo | grep "'+nombre+'" ../listaconpesos/listadisco1.txt').read()
	if salida_system!="":
		# coincidencias=salida_system
		out=open('../listas_de_vacios/SI_estan_en_disco1.txt', 'a')
		out.write(salida_system)
		out.write("\n")
		# out.close()		
		flag=True
	else:
		flag=False
	return flag


def buscarenerlinda(nombre):
	salida_system = os.popen('echo | grep "'+ nombre +'" ../listaconpesos/listadisco2.txt').read()
	if salida_system!="":
		# coincidencias=salida_system.split()
		oute=open('../listas_de_vacios/SI_estan_disco2.txt', 'a')
		oute.write(salida_system)
		oute.write("\n")
		oute.close()
	else:
		outp=open('../listas_de_vacios/PerdidosDefinitivos.txt', 'a')
		outp.write(nombre)
		outp.write("\n")
		outp.close()
	



if __name__ == '__main__':
	p = subprocess.Popen(['wc', '-l', '../listas_de_vacios/Perdidos.txt'], stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE)
	result, err = p.communicate()
	total_lineas=int(result.strip().split()[0])
	number=0	
	lista_vacios=open('../listas_de_vacios/Perdidos.txt', 'r')
	for linea in lista_vacios:
		nombre=str(linea).upper().strip()
		print nombre
		if buscarenliliana(nombre):
			None
		else:
			buscarenerlinda(nombre)
		# progress.printProgress(number, total_lineas-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
		number+=1

	# buscar_en_liliana("m03-6688.txt")
