import random
class A:
    i = 5
    def __init__(self):
        self.i = random.randint(1,100)

    def getI(self):
        return self.i

one = A()
print(A.i)
print(one.getI())
two = A()
print(two.getI())

class Restaurant(object):
    def __init__(self, cad_nombre, cad_propietario, cad_chef):
        self.nombre = cad_nombre
        self.propietario = cad_propietario
        self.chef = cad_chef
        self.dishes = 15

    def __str__(self):
        return (self.nombre + "(Propietario: " + self.propietario + ", Chef: " + self.chef +")")


mcAlgo = Restaurant("Hamburguesas MCAlgo", "Josue", "Alisson")
print(mcAlgo)
print(dir(mcAlgo))

class Saucer(object):
    def __init__(self, cadNombre, realPrecio, cadDescripcion=None, cadImgen=None, boolVegetariano=False,entCoccion=1):
        self.nombre = cadNombre
        self.precio = realPrecio
        self.descripion = cadDescripcion
        self.imagen = cadImgen
        self.esVegetariano = boolVegetariano
        self.coccion = entCoccion

    def __str__(self):
        return "{nombre}{esVeg}: {precio:.2f}{desc}".format(
        nombre = self.nombre,
        desc = '('+self.descripion + ')' if self.descripion else '',
        precio = self.precio,
        esVeg='*' if self.esVegetariano else ' ')

burgerPyton = Saucer("Hamburguesa de Python", 0.13, cadDescripcion="Barely an eighth of a byte")
print(burgerPyton)
