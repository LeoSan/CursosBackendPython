import matplotlib.pyplot as plt

def generate_pie_chart(labels,values, nombre):
    directorio = "/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/03_Curso_Python_PIP_Entornos_Virtuales/practica/13_pandas/"

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(directorio + nombre + '.png')
    plt.close()