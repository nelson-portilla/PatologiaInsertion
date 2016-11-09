#!/bin/bash
# -*- ENCODING: UTF-8 -*-

#UBICACION DONDE QUEDARAN EL LISTADO DE ARCHIVOS A ORGANIZAR:
rutalistado="/home/registro/Vídeos/prueba_cargar/scripts/texto_plano/lista_archivo.txt"


##PROCESO DE CREACION DE LA LISTA
##carpeta: 	VARIABLE QUE LEE LA PRIMERA ENTRADA DEL USUARIO, ES DECIR
##			LA CARPETA DONDE  ESTAN LOS ARCHIVOS A ORGANIZAR.
carpeta=$1
echo "Creando lista de archivos de la carpeta: $carpeta \n"
ls $carpeta > $rutalistado

################ 	PROCESO DE EJECUCION DEL SCRIPT PYTHON          #############################

#Definir las rutas antes de correr el script:

#RUTA DEL ARCHIVO PYTHON, CAMBIAR RUTA SI ESTA EN UNA UBICACION DIFERENTE
pythonfile="/home/registro/Vídeos/prueba_cargar/scripts/auxiliares/organizar.py"

#RUTA de la lista creada anteriormente, MODIFICAR SI ES DIFERENTE
rutalista=$rutalistado

#FOLDER DONDE ESTAN LOS ARCHIVOS
rutafolder='/home/registro/Vídeos/prueba_cargar/archivos'

#FOLDER DONDE QUEDARAN LOS ARCHIVOS COPIADOS
rutadestino='/home/registro/Vídeos/prueba_cargar/organizados'

python $pythonfile $rutalista $rutafolder $rutadestino

exit
