import json
import random
from faker import Faker

fake = Faker("ru_RU")

TOTAL = 50_000
OUTPUT_FILE = "products.json"

categories = [
    "Электроника", "Одежда", "Обувь", "Дом и сад", "Красота",
    "Спорт", "Детские товары", "Книги", "Продукты", "Автотовары"
]

brands = [
    "NovaTech", "Aurora", "Kvart", "BaltLine", "Terra",
    "Solaris", "Nordwind", "Prime", "Urban", "Vega"
]

def make_product(product_id: int) -> dict:
    category = random.choice(categories)
    brand = random.choice(brands)
    price = round(random.uniform(199, 99_999), 2)

    return {
        "id": product_id,
        "sku": f"SKU-{product_id:06d}",
        "name": f"{brand} {fake.word().capitalize()} {fake.word().capitalize()}",
      }

products = [make_product(i) for i in range(1, TOTAL + 1)]

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)

print(f"Готово: {TOTAL} товаров сохранены в {OUTPUT_FILE}")