# -*- coding: utf-8 -*-
import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs
global informe, lista, jsonDatos, switch, dataMacro, dataMicro, dataDiag, textoPlano
from HTMLParser import HTMLParser
informe=textoPlano=""
lista=[]
switch=0
dataDiag=dataMicro=dataMacro=""
jsonDatos= {'NumeroRegistro':"",
			'HistoriaClinica': "",
			'DescMacro':"",
			'DescMicro':"",
			'DescDiagnostico':"",
			'Texto':""
			}


def inicializar():
	global informe, lista, jsonDatos, switch, dataMacro, dataMicro, dataDiag, textoPlano
	# print "Limpiando..." 
	informe=textoPlano=""
	lista=[]
	switch=0
	dataDiag=dataMicro=dataMacro=""
	jsonDatos= {'NumeroRegistro':"",
			'HistoriaClinica': "",
			'DescMacro':"",
			'DescMicro':"",
			'DescDiagnostico':"",
			'Texto':""
			}

#Clase para leer el html, se obtienen solo el Data, se limpia y se arma la lista.
class LecturaHTML(HTMLParser):

        def handle_data(self, data):        	
        	global switch, dataMacro, dataMicro, dataDiag, textoPlano        	
			#Se limpia el texto, se eliminan saltos de linea y espacios.
        	data=data.replace('\r\n',"").replace("\t", "").replace("\n", " ").replace("||", " ").replace("|", " ").strip()
        	
        	if data!="":
        		textoPlano+=data+" "

	        	if data=='DESCRIPCION MACROSCOPICA':
	        		switch=1	        		

	        	if data=='DESCRIPCION MICROSCOPICA':
	        		switch=2
	        		
	        	if data=='DIAGNOSTICO:':
	        		switch=3        		

	        	if switch==0:
	        		lista.append(data)
	        		
				
			if switch==1:				
				dataMacro+=" "+data

	        	if switch==2:
	        		dataMicro+=" "+data

	        	if switch==3:
	        		#CODIGO PARA PARADA, Analizar TM33464 M7387
	        		if any(char.isdigit() for char in data[:2]):
	        			switch=4
	        		else:
	        			dataDiag+=" "+data
	def __del__(self):
		None
		# print "ok...";
        
def ArmarJson(ruta):
	global lista, jsonDatos, dataMacro, dataMicro, dataDiag,switch,textoPlano
	try:
		
		if ruta.endswith(".html"):

			#RECIBE '../informes-patologia-htlm/c02/c00.txt.html' -> cortar -> final -> c02
			# numreg=ruta[34:]
			numreg=ruta
			# print "NUMERO REGISTRO: ",numreg
			jsonDatos['NumeroRegistro']=numreg.replace(".txt.html", "").lower()
			#VALIDAR SI EXISTE HOSTORIA CLINCICA
			if len(lista)>0:
				if lista[1].isdigit():
					jsonDatos['HistoriaClinica']=lista[1]
				else:
					jsonDatos['HistoriaClinica']=''
			else:
				jsonDatos['HistoriaClinica']=''


			#Se Agregan al diccionario Eliminando el titulo "Desc Macro...", etc.
			jsonDatos['DescMacro']=dataMacro[25:]
			jsonDatos['DescMicro']=dataMicro[25:]
			jsonDatos['DescDiagnostico']=dataDiag[13:]
			jsonDatos['Texto']=textoPlano
			
			## lista=[]
			## switch=0
			## dataDiag=dataMicro=dataMacro=textoPlano=""
			# print "==> Datos cargados ..OK"
			# print "NR..>",jsonDatos['NumeroRegistro']
			# print "HC..>",jsonDatos['HistoriaClinica']
			# print "MACRO..>",jsonDatos['DescMacro']
			# print "MiCRO..>",jsonDatos['DescMicro']
			# print "Diag..>",jsonDatos['DescDiagnostico']

	except IndexError, e:
		None
		# print "ENTRO en IndexError", lista, jsonDatos['NumeroRegistro']
			
#Se obtiene el numero de registro
def getNumeroRegistro():
	return jsonDatos['NumeroRegistro']

#Se Obtiene la descripcion macroscopica
def getMacro():
	return jsonDatos['DescMacro']

#Se Obtiene la descripcion microscopica
def getMicro():
	return jsonDatos['DescMicro']

#Se Obtiene la descripcion diagnostico
def getDiagnostico():
	return jsonDatos['DescDiagnostico']

#Se Obtiene la Historia Clinica
def getHistoriaClinica():
	return jsonDatos['HistoriaClinica']

#Se obtiene el id del paciente de acuerdo a la historia clinica
def getId_Paciente():
	hc=getHistoriaClinica()	
	csv=os.popen("echo | psql -U postgres -h localhost -d patologiaHUV -c 'select p.id from paciente as p where hc="+hc+";'").read().split()
	return csv[2]

#se obtiene el id de la tabla Muestra
def getId_Muestra():
	idpac=getId_Paciente()
	csv=os.popen("echo | psql -U postgres -h localhost -d patologiaHUV -c 'select id from muestra  where idpaciente="+idpac+";'").read().split()
	return csv[2]

def getHTML():
	return jsonDatos['Texto']

#Se abre el archivo y se almacena el contenido
def leerArchivo(ruta):
	global informe
	informe=ruta
	# print "==> Leyendo archivo: ..OK"
	return informe

def escribirArchivo(folder, folder_txt):
	global textoPlano, jsonDatos
	#RECIBE '../informesEnTXT/c02' -> cortar -> final -> c02
	# print "ESTE FOLDER",folder
	if not os.path.exists(folder_txt+"/"+folder):
		try:
			os.makedirs(folder_txt+"/"+folder)
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	nr=jsonDatos['NumeroRegistro']+".txt"	
	outputtxt=open(folder_txt+"/"+folder+'/'+nr, 'w')
	outputtxt.write(textoPlano)
	outputtxt.write("\n")
	outputtxt.close()
	# print "==> Convirtiendo Archivo : ",nr+" ..OK"

if __name__ == '__main__':
	None
