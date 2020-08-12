class Coordenada(object):
	def __init__(self, x, y, nombre):
		self._nombre = 'c' + str(nombre)
		self.x = x
		self.y = y
		self.color = 'blue'
		self.nivel = 1
		
	def get_coordenada(self):
		return (self.x, self.y)


	def get_nombre(self):
		return self._nombre	
