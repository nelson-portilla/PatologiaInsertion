import os,sys
#matriz=[[None] * 7 for i in range(2)]

#recibe ../../informes-patologia-html/r03/r03-058.txt.html
def formatear():
	try:
		# inputtxt=open('../listaconpesos/master.txt', 'r')
		inputtxt=open('../listaconpesos/masterhtml.txt', 'r')
		# outputtxt=open('../listaconpesos/master_formateado.txt', 'w')
		outputtxt=open('../listaconpesos/master_formateado_html.txt', 'w')

		for linea in inputtxt:
			linea=linea.rstrip()			
			if linea[:5]=="-rw-r":
				print "formating..."								
				lista=linea.split()			
				peso=lista[4]				
				nombre = lista [7]				
				outputtxt.write(peso)
				outputtxt.write(" ")
				outputtxt.write(nombre)
				outputtxt.write("\n")
		inputtxt.close()
		outputtxt.close()
	except Exception, e:
		print "Ha fallado",str(e)
		sys.exit(1)

if __name__ == '__main__':
	formatear()