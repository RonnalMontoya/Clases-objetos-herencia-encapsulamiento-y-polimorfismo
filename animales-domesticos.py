class Animal:
    """
    Clase base que representa un animal.
    """

    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado para almacenar el nombre del animal

    def hacer_sonido(self):
        """
        Método abstracto para hacer un sonido.
        """
        raise NotImplementedError("Este método debe ser sobrescrito en una subclase")

    def obtener_nombre(self):
        """
        Método público para obtener el nombre del animal.
        """
        return self.__nombre

class Perro(Animal):
    """
    Clase derivada que representa un perro.
    Hereda de la clase Animal.
    """

    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Inicializa la clase base
        self.__raza = raza  # Atributo privado para almacenar la raza del perro

    def hacer_sonido(self):
        """
        Método sobrescrito para hacer el sonido del perro.
        """
        return "Guau"

    def obtener_raza(self):
        """
        Método público para obtener la raza del perro.
        """
        return self.__raza

class Gato(Animal):
    """
    Clase derivada que representa un gato.
    Hereda de la clase Animal.
    """

    def __init__(self, nombre, color):
        super().__init__(nombre)  # Inicializa la clase base
        self.__color = color  # Atributo privado para almacenar el color del gato

    def hacer_sonido(self):
        """
        Método sobrescrito para hacer el sonido del gato.
        """
        return "Miau"

    def obtener_color(self):
        """
        Método público para obtener el color del gato.
        """
        return self.__color

# Función que demuestra el polimorfismo
def mostrar_info_animal(animal):
    print(f"Nombre: {animal.obtener_nombre()}")
    print(f"Sonido: {animal.hacer_sonido()}")

# Crear instancias de las clases
perro = Perro("Chiquitin", "French")
gato = Gato("Michifu", "Negro")

# Mostrar información de cada animal
print("Información del Perro:")
mostrar_info_animal(perro)
print(f"Raza: {perro.obtener_raza()}")

print("\nInformación del Gato:")
mostrar_info_animal(gato)
print(f"Color: {gato.obtener_color()}")