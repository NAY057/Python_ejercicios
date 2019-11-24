# -*- coding: utf-8 -*-
import turtle

def main():
	window = turtle.Screen()
	nico = turtle.Turtle()


	make_square(nico)

	turtle.mainloop()


def make_square(nico):
	length = int(raw_input('Tamaño de cuadro: ')) 

 	
 	for i in range(100):
	        make_line_and_trun(nico, length)


def make_line_and_trun(nico, length):
	nico.forward(length)
	nico.left(120+2)




if __name__=='__main__':
	main()