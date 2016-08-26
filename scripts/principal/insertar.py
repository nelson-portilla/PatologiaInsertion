# -*- coding: utf-8 -*-
import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
import extraccion as extraer
import getempty as getempty
import progressBar as progress
global matriz 
import glob
from time import time
matriz=[[None] * 7 for i in range(2)]

##METODO QUE CARGA EL ARCHIVO.SQL QUE CONTIENE EL COPY EL CUAL INSERTA DATOS A UNA TABLA DESDE UN SCV
def insertar():
	try:
		# print "Insertando datos desde csv..."
		csv=os.popen("echo | psql -U postgres -h localhost -d patologiaHUV -f insertarFROMcsv.sql").read()
		if(csv[:4]=="COPY"):
			None
			# print "Insercion exitosa", csv
		else:
			raise NameError('NoExito')
	except NameError:
		print "Ha fallado la insercion, error de los datos: posible llave duplicada o tipo de datos"
		sys.exit(1)
	except Exception, e:
		print "Ha fallado la insercion: error general",str(e)
		sys.exit(1)


##METODO QUE INICIALIZA LA MATRIZ CON None, EL TAMANO DEPENDE DEL NUMERO DE ARCHIVOS EN LA CARPETA
def crearMatriz(numArchivos):
	global matriz
	matriz=[[None] * 7 for i in range(numArchivos+1)]
	matriz[0][0]="numeroregistro"
	matriz[0][1]="historiaclinica"
	matriz[0][2]="cedula"
	matriz[0][3]="descmacro"
	matriz[0][4]="descmicro"
	matriz[0][5]="diagnostico"
	matriz[0][6]="html"
	# print "==> Creando Matriz ..OK"
	

##METODO QUE CUENTA EL NUMERO DE ARCHIVOS EN UN DIRECTORIO
def contarArchivos(ruta):
	count=0
	count=len([name for name in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, name))])
	# print "==> Contando Archivos ..OK", count
	return count

##METODO PARA LLENAR LA MATRIZ CON LOS DATOS ALMACENADOS EN EXTRACCION
## i: ES EL NUMERO DE ARCHIVO QUE SE VA A INSERTAR
def crearcsv(i, folder):
	matriz[i][0]=extraer.getNumeroRegistro()
	matriz[i][1]=extraer.getHistoriaClinica()
	matriz[i][2]=""#ESPACIO PARA LA CEDULA
	matriz[i][3]=extraer.getMacro()
	matriz[i][4]=extraer.getMicro()
	matriz[i][5]=extraer.getDiagnostico()
	matriz[i][6]=extraer.getHTML()
	
	##BANDERA PARA SABER SI LOS ARCHIVOS SON VACIOS DEPENDIENDO SI SON M,R O C
	flag=False
	#Para los folders c00,c01. No se revisa macro, micro
	#PENDIENTE: matriz[i][1]=="" para cedula
	if folder[0]=="m":
		#SI hc o macro,micro,diagnostico estan vacios:
		if (matriz[i][3]=="" or matriz[i][4]=="" or matriz[i][5]==""):
			flag= True
		else:
			flag= False

	#Para los r00 tienen macro, micro y algunos citologia.
	elif folder[0]=="r":
		if (matriz[i][3]=="" or matriz[i][4]=="" or matriz[i][5]==""):
			if ("CITOLOGIA" in matriz[i][6]):
				flag=False
			else:
				flag=True
		else:
			flag= False

	elif folder[0]=="c":		
		if ("CITOLOGIA" in matriz[i][6]):
			flag=False
		else:
			flag=True
	return flag


##METODO PARA ESCRIBIR LA MATRIZ EN UN ARCHIVO SCV
def escribirCSV():
	# print "MATRIZ: ",len (matriz)
	reg=open("registro.csv", 'w')

	for idx, linea in enumerate(matriz):
		if idx==len(matriz)-1:			
			reg.write("|".join(linea))
		else:			
			reg.write("|".join(linea))
			reg.write("\n")

	reg.close()
	# print "==> Creando Archivo CSV ..OK"


##METODO PARA EL PROCESO CONSECUTIVO DE EXTRACCION
def extraerDatos(datos, ruta, folder):
	#Se crea el Objeto de la clase	
	objHTML = extraer.LecturaHTML()
	#Se Lee el archivo
	textoHTML= extraer.leerArchivo(datos)
	#Se envia el html para obtener solo los datos
	objHTML.feed(textoHTML)
	#Con la lista creada se arma un Json
	extraer.ArmarJson(ruta)
	#Se Convierte de HTML A TXT
	extraer.escribirArchivo(folder)
	
	

##METODO PARA CREAR EL ARCHIVO SQL QUE CARGA EL CSV A LA BASE DE DATOS
def crearSQL():
	ruta=os.path.abspath('registro.csv')
	sql=open('insertarFROMcsv.sql', 'w')
	sql.write ("COPY muestra_html FROM '"+ruta+"' DELIMITER '|' CSV HEADER;")
	# print "==> Creando SQL-File-COPY ..OK"
	

##METODO QUE RETORNA TRUE SI EL FOLDER EXISTE
def existefolder(folder, subfolder):
	#RECIBE '../../informes-patologia-html/r96' -> cortar -> final -> c02
	# folder=str(folder)[30:]	
	return os.path.exists(folder+subfolder)


##CLASE PRINCIPAL
if __name__ == '__main__':

	folder_principal='../../informes-patologia-html/*'	
	##SE RECIBE LA RUTA DEL folder principal
	folder_principal=str(sys.argv[1])
	##SE RECIBE LA RUTA DEL folder para guardar los txt
	folder_txt=sys.argv[2]

	##SE CREA UNA LISTA CON LOS SUBFOLDERS: M16, C08, ETC
	subfolders_name=str(os.popen("echo | ls "+folder_principal).read()).split()

	tiempo_inicial = time()
	number=0

	##Se crea una lista con los subfolder pero con la ruta completa
	subfolders=glob.glob(folder_principal+'/*')   
	
	##subfolders son: c00, c01, r05, m16, etc
	for subfolder in subfolders_name:
		#IGNORAR FOLDER OTROS:				
		if (subfolder!="otros") and not existefolder(folder_txt, subfolder):
			path = folder_principal+subfolder+'/*.html'		
			files=os.popen("echo | ls "+folder_principal+subfolder+"/*.html").read().split()					
			
			files_glob=glob.glob(path)
			files_list=os.listdir(folder_principal+"/"+subfolder)
			# totalRegistros=contarArchivos("../informes") **
			totalRegistros=len(files)			
			crearMatriz(totalRegistros)
			# progress.printProgress(number, len(subfolders_name)-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
			i=1
			print files_list			
			for file in files_list:
				# print "\n==> Enviando archivo: ", file+"..."+str(i)
				completa=os.path.join(folder_principal,subfolder,file)
				print completa
				# filedata=open(file, 'r').read()
				# print files
				# extraerDatos(filedata, file, subfolder)
				# flag=crearcsv(i, subfolder)
			# 	if flag:
			# 		getempty.listar(file[34:])
			# 	extraer.inicializar()		
			# 	i+=1
			# 	# print "Archivo Numero: ",i
			# # getempty.crearfolder(folder)
			# getempty.escribirlista(folder)
			# escribirCSV()	
			# crearSQL()
			# insertar()
			# number+=1

	tiempo_final = time()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print '\n- - El tiempo de ejecucion en segundos fue: - - > ',str(tiempo_ejecucion)+"seg" #En segundos
	
	
	
