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

def comparar(elemento_1, elemento_2):
	nombre = elemento_1.get_nombre()+'*'+elemento_2.get_nombre()
	distancia_menor = None
	if nombre in dic_distancias:
		return dic_distancias[nombre]
	if isinstance(elemento_1, Grupo):
		distancia_1 = comparar(elemento_1.elemento_1)
		distancia_2 = comparar(elemento_1.elemento_2)
		if distancia_1 < distancia_2:
			dic_distancias[nombre] = distancia_1			
		else
			dic_distancias[nombre] = distancia_2
		return dic_distancias[nombre]

	if isinstance(elemento_2, Grupo):
		distancia_1 = comparar(elemento_2.elemento_1)
		distancia_2 = comparar(elemento_2.elemento_2)
		if distancia_1 < distancia_2:
			dic_distancias[nombre] = distancia_1			
		else
			dic_distancias[nombre] = distancia_2 
		return dic_distancias[nombre]

	dic_distancias[nombre] = medir_distancia(elemento_1.x - elemento_2.x, elemento_1.y - elemento_2.y)	
	return dic_distancias[nombre]	
	

def menor_distancia(elementos):
	distancia_menor = None
	elemento_1 = None
	elemento_2 = None
	for i in range(len(elementos)-1):		
		for j in range(i+1, len(elementos)):
			distancia = comparar(elementos[i],elementos[j])
			
			if distancia_menor:				
				if distancia < distancia_menor:
					distancia_menor = distancia
					elemento_1 = elementos[i]
					elemento_2 = elementos[j]
			else:
				distancia_menor = distancia
				elemento_1 = elementos[i]
				elemento_2 = elementos[j]
	return (elemento_1, elemento_2)			

def agrupar(elementos):
	distancia_menor = None		
	elemento_1, elemento_2 = menor_distancia(elementos) 
	grupo = Grupo(elemento_1, elemento_2, i)
	elementos.remove(elemento_1)
	elementos.remove(elemento_2)
	elementos.append(grupo)
	if (len(elementos)>1):
		elementos = agrupar(elementos)
	
	return elementos	

def main(coordenadas_numero):
	coordenadas = crear_coordenadas(coordenadas_numero)
	elementos = agrupar(coordenadas)
	print(elementos[0].get_nombre)



dic_distancias = {}
if __name__=="__main__":
	coordenadas_numero = int(input("Por favor digite cuantas coordenadas quiere tener "))
	main(coordenadas_numero)