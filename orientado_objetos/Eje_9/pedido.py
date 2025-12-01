class ItemPedido:
    def __init__(self, producto, cantidad):
        self._producto = producto
        self._cantidad = cantidad

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor > 0:
            self._cantidad = valor
        else:
            raise ValueError("La cantidad debe ser mayor a cero.")

    @property
    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = ${self.subtotal}"



class Pedido:
    def __init__(self, cliente, fecha):
        self._cliente = cliente
        self._fecha = fecha
        self._items = []
        self._total = 0.0

    @property
    def cliente(self):
        return self._cliente

    @property
    def fecha(self):
        return self._fecha

    @property
    def total(self):
        return self._total

    @property
    def items(self):
        return self._items

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    def agregarProducto(self, producto, cantidad):
        item = ItemPedido(producto, cantidad)
        self._items.append(item)
        self._total += item.subtotal

    def __str__(self):
        texto = f"Pedido del cliente: {self.cliente.nombre}\nFecha: {self.fecha}\n"
        texto += "---- Items ----\n"
        for i in self.items:
            texto += str(i) + "\n"
        texto += f"TOTAL = ${self.total}"
        return texto
