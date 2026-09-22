def dobrar(numero):
 	return numero * 2

 assert dobrar(3) == 6 #P
 assert dobrar(0) == 1 #F    #Resultado real == 0     #Estava incorreto por que o assert afirmava que 0 * 2 era 1
 assert dobrar(-2) == -4 #P