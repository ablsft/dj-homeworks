import random

from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from faker import Faker
from faker_food import FoodProvider

from logistic.models import Product, Stock, StockProduct


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        pass

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = Faker()
        fake.add_provider(FoodProvider)

        product_titles = list([fake.fruit() for _ in range(500)])
        product_titles += list([fake.vegetable() for _ in range(500)])
        product_titles += list([fake.ingredient() for _ in range(500)])
        product_titles = list(set(product_titles))
        
        for i in range(len(product_titles)):
            product = Product(title=product_titles[i],
                              description=fake.dish_description())
            product.save()

        for _ in range(30):
            stock = Stock(address=fake.address())
            stock.save()

        product_objects = Product.objects.all()
        stock_objects = Stock.objects.all()

        for _ in range(300):
            stockproduct = StockProduct(stock=random.choice(stock_objects),
                                        product=random.choice(product_objects),
                                        quantity=random.randrange(20),
                                        price=random.randrange(50, 500))
            stockproduct.save()
