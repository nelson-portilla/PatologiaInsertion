import os,sys
#from extraccion as t import *
import extraccion as extraer
global matriz
matriz=[[None] * 7 for i in range(2)]

def insertar():
	try:
		print "Insertando datos desde csv"
		csv=os.popen("echo | psql -U postgres -h localhost -d patologiaHUV -f insertarFROMcsv.sql").read()
		if(csv[:4]=="COPY"):
			print "Insercion exitosa", csv
		else:
			raise NameError('NoExito')
	except NameError:
		print "Ha fallado la insercion, error de los datos: posible llave duplicada o tipo de datos"
	except Exception, e:
		print "Ha fallado la insercion: error general",str(e)

	

def crearcsv():
	global matriz
	matriz[0][0]="id"
	matriz[0][1]="idpaciente"
	matriz[0][2]="numeroregistro"
	matriz[0][3]="descmacro"
	matriz[0][4]="descmicro"
	matriz[0][5]="diagnostico"
	matriz[0][6]="html"

	for i in range(1,2):
		matriz[i][0]=extraer.getId_Muestra()
		matriz[i][1]=extraer.getId_Paciente()
		matriz[i][2]=extraer.getNumeroRegistro()
		matriz[i][3]=extraer.getMacro()
		matriz[i][4]=extraer.getMicro()
		matriz[i][5]=extraer.getDiagnostico()
		matriz[i][6]="HTML"#extraer.getHTML()
	
	
	reg=open("registro.csv", 'w')
	for idx, linea in enumerate(matriz):
		if idx==len(matriz)-1:			
			reg.write("|".join(linea))
		else:
			reg.write("|".join(linea))
			reg.write("\n")

	reg.close()
	# print matriz

def extraerDatos(ruta):
	#Se crea el Objeto de la clase	
	objHTML = extraer.LecturaHTML()
	#Se Lee el archivo
	textoHTML= extraer.leerArchivo(ruta)
	#Se envia el html para obtener solo los datos
	objHTML.feed(textoHTML)
	#Con la lista creada se arma un Json
	extraer.ArmarJson()
	#Se prueba la informacio
	# print extraer.getHistoriaClinica()

def crearSQL():
	print "Creando Archivo SQL COPY..."
	ruta=os.path.abspath('registro.csv')
	sql=open('insertarFROMcsv.sql', 'w')
	sql.write ("COPY muestra_html FROM '"+ruta+"' DELIMITER '|' CSV HEADER;")
	

if __name__ == '__main__':
	extraerDatos("../informes/m10-0001.txt.html")
	crearcsv()
	crearSQL()
	insertar()
