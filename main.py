import random
import math
import time
import logging
logging.basicConfig(level=logging.INFO)
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from coordenada import Coordenada
from grupos import Grupo

logger = logging.getLogger(__name__)

#Crear una coleccion de objetos Coordenada con valor aletorio entre 0 y 100
def crear_coordenadas(coordenadas_numero):
	logger.info('Creando coordenadas')
	coordenadas = []
	for i in range(coordenadas_numero):
		coordenada = Coordenada(random.randrange(100), random.randrange(100), i)
		coordenadas.append(coordenada)
	return coordenadas

#Funcion para graficar las agrupaciones que se hacen
def graficar(coordenadas, ax):
	ax.cla()
	ax.set_xlim(0.0, 100.0)
	ax.set_ylim(0.0, 100.0)
	ax.scatter(coordenadas[0], coordenadas[1], marker='o', s=coordenadas[2], c=coordenadas[3])
	time.sleep(0.2)

#Guardamos los datos para graficar en un arreglo, se guardan para realizar una grafica dinamica 
def agregar_grafica(coordenadas):
	logger.info('Agregando datos para graficar')
	datos = []
	x = [coordenada.x for coordenada in coordenadas]
	y = [coordenada.y for coordenada in coordenadas]
	s = [coordenada.nivel*100 for coordenada in coordenadas]
	c = [coordenada.color for coordenada in coordenadas]
	datos.append(x)
	datos.append(y)
	datos.append(s)
	datos.append(c)
	frames_graf.append(datos)	

#Medir distancia entre coordenadas
def medir_distancia(x, y):
	return math.sqrt((x**2)+(y**2))

#Realiza comparacion cuando el primer elemento es un grupo
def comparar_grupo(elemento_g, elemento_2):
	distancia_1 = comparar(elemento_g.elemento_1, elemento_2)
	distancia_2 = comparar(elemento_g.elemento_2, elemento_2)
	if distancia_1 < distancia_2:
		return distancia_1			
	else:
		return distancia_2	

#Comparar distancia entre dos elementos
def comparar(elemento_1, elemento_2):
	nombre = elemento_2.get_nombre()+'*'+elemento_1.get_nombre()
	distancia_menor = None
	#Buscar en el diccionario si ya se tiene guardado el valor
	if nombre in dic_distancias:
		return dic_distancias[nombre]
	nombre = elemento_1.get_nombre()+'*'+elemento_2.get_nombre()
	if nombre in dic_distancias:
		return dic_distancias[nombre]

	#Revisar si son instancias de un grupo y volverse a llamar	
	if isinstance(elemento_1, Grupo):
		dic_distancias[nombre] = comparar_grupo(elemento_1, elemento_2)
		return dic_distancias[nombre]

	if isinstance(elemento_2, Grupo):
		dic_distancias[nombre] = comparar_grupo(elemento_2, elemento_1)
		return dic_distancias[nombre]		

	#Medir distancia en caso que no se halla guardado ni sea un grupo	
	dic_distancias[nombre] = medir_distancia(elemento_1.x - elemento_2.x, elemento_1.y - elemento_2.y)	
	return dic_distancias[nombre]	
	
#De la lista elementos, cuales son los dos elementos que tienen la menor distancia entre si
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

#Formar grupos de elementos hasta que solo quede un elemento
def agrupar(elementos, i):
	elemento_1, elemento_2 = menor_distancia(elementos)
	logger.info(f'Haremos grupo de {elemento_1.get_nombre()} y {elemento_2.get_nombre()}')	
	grupo = Grupo(elemento_1, elemento_2, i)
	logger.info(f'Grupo creado {grupo.get_nombre()}')	
	elementos.remove(elemento_1)
	elementos.remove(elemento_2)
	elementos.append(grupo)
	agregar_grafica(elementos)	
	if (len(elementos)>1):
		elementos = agrupar(elementos, i+1)
	
	return elementos	

#Funcion principal
def main(coordenadas_numero):
	logger.info(f'Has seleccionado {coordenadas_numero} coordenadas')
	coordenadas = crear_coordenadas(coordenadas_numero)
	agregar_grafica(coordenadas)
	elementos = agrupar(coordenadas, 0)
	logger.info(f'El grupo final es {elementos[0].get_nombre()}')
	fig, ax = plt.subplots()	
	ax.set_xlim(0.0, 100.0)
	ax.set_ylim(0.0, 100.0)		
	animation = FuncAnimation(fig, func=graficar, frames=frames_graf, fargs=(ax,))
	plt.show()
	


#Arreglo y diccionario como estructuras de datos glogales
frames_graf = []
dic_distancias = {}
if __name__=="__main__":
	coordenadas_numero = int(input("Por favor digite cuantas coordenadas quiere tener "))
	main(coordenadas_numero)