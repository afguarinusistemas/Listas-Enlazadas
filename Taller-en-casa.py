class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazadas:
    def __init__(self):
        self.cabeza = None

    def insertarInicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def obtenerNodo(self, posicion):
        actual = self.cabeza
        contador = 1

        while actual is not None:
            if contador == posicion:
                return actual

            actual = actual.siguiente
            contador += 1

        return None


# Crear la lista
lista = ListaEnlazadas()

# Insertar nombres
lista.insertarInicio("Danna")
lista.insertarInicio("Bleimar")
lista.insertarInicio("Tulio")
lista.insertarInicio("Fabian")
lista.insertarInicio("Doñaluz")

# Preguntar al usuario qué nodo desea consultar
numero = int(input("¿Qué nodo desea mostrar? "))

nodo = lista.obtenerNodo(numero)

if nodo is not None:
    print("El dato del nodo", numero, "es:", nodo.dato)
else:
    print("Ese nodo no existe.")

    