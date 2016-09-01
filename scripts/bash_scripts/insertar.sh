#!/bin/bash
# -*- ENCODING: UTF-8 -*-

#CAMBIAR RUTAS DE LOS ARCHIVOS

pythonFile='/home/registro/Vídeos/prueba_cargar/scripts/principal/insertar.py'

folderPatologias='/home/registro/Vídeos/prueba_cargar/organizados'

folderTXTConvertidos='/home/registro/Vídeos/prueba_cargar/archivos_txt'

folderPrincipalScripts='/home/registro/Vídeos/prueba_cargar'

echo 'Ejecuntado INSERTAR \n'
python $pythonFile $folderPatologias $folderTXTConvertidos $folderPrincipalScripts

exit