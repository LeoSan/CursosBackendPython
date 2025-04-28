import charts 
import pandas as pd

def lee_csv_grafica():
    archivo = "/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/03_Curso_Python_PIP_Entornos_Virtuales/practica/13_pandas/data.csv"
    try:
        df = pd.read_csv(archivo)
        df = df[df['Continent']=='South America']
        countries = df['Country'].values
        porcentages = df['World Population Percentage'].values
        charts.generate_pie_chart(countries,porcentages, 'South America')
    except Exception as e:
        print(f"Error: {e}")
