#Importa funciones de los modulos dentro del paquete
from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sale

add_product('Laptop', 10)
remove_product('Laptop')
process_sale('Laptop', 2)