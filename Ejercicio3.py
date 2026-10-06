class Evolucion:
    def __init__(self, nombre: str):
        self.nombre  = nombre
        self.siguiente= (
            None
        )
    def __str__ (self):
        return self.nombre
class IteradorPilaEvoluciones:
    def __init__(self, actual):
        self.actual = actual
    def __iter__(self):
        return self 
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        evolucion_actual = self.actual
        self.actual = self.actual.siguiente
        return evolucion_ actual

class PilaEvoluciones:
    def __init__ (self):
        self.cima = (
            None)
    def apilar(self, evolucion: Evolucion):
        evolucion.siguiente = self.cima
        self.cima= evolucion
        print(f"Evolucion {evolucion.nombre} registrada en la pila.")
        )