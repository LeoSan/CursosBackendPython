import csv, sys

file_csv_ruta = "/Users/leonard/CursosBackendPython/Primeros_pasos_Python/CursoPython/Practicas/Basicas/productos.csv"
new_product = {
    'name': 'Prueba',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-07-04'
}

with open(file_csv_ruta, mode='a', newline='', encoding='utf-8') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)


with open(file_csv_ruta, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

with open(file_csv_ruta, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Categoria: {row['category']}")

with open(file_csv_ruta, newline='') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(file_csv_ruta, reader.line_num, e))