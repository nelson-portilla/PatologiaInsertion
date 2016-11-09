#!/bin/bash
# -*- ENCODING: UTF-8 -*-

#CAMBIAR RUTAS DE LOS ARCHIVOS

pythonFile='/home/registro/Vídeos/prueba_cargar/scripts/principal/insertar.py'

folderPatologias='/home/registro/Vídeos/prueba_cargar/organizados'
#folderPatologias='/home/registro/Documentos/ultimo/informes-patologia-html'
#folderPatologias='/home/registro/Documentos/Repositorios/Patologias_Sep_2016/informes_patologia_html'
#folderPatologias='/home/registro/Documentos/Repositorios/Patologias_Sep_2016/especial_m06'
#folderPatologias='/home/registro/Vídeos/prueba_cargar/aa'

folderTXTConvertidos='/home/registro/Vídeos/prueba_cargar/archivos_txt'

folderPrincipalScripts='/home/registro/Vídeos/prueba_cargar'

echo 'Ejecuntado INSERTAR \n'
python $pythonFile $folderPatologias $folderTXTConvertidos $folderPrincipalScripts

exit
