import os,sys
#from extraccion as t import *
import extraccion as extraer
global matriz 
import glob
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
	except Exception, e:
		print "Ha fallado la insercion: error general",str(e)

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
	count=2
	count=len([name for name in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, name))])
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
	reg=open("registro.csv", 'w')

	for idx, linea in enumerate(matriz):
		if idx==len(matriz)-1:			
			reg.write("|".join(linea))
		else:
			reg.write("|".join(linea))
			reg.write("\n")

	reg.close()
	print "==> Creando Archivo CSV ..OK"

def extraerDatos(ruta):
	#Se crea el Objeto de la clase	
	objHTML = extraer.LecturaHTML()
	#Se Lee el archivo
	textoHTML= extraer.leerArchivo(ruta)
	#Se envia el html para obtener solo los datos
	objHTML.feed(textoHTML)
	#Con la lista creada se arma un Json
	extraer.ArmarJson()
	#Se Convierte de HTML A TXT
	extraer.escribirArchivo()
	objHTML.inicializar()
	

def crearSQL():
	ruta=os.path.abspath('registro.csv')
	sql=open('insertarFROMcsv.sql', 'w')
	sql.write ("COPY muestra_html FROM '"+ruta+"' DELIMITER '|' CSV HEADER;")
	print "==> Creando SQL-File-COPY ..OK"
	

if __name__ == '__main__':
	i=1   
	totalRegistros=contarArchivos("../informes")
	crearMatriz(totalRegistros)
	path = '../informes/*.html'   
	files=glob.glob(path)   
	for file in files:
		print "\n==> Enviando archivo: ", file+"..."+str(i)
		filedata=open(file, 'r').read()
		extraerDatos(filedata)
		crearcsv(i)		
		i+=1
	escribirCSV()	
	crearSQL()
	insertar()
	
	
	
