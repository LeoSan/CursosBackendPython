import matplotlib.pyplot as plt

def grafica_barras(labels, values, directorio):
    #labels = ['A', 'B', 'C']
    #values = [200, 34, 120]
    fig, ax = plt.subplots() #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
    ax.bar(labels, values)#aquí le estás indicando que quieres generar una gráfica de barras (bar), y le envías labels y values para que sepa que tiene que crear el gráfico con esos valores
    ax.set_ylabel('Juegos Totales') # Titulo eje Y 
    ax.set_title('Medición total de ganadores y perdedores') # Titulo de la grafica
    #ax.legend(title='Juegos')
    plt.savefig(directorio+'barras.png')# Guarda la grafica 
    plt.show()# Genera la grafica 
    plt.close()# Cierra la grafica


def grafica_pastel(labels, values, directorio):
    #labels = ['A', 'B', 'C']
    #values = [200, 34, 120]
    fig, ax = plt.subplots() #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
    ax.pie(values, labels=labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6, shadow=True, startangle=90)
    plt.savefig(directorio+'pie.png')
    plt.show()
    plt.close()
