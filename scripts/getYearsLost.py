import os,sys
import progressBar as progress
import subprocess
global contador
contador=[0]*100
#Clase de emparejamiento entre master y listas_de_vacios para obtener lista de archivos faltantes.
def contar(anno):
	try:
		contador[anno]+=1
	except Exception, e:
		print "Ha fallado",str(e),anno
		sys.exit(1)

if __name__ == '__main__':
	global contador
	p = subprocess.Popen(['wc', '-l', '../listas_de_vacios/PerdidosDefinitivos.txt'], stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE)
	result, err = p.communicate()
	total_lineas=int(result.strip().split()[0])
	number=0	
	lista_vacios=open('../listas_de_vacios/PerdidosDefinitivos.txt', 'r')
	yearslost=open('../listas_de_vacios/yearsLostDefinitely.txt', 'w')
	for linea in lista_vacios:
		anno=int(linea[1:3])
		contar(anno)
		progress.printProgress(number, total_lineas-1, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
		number+=1
	listkey=[]
	listvalue=[]
	for num in contador:
		if num>0:
			yearslost.write(str(contador.index(num))+" ")			
			yearslost.write(str(num))
			yearslost.write("\n")

	# reporte=dict(zip(listkey,listvalue))
	# print reporte
	yearslost.close()




	# buscar_en_liliana("m03-6688.txt")
