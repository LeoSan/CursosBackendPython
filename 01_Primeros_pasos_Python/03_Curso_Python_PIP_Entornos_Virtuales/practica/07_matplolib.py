import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    directorio = "/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/03_Curso_Python_PIP_Entornos_Virtuales/info/practica/"
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(directorio+'pie.png')
    plt.show()
    plt.close()

if __name__ == '__main__':
    generate_pie_chart()