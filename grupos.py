class Grupo(object):
	def __init__(self, elemento_1, elemento_2, nombre)
		self.elemento_1 = elemento_1
		self.elemento_2 = elemento_2
		self._nombre = 'g' + str(nombre)

	def get_grupo(self):
		return (self.elemento_1, self.elemento_2) 
		
	def get_nombre(self):
		return self._nombre