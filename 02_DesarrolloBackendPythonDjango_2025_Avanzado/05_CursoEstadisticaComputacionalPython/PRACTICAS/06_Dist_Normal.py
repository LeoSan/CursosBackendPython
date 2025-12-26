import numpy as np
import matplotlib.pyplot as plt

def tirar_dados(n_tiradas):
    # Simula la tirada de 2 dados y devuelve las sumas
    resultado = [np.random.randint(1, 7) + np.random.randint(1, 7) for _ in range(n_tiradas)]
    return resultado

def graficar_histograma(data, n_tiradas):
    # Crea un histograma de los resultados
    plt.hist(data, bins=np.arange(2, 14) - 0.5, density=True, 
             alpha=0.6, color='g', label='Distribución de Sumas')
    
    # Graficar la distribución normal
    mu = np.mean(data)
    sigma = np.std(data)
    x = np.linspace(2, 12, 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    plt.plot(x, y, color='red', label='Distribución Normal')

    # Personalizar el gráfico
    plt.title(f'Histograma de Sumas de {n_tiradas} Tiradas de 2 Dados')
    plt.xlabel('Suma')
    plt.ylabel('Frecuencia Relativa')
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid()
    plt.show()

def main():
    n_tiradas = 10000  # Número de tiradas de dados
    resultados = tirar_dados(n_tiradas)
    graficar_histograma(resultados, n_tiradas)

main()