class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    '''def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id":producto.id,
                "imagen":producto.imagen.url,
                "nombre":producto.nombre,
                "precio":producto.precio,
                "sub_total":producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["sub_total"] += producto.precio

        self.guardar()'''

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "imagen": producto.imagen.url,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "sub_total": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["sub_total"] = self.carrito[id]["cantidad"] * producto.precio

        self.guardar()

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.guardar()
    
    '''def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["sub_total"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar()'''

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["sub_total"] = self.carrito[id]["cantidad"] * producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar()


    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def calcular_total(self):
        total = 0
        for item in self.carrito.values():
            total += item["sub_total"]
        return total