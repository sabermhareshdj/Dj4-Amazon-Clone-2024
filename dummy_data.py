import os , django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand , Product


def seed_brand(n):
  fake = Faker()
  images = ['1.jpeg','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
  for _ in range(n):
    Brand.objects.create(
      name = fake.name() , 
      image = f'brands/{images[random.randint(0,9)]}'

    )
  print(f'Seed {n} Brands Successfully')

def seed_product(n):
  fake = Faker()
  images = ['1.jpeg','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
  flags =['Sale','New','Feature']
  for _ in range(n):
    Product.objects.create(
      name = fake.name() , 
      image = f'brands/{images[random.randint(0,9)]}' ,
      flag = flags[random.randint(0,2)] ,
      price = round(random.uniform(20.99,99.99),2) ,
      sku = random.randint(1000,10000000) ,
      subtitle = fake.text(max_nb_chars=250) ,
      description = fake.text(max_nb_chars=20000) ,
      quantity = random.randint(0,30) ,
      brand = Brand.objects.get(id=random.randint(1,100)),
      tags="dummy",
    )
    print(f'Seed {n} products Successfully')




#seed_brand(200)
seed_product(2000)