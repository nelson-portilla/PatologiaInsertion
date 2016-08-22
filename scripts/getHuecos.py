import os,sys
import progressBar as progress
import subprocess

#Clase de emparejamiento entre master y listas_de_vacios para obtener lista de archivos faltantes.
def buscarenlista(nombre, ruta, newfile):
	try:		
		salida_system = os.popen('echo | grep -c "'+ nombre +'" '+ruta).read()
		coincidencias=int(salida_system)
		out=open(newfile, 'a')
		if coincidencias!=0:
			out.write(nombre)
			out.write("\n")
		out.close()
	except Exception, e:
		print "Ha fallado",str(e),nombre
		sys.exit(1)


if __name__ == '__main__':

	# rutaorigen='../listaconpesos/master_formateado.txt'
	# rutadestino='../lista_de_huecos/lista_en_base_datos.txt'
	# archivo_nuevo='../lista_de_huecos/huecos_estan_en_master.txt'
	
	# rutaorigen='../listaconpesos/liliana.csv'
	# rutadestino='../listaconpesos/master_formateado.txt'
	# archivo_nuevo='../lista_de_huecos/liliana_no_estan_en_master.txt'

	# rutaorigen='../listaconpesos/erlinda.csv'
	# rutadestino='../listaconpesos/master_formateado.txt'
	# archivo_nuevo='../lista_de_huecos/erlinda_no_estan_en_master.txt'

	# rutaorigen='../listaconpesos/listadisco2.txt'
	# rutadestino='../listaconpesos/master_formateado.txt'
	# archivo_nuevo='../lista_de_huecos/disco2_no_estan_en_master.txt'

	# rutaorigen='../lista_de_huecos/huecos_estan_en_master.txt'
	# rutadestino='../listaconpesos/master_formateado_html.txt'
	# archivo_nuevo='../lista_de_huecos/huecos_estan_en_master_pero_wp.txt'

	# rutaorigen='../listaconpesos/master_formateado.txt'
	# rutadestino='../listaconpesos/master_formateado_html.txt'
	# archivo_nuevo='../lista_de_huecos/master_no_estan_html.txt'

	rutaorigen='../lista_de_huecos/huecos_estan_en_master.txt'
	rutadestino='../listaconpesos/master_formateado_html.txt'
	archivo_nuevo='../lista_de_huecos/huecos_estan_en_master_pero_html.txt'

	p = subprocess.Popen(['wc', '-l', rutaorigen], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	result, err = p.communicate()
	total_lineas=int(result.strip().split()[0])
	number=0

	lista_master=open(rutaorigen, 'r')

	for linea in lista_master:
		##PARA LILIANA
		# nombre=str(linea.split(";")[3].strip().lower())		
		##PARA ERLINDA
		# nombre=str(linea.split(";")[2].split()[1].strip().lower())		
		
		##PARA DISCO1
		# if linea.strip()[-1:]!="!":
		# 	nombre=str(linea.strip().lower())		
		

		# nombre=str(linea.split()[1].strip())		
		nombre=str(linea.strip())		
		buscarenlista(nombre, rutadestino, archivo_nuevo)
		progress.printProgress(number, total_lineas-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
		number+=1


	print "\n"
