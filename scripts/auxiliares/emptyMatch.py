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
	# salida_system = os.popen('echo | grep "'+nombre+'" ../listaconpesos/listadisco1.txt').read()
	salida_system = os.popen('echo | grep "'+nombre+'" ../listaconpesos/liliana.csv').read()
	if salida_system!="":
		# coincidencias=salida_system
		# out=open('../listas_de_vacios/SI_estan_en_disco1.txt', 'a')
		out=open('../listas_de_vacios/SI_estan_en_liliana.txt', 'a')
		out.write(salida_system)
		out.write("\n")
		# out.close()		
		flag=True
	else:
		flag=False
	return flag

def buscarenerlinda(nombre):
	salida_system = os.popen('echo | grep "'+ nombre +'" ../listaconpesos/erlinda.csv').read()
	# salida_system = os.popen('echo | grep "'+ nombre +'" ../listaconpesos/listadisco2.txt').read()
	if salida_system!="":
		# coincidencias=salida_system.split()
		# oute=open('../listas_de_vacios/SI_estan_disco2.txt', 'a')
		oute=open('../listas_de_vacios/SI_estan_erlinda.txt', 'a')
		oute.write(salida_system)
		oute.write("\n")
		oute.close()
	else:
		outp=open('../listas_de_vacios/Perdidos_no_estan_liliana_erlinda.txt', 'a')
		# outp=open('../listas_de_vacios/PerdidosDefinitivos.txt', 'a')
		outp.write(nombre)
		outp.write("\n")
		outp.close()

def buscarenmasterhtml(nombre):
	try:		
		salida_system = os.popen('echo | grep -c "'+ nombre +'" ../listaconpesos/master_formateado_html.txt').read()
		coincidencias=int(salida_system)
		out=open('../listas_de_vacios/SI_estan_en_masterHTML.txt_NO_VACIOS', 'a')
		if coincidencias!=0:
			out.write(nombre)
			out.write("\n")
		else:
			outp=open('../listas_de_vacios/Estan_en_Master_No_HTML.txt_NO_VACIOS', 'a')
			outp.write(nombre)
			outp.write("\n")
			outp.close()
		out.close()
	except Exception, e:
		print "Ha fallado",str(e),nombre
		sys.exit(1)

def buscarenvaciosmaster(nombre):
	try:		
		salida_system = os.popen('echo | grep -c "'+ nombre +'" ../listaconpesos/vacios_en_master.txt').read()
		coincidencias=int(salida_system)
		out=open('../listas_de_vacios/Estan_en_Master_Y_VACIOS.txt', 'a')
		if coincidencias!=0:
			out.write(nombre)
			out.write("\n")
		else:
			outp=open('../listas_de_vacios/Estan_en_Master_Y_No_VACIOS.txt', 'a')
			outp.write(nombre)
			outp.write("\n")
			outp.close()
		out.close()
	except Exception, e:
		print "Ha fallado",str(e),nombre
		sys.exit(1)



if __name__ == '__main__':
	p = subprocess.Popen(['wc', '-l', '../listas_de_vacios/NO_estan_en_master.txt'], stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE)
	result, err = p.communicate()
	total_lineas=int(result.strip().split()[0])
	number=0	
	lista_vacios=open('../listas_de_vacios/NO_estan_en_master.txt', 'r')
	for linea in lista_vacios:
		# nombre=str(linea)
		# buscarenliliana(linea.strip())
		if buscarenliliana(linea.strip()):
			None
		else:
			buscarenerlinda(linea.strip())
		progress.printProgress(number, total_lineas-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
		number+=1

	# buscar_en_liliana("m03-6688.txt")
