# -*- coding: utf-8 -*-
#By: Nelson Portilla
import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs
global informe, lista, jsonDatos;
from HTMLParser import HTMLParser
informe=""
lista=[]
jsonDatos={	'NumeroRegistro':"",
			'HistoriaClinica': "",
			'DescMacro':"",
			'DescMicro':"",
			'DescDiagnostico':""
			}

#Clase para leer el html, se obtienen solo el Data, se limpia y se arma la lista.
class LecturaHTML(HTMLParser):        
        def handle_data(self, data):        	
        	if((data.replace('\r\n',"")).replace("\t", "")!=""):
        		lista.append(data.strip())
        
def ArmarJson():
	global lista, jsonDatos
	jsonDatos['NumeroRegistro']=lista[0].replace(".txt", "")
	jsonDatos['HistoriaClinica']=lista[1]
	jsonDatos['DescMacro']=lista[7]
	jsonDatos['DescMicro']=lista[9]
	jsonDatos['DescDiagnostico']=lista[11]
	# print jsonDatos		
			
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
	return informe

#Se abre el archivo y se almacena el contenido
def leerArchivo(ruta):
	global informe
	informe=open(ruta, 'r').read()
	return informe


if __name__ == '__main__':
	None
