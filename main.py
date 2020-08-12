import random
import math
from coordenada import Coordenada

#Crear una coleccion de objetos Coordenada con valor aletorio entre 0 y 100
def crear_coordenadas(coordenadas_numero):
	coordenadas = []
	for i in range(coordenadas_numero):
		coordenada = Coordenada(random.randrange(100), random.randrange(100), i)
		coordenadas.append(coordenada)
	return coordenadas


def main(coordenadas_numero):
	coordenadas = crear_coordenadas(coordenadas_numero)
	for coordenada in coordenadas:
		print(coordenada.get_nombre())
		print(coordenada.get_coordenada())



if __name__=="__main__":
	coordenadas_numero = int(input("Por favor digite cuantas coordenadas quiere tener "))
	main(coordenadas_numero)