import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id,' ',p.text)

p = Pizza.objects.get(id=1)

print(p.text)
print(p.date_added)


toppings = p.toppings_set_all()

for t in toppings:
    print(t.text)
