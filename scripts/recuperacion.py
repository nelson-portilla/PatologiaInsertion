import os,sys
import progressBar as progress
import subprocess

#Clase de emparejamiento entre master y listas_de_vacios para obtener lista de archivos faltantes.
def copiar(nombre, origen, destino, folder):
	try:		
		
		##PARA LA BUSQUEDA EN MASTER PRIMERO ENCONTRAR RUTA.
		nuevaruta=os.popen("echo | find ../../00HUV_patologias/master/informes-patologia/informes-patologia-unificado -iname "+nombre).read()
		respuesta=os.system("cp "+nuevaruta.strip()+" "+destino)
		
		##PARA LOS OTROS FOLDERS COMENTAR LINEAS ANTERIORES Y DESCOMENTAR LA DE ABAJO
		# respuesta=os.system("cp "+origen+"/"+nombre+" "+destino)
		# if respuesta!=0:
		# 	out=open(destino+"/000_NO_copiados_"+folder+".txt", 'a')
		# 	out.write(nombre)
		# 	out.write("\n")
		# 	out.close()

	except Exception, e:
		print "Ha fallado",str(e),nombre
		sys.exit(1)


if __name__ == '__main__':

	# lista='../listas_de_vacios/SI_estan_en_liliana.txt'
	# rutaorigen='../../00HUV_patologias/patologias_miriam'	
	# rutadestino='../../recuperacion_info/liliana'
	# rutadestino='../../recuperacion_huecos/liliana'

	##RECUPERACION_HUECOS Disco 1
	# lista='../lista_de_huecos/huecos_estan_en_disco1.txt'
	# rutaorigen='../../00HUV_patologias/Disco1/PatologiHUV/PATOLOGI'
	# rutadestino='../../recuperacion_huecos/disco1'
	# folder='disco1'
	
	##RERACION_HUECOS Disco 2 - PATOLOGI
	# lista='../lista_de_huecos/huecos_estan_en_disco2.txt'
	# rutaorigen='../../00HUV_patologias/Disco2/PATOLOGI'
	# rutadestino='../../recuperacion_huecos/disco2'
	# folder='disco2'

	##RERACION_HUECOS Disco 2 - patolog
	# lista='../lista_de_huecos/huecos_estan_en_disco2.txt'
	# rutaorigen='../../00HUV_patologias/Disco2/patolog'
	# rutadestino='../../recuperacion_huecos/disco2'
	# folder='disco2'

	##RERACION_HUECOS master_html
	# lista='../lista_de_huecos/huecos_estan_en_master_pero_html.txt'
	# rutaorigen='../../00HUV_patologias/master/informes-patologia/informes-patologia-html'
	# rutadestino='../../recuperacion_huecos/master_html'
	# folder='master_html'

	##RERACION_HUECOS master_WP
	lista='../lista_de_huecos/huecos_estan_en_master_pero_wp.txt'
	rutaorigen='../../00HUV_patologias/master/informes-patologia/informes-patologia-html'
	rutadestino='../../recuperacion_huecos/master_wp'
	folder='master_wp'




	p = subprocess.Popen(['wc', '-l', lista], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	result, err = p.communicate()
	total_lineas=int(result.strip().split()[0])
	number=0

	lista_master=open(lista, 'r')

	for linea in lista_master:
		nombre=str(linea.strip())		
		copiar(nombre, rutaorigen, rutadestino, folder)
		progress.printProgress(number, total_lineas-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
		number+=1
	print "\n"
