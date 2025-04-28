import matplotlib.pyplot as plt

def grafica_barras(labels, values, directorio):
    #labels = ['A', 'B', 'C']
    #values = [200, 34, 120]
    fig, ax = plt.subplots() #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
    ax.bar(labels, values)#aquí le estás indicando que quieres generar una gráfica de barras (bar), y le envías labels y values para que sepa que tiene que crear el gráfico con esos valores
    plt.savefig(directorio+'barras.png')# Guarda la grafica 
    plt.show()# Genera la grafica 
    plt.close()# Cierra la grafica
