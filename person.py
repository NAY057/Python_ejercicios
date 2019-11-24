# -*- coding: utf-8 -*-

class Persona:
	def __init__(self,sexo, nombre, color, peso, edad, altura):
		self._sexo = sexo
		self._nombre = nombre
		self._color = color
		self._peso = peso
		self._edad = edad
		self._altura = altura


   
	def setNombre(self):
		nombre = str(raw_input('Ingrese el nombre de la persona que quieres crear: '))
		self._nombre = nombre
	  

	def setColor(self):
		color = str(raw_input('Ingrese el color de la piel: '))
		self._color = color

	def setPeso(self):
		peso = int(raw_input('Ingrese el peso de la persona en kg: '))
		self._peso = peso

	def setEdad(self):
		edad = int(raw_input('Ingrese la edad de la persona: '))
		self._edad = edad

	def setAltura(self):
		altura = int(raw_input('Ingrese la altura de la persona en Cm: '))
		self._altura = altura   

	def setSexo(self):
		
		sexo = str(raw_input('Ingrese el sexo de la persona "F" O "M": '))
	
		self._sexo = sexo 


	def getSexo(self):
		return self._sexo
   
	def getNombre(self):
		return self._nombre

	def getColor(self):
		return self._color

	def getPeso(self):
		return self._peso
       
	def getEdad(self):
		return self._edad
       
	def getAltura(self):
		return self._altura       
       



def run():
	persona1 = Persona('','','','','','')
	nombre2 = str(raw_input('Porfavor ingresa tu nombre: '))
	persona1.setSexo()
	print(' ')
	persona1.setNombre()
	print(' ')
	persona1.setEdad()
	print(' ')
	persona1.setAltura()
	print(' ')
	persona1.setPeso()
	print(' ')
	persona1.setColor()
	print(' ')
	print('*************************************************')
	print('--------ASI ES LA PERSONA QUE CREASTE {}-------- ')
	print(' ')
	print('Creador: {}'.format(str.upper(nombre2)))
	print('*************************************************')
	

	print('Nombre: {}'.format(persona1.getNombre()))

	sexo = persona1.getSexo()
	
	if sexo  == ("m"or"M"):
		print('Sexo: {}'.format('Masculino'))
	else:
		print('Sexo: {}'.format('Femenino'))
	
	print('Color: {}'.format(persona1.getColor()))
	print('Peso: {}'.format(persona1.getPeso()))
	print('Edad: {}'.format(persona1.getEdad()))
	print('Altura: {}'.format(persona1.getAltura()))
  
if __name__ == '__main__':

	run()
