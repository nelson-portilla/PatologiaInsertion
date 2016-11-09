import os,sys
import progressBar as progress
import subprocess

#METODO QUE A PARTIR DE UNA LISTA, UBICACION DE LOS ARCHIVOS Y UBICACION DESTINO
##ORGANIZA EN SUBCARPETAS C00,C01,M14,M15,M16,ETC
def organizar(archivo, folder, destino):
	try:
		#BLOQUE PARA LA LINEA DE PROGRESO
		p = subprocess.Popen(['wc', '-l', archivo], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		result, err = p.communicate()
		total_lineas=int(result.strip().split()[0])
		number=0

		file=open(archivo, 'r')
		for linea in file:
			#DE LA LINEA OBTIENE LOS TRES PRIMEROS CARACTERES: M16-1578 -> M16
			subfolder=linea[:3].lower()
				
			#LINEA DE PROGRESO SE LLAMA EN CADA CICLO
			progress.printProgress(number, total_lineas-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
			number+=1

			#SE UNE FODLER DESTINO CON SUBFOLDER. EJEMPLO: PATOLOGIAS/M15
			rutaunion=destino+"/"+subfolder
			#CONDICION Si NO EXISTE FOLDER EJ: PATOLOG/M16 ENTONCES LO CREA
			if not existefolder(rutaunion):
				crearfolder(rutaunion)
			
			#VA A COPIAR EJ: (linea)m16-002.txt.html ubicado en (folder)/home/fox copiar hacia (destino)/home/fox/organizado
			copiar(linea, folder, rutaunion)
		file.close()
		print ("\n")
	except Exception, e:
		print "Ha fallado en organizar",str(e)
		sys.exit(1)
		


#METODO QUE RETORNA TRUE SI EXISTE EL FOLDER
def existefolder(folder):
	return os.path.exists(folder)

#METODO QUE CREA EL FOLDER
def crearfolder(folder):
	try:
		os.makedirs(folder)
	except OSError as exc: # Guard against race condition
		if exc.errno != errno.EEXIST:
			print "Ha fallado en la creacion del folder"
			raise

#METODO PARA COPIAR UN NOMBRE_ARCHIVO EN UNA RUTA_ORIGEN HACIA UNA RUTA DESTINO
def copiar(nombre, origen, destino):
	try:
		#SE ARMA LA RUTA EJEMPLO: /home/patologias , m16-001 -> /home/patologias/m16-001.txt.html
		rutaunion=origen+"/"+nombre			
		respuesta=os.system("cp "+rutaunion.strip()+" "+destino)				
		if respuesta!=0:
			out=open(destino+"/000_NO_copiados.txt", 'a')
			out.write(nombre)
			out.write("\n")
			out.close()
	except Exception, e:
		print "Ha fallado al copiar archivos",str(e)
		sys.exit(1)


if __name__ == '__main__':	
	#SE RECIBE LA RUTA DEL ARCHIVO PLANO CON EL NOMBRE DE LOS ARCHIVOS
	archivo=sys.argv[1]
	#SE RECIBE LA RUTA DEL FOLDER DONDE ESTAN LOS ARCHIVOS
	folder=sys.argv[2]
	#SE RECIBE LA RUTA DEL FOLDER DONDE SE VAN A ORGANIZAR LOS ARCHIVOS
	destino=sys.argv[3]

	#LAS RUTAS SE ENVIAN A ORGANIZAR
	organizar(archivo, folder, destino)
	
