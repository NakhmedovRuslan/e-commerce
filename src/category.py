from src.product import Product


class Category:
    """Класс для категорий товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """Метод, добавляющий объект в категорию, если объект относится к классу"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return self.__products

    def __str__(self):
        total_quantity = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {total_quantity}"
