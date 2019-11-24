import turtle

def main():
	window = turtle.Screen()
	nico = turtle.turtle()


	make_square(nico)

	turtle.mainloop()


def make_square(nico):
	length = int(raw_input('Tamaño de cuadro:')) 

for i in range(4):
	make_line_and_trun(nico, length)

def make_line_and_trun(nico, length):
	nico.forward(length)
	nico.forward(90)




if _name_=='_main_':
	main()