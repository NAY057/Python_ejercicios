# -*- coding: utf-8 -*-
import random


def  main():
	number_found = False
	random_numbre = random.randint(0, 21)

	while not number_found:
		number = int(raw_input('Intenta un numero: '))

		if number == random_numbre:
			print('Felicidades. encontrate el numero')
			number_found = True
		elif number > random_numbre:
			print('El numero es mas pequeño')
		else:
			print('El numero es mas grnade')




if __name__ == '__main__':
	main()