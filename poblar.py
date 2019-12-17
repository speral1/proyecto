# PSI Practica 3
# Grupo: 2401
# Pareja: 1
# Autoras: Inés Mozas y Sara Peral
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import pizza, ingrediente, contiene

def test_query():

    pizza_a = pizza.objects.create(id=1001, nombreP="pizza_a")
    pizza_b = pizza.objects.create(id=1002, nombreP="pizza_b")
    pizza_c = pizza.objects.create(id=1003, nombreP="pizza_c")

    ingrediente_a = ingrediente.objects.create(id=1001, nombreI="ingrediente_a")
    ingrediente_b = ingrediente.objects.create(id=1002, nombreI="ingrediente_b")
    ingrediente_c = ingrediente.objects.create(id=1003, nombreI="ingrediente_c")
    ingrediente_d = ingrediente.objects.create(id=1004, nombreI="ingrediente_d")


    contiene.objects.create(id=1001, pizza=pizza_a, ingrediente=ingrediente_a, porcentaje=43.2)
    contiene.objects.create(id=1002, pizza=pizza_b, ingrediente=ingrediente_b, porcentaje=34.2)
    contiene.objects.create(id=1003, pizza=pizza_b, ingrediente=ingrediente_c, porcentaje=27.4)
    contiene.objects.create(id=1004, pizza=pizza_a, ingrediente=ingrediente_c, porcentaje=13.2)


# Start execution here!
if __name__ == '__main__':
    print('Starting poblar script...')
    test_query()
