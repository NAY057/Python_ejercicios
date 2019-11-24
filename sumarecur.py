# -*- coding: utf-8 -*-



def cargar_lista():
	li=[]
	number = int(raw_input('ingrese el numero de valores que quiere sumar: '))
	for i in range(0,number):
		print('Ingrese el valor numero {} '.format(number))
		valor = int (raw_input())
		li.append(valor)
		number -= 1

	return(li)




if __name__ == '__main__':
	
	lista = cargar_lista()
	print(' ')
	print('E L  R E S U L T A D O  E S  ' )
	print(' ')
	print(sum(lista))

	

#	sumar_lista(li)


	
	
	