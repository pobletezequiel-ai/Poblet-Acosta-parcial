class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = max(1, min(100, nivel))
    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
    def __str__(self):
        return f"Nombre:{self.nombre}, Tpo: {self.tipo}, Nivel: {self.nivel}"
class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []
    def agregar_pokemon(self, pokemon: Pokemon):
        if len(self.equipo)< 6:
            self.equipo.append(pokemon)
            print(f"¡{pokemon.nombre} fue añadido al equipo de {self.nombre}!")
            else:
                print(
                    f"Aviso:{pokemon.nombre} ya tiene 6 pokemones en su equipo . No se puede tener más."
                )
    def mostrar_equipo(self):
        print(f"Equipo pokemon de {self.nombre}:")
        if not self.equipo:
            print( "(El equipo estavacio)") 
            for pokemon in self.equipo:
                print(f" - {pokemon}")
    def nivel_promedio(self) -> float:
        if not self.equipo:
            return 0 
        total_niveles = sum(p.nivel for p in self.equipo)
        return total_niveles / len(self.equipo)
        