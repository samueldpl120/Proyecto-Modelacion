class Person:
    def __init__(self, name, base_time, position):
        """
        name: Nombre de la persona
        base_time: Tiempo base para recorrer una cuadra
        position: Posición inicial (calle, carrera)
        """
        self.name = name
        self.base_time = base_time
        self.position = position