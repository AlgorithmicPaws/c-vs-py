import matplotlib.pyplot as plt

#Datos de comparación de tiempo entre C y Python para factorial iterativo y recursivo
tamanio_factorial = [1, 5, 10, 15, 20, 25]
c_iterativo = [1.42033, 1.42033, 1.56, 1.746, 1.467, 1.443]
c_recursivo = [1.280, 1.559, 1.886, 2.072, 1.9323, 1.909]
python_iterativo = [6.653, 5.75, 7.096, 7.586, 6.746, 7.286]
python_recursivo = [3.513, 4.89, 7.283, 8.356, 11.87, 13.723]

#Graficar los datos
plt.figure(figsize=(10, 6))

#Graficar el tiempo de ejecución de C
plt.plot(tamanio_factorial, c_iterativo, label='C Iterativo', marker='o')
plt.plot(tamanio_factorial, c_recursivo, label='C Recursivo', marker='o')

#Graficar el tiempo de ejecución de Python
plt.plot(tamanio_factorial, python_iterativo, label='Python Iterativo', marker='o')
plt.plot(tamanio_factorial, python_recursivo, label='Python Recursivo', marker='o')

#Agregar título y etiquetas de los ejes
plt.title('Comparación de Tiempos de Ejecución entre C y Python')
plt.xlabel('Tamaño del Factorial')
plt.ylabel('Tiempo de Ejecución (segundos)')

#Mostrar leyenda y grid
plt.legend()
plt.grid(True)

#Mostrar la gráfica
plt.show()