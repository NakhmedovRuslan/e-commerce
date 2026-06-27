class Product:
    """Класс для товаров"""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products: list = None):
        if products is not None:
            for product in products:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    product.price = max(product.price, product_data["price"])
                    return product

        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = price

    def __add__(self, other):
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        elif type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.name, self.description, self.price, self.quantity}"


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
