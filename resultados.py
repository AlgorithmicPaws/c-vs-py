import matplotlib.pyplot as plt

# Datos de comparación de tiempo entre C y Python para factorial iterativo y recursivo
tamanio_factorial = [5, 10, 15, 20, 25]
c_iterativo = [0.001, 0.002, 0.003, 0.005, 0.008]
c_recursivo = [0.002, 0.005, 0.012, 0.025, 0.045]
python_iterativo = [0.005, 0.012, 0.025, 0.042, 0.065]
python_recursivo = [0.012, 0.025, 0.045, 0.072, 0.110]

# Graficar los datos
plt.figure(figsize=(10, 6))

# Graficar el tiempo de ejecución de C
plt.plot(tamanio_factorial, c_iterativo, label='C Iterativo', marker='o')
plt.plot(tamanio_factorial, c_recursivo, label='C Recursivo', marker='o')

# Graficar el tiempo de ejecución de Python
plt.plot(tamanio_factorial, python_iterativo, label='Python Iterativo', marker='o')
plt.plot(tamanio_factorial, python_recursivo, label='Python Recursivo', marker='o')

# Agregar título y etiquetas de los ejes
plt.title('Comparación de Tiempos de Ejecución entre C y Python')
plt.xlabel('Tamaño del Factorial')
plt.ylabel('Tiempo de Ejecución (segundos)')

# Mostrar leyenda y grid
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
