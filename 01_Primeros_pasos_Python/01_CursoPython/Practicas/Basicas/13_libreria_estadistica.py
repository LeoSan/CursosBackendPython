import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo CSV

file_csv_ruta = "/Users/leonard/CursosBackendPython/Primeros_pasos_Python/CursoPython/Practicas/Basicas/productos.csv"

monthly_sales = {}

try:
    with open(file_csv_ruta, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            month = row['month']
            sales = int(row['price'])
            monthly_sales[month] = sales
except IOError as e:
    print(f"Error de E/S al leer el archivo: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    


sales = list(monthly_sales.values())
#print(sales)

#Hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

#Hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Desviación Estándar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {stdev_sales}")

#Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La moda es: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')