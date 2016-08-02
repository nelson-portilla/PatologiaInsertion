import os,sys
#from extraccion as t import *
import extraccion as extraer
global matriz 
import glob
from time import time
matriz=[[None] * 6 for i in range(2)]

def insertar():
	try:
		print "Insertando datos desde csv..."
		csv=os.popen("echo | psql -U postgres -h localhost -d patologiaHUV -f insertarFROMcsv.sql").read()
		if(csv[:4]=="COPY"):
			print "Insercion exitosa", csv
		else:
			raise NameError('NoExito')
	except NameError:
		print "Ha fallado la insercion, error de los datos: posible llave duplicada o tipo de datos"
		sys.exit(1)
	except Exception, e:
		print "Ha fallado la insercion: error general",str(e)
		sys.exit(1)

def crearMatriz(numArchivos):
	global matriz
	matriz=[[None] * 6 for i in range(numArchivos+1)]
	matriz[0][0]="numeroregistro"
	matriz[0][1]="historiaclinica"
	matriz[0][2]="descmacro"
	matriz[0][3]="descmicro"
	matriz[0][4]="diagnostico"
	matriz[0][5]="html"
	print "==> Creando Matriz ..OK"
	
def contarArchivos(ruta):
	count=0
	count=len([name for name in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, name))])
	# count=([name for name in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, name))])
	# print count
	# for folder in count:
	# 	contents = os.listdir(os.path.join(ruta,folder)) # get list of contents
	# 	if len(contents) > 20:
	# 		print (folder,len(contents))
	print "==> Contando Archivos ..OK", count
	return count

def crearcsv(i):
	matriz[i][0]=extraer.getNumeroRegistro()
	matriz[i][1]=extraer.getHistoriaClinica()
	matriz[i][2]=extraer.getMacro()
	matriz[i][3]=extraer.getMicro()
	matriz[i][4]=extraer.getDiagnostico()
	matriz[i][5]=extraer.getHTML()

def escribirCSV():
	print "MATRIZ: ",len (matriz)
	reg=open("registro.csv", 'w')

	for idx, linea in enumerate(matriz):
		if idx==len(matriz)-1:			
			reg.write("|".join(linea))
		else:			
			reg.write("|".join(linea))
			reg.write("\n")

	reg.close()
	print "==> Creando Archivo CSV ..OK"

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
	
	

def crearSQL():
	ruta=os.path.abspath('registro.csv')
	sql=open('insertarFROMcsv.sql', 'w')
	sql.write ("COPY muestra_html FROM '"+ruta+"' DELIMITER '|' CSV HEADER;")
	print "==> Creando SQL-File-COPY ..OK"
	
def existefolder(folder):
	#RECIBE '../informesEnTXT/c02' -> cortar -> final -> c02
	folder=str(folder)[22:]
	return os.path.exists('../informesEnTXT/'+folder)


if __name__ == '__main__':
	
	# totalRegistros=contarArchivos("../../../informes-patologia") **
	# path = '../informes/*.html' **
	tiempo_inicial = time()
	folders=glob.glob('../informes-patologia/*')   
	print folders
	for folder in folders:
		#IGNORAR FOLDER OTROS:
		fotros=str(folder)[22:]
		if (fotros!="otros") and not existefolder(folder):
			path = folder+'/*.html'
			# path = '../Informes_Revisar/*.html'   **
			files=glob.glob(path)   
			# totalRegistros=contarArchivos("../informes") **
			totalRegistros=len(files)
			crearMatriz(totalRegistros)
			i=1
			for file in files:
				print "\n==> Enviando archivo: ", file+"..."+str(i)
				filedata=open(file, 'r').read()
				extraerDatos(filedata, file, folder)
				crearcsv(i)
				extraer.inicializar()		
				i+=1
				print "Archivo Numero: ",i
			escribirCSV()	
			crearSQL()
			insertar()
	tiempo_final = time()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print '- - El tiempo de ejecucion en segundos fue: - - > ',str(tiempo_ejecucion)+"seg" #En segundos
	
	
	
