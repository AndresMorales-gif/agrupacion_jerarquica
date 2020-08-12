class Grupo(object):
	def __init__(self, elemento_1, elemento_2, nombre):
		self.elemento_1 = elemento_1
		self.elemento_2 = elemento_2
		self._nombre = 'g' + str(nombre)
		self.color = 'red'
		self._hallar_centro()
		self._hallar_nivel()

	def get_grupo(self):
		return (self.elemento_1, self.elemento_2) 
		
	def get_nombre(self):
		return self._nombre

	def get_centro(self):
		return (self.x, self.y)

	def _hallar_centro(self):
		if isinstance(self.elemento_1, Grupo):
			x1, y1 = self.elemento_1.get_centro()
		else:
			x1, y1 = self.elemento_1.get_coordenada()
		if isinstance(self.elemento_2, Grupo):
			x2, y2 = self.elemento_2.get_centro()
		else:
			x2, y2 = self.elemento_2.get_coordenada()
		self.x = (x1+x2) / 2
		self.y = (y1+y2) / 2

	def _hallar_nivel(self):
		self.nivel = 2
		if isinstance(self.elemento_1, Grupo):
			self.nivel += self.elemento_1.nivel		
		if isinstance(self.elemento_2, Grupo):
			self.nivel += self.elemento_2.nivel