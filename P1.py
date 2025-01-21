import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Crear variables de salarios W(i,j), ganancias G(i,j), consumos C(i,j)
# i es el hogar, j la firma o bien
w = np.array([[1, 2], [3, 4]])
g = np.array([[10, 20], [30, 40]])
c = np.array([[100, 200], [300, 400]])

# Create a DataFrame with the desired variables (using '\n' for line breaks in the problematic cells)
data = [
    ['w[0,0]+w[0,1]', 'w[1,0]+w[1,1]', '-w[0,0]-w[1,0]', '-w[0,1]-w[1,1]',
     'w[0,0]+w[0,1]\n+w[1,0]+w[1,1]\n-w[0,0]-w[1,0]\n-w[0,1]-w[1,1]'],
    ['g[0,0]+g[0,1]', 'g[1,0]+g[1,1]', '-g[0,0]-g[1,0]', '-g[0,1]-g[1,1]',
        'g[0,0]+g[0,1]\n+ g[1,0]+g[1,1]\n-g[0,0]-g[1,0]\n-g[0,1]-g[1,1]'],
    ['-c[0,0]', '-c[1,0]', '+c[0,0]+c[1,0]', '', '-c[0,0]-c[1,0]\n+c[0,0]+c[1,0]'],
    ['-c[0,1]', '-c[1,1]', '', '+c[0,1]+c[1,1]', '-c[0,1]-c[1,1]\n+c[0,1]+c[1,1]']
]

s1 = f"{data[0][0]} \n +{data[1][0]} \n {data[2][0]} \n {data[3][0]}"
s2 = f"{data[0][1]}\n+{data[1][1]} \n {data[2][1]} \n{data[3][1]}"
s3 = f"{data[0][2]}\n{data[1][2]} \n {data[2][2]} \n{data[3][2]}"
s4 = f"{data[0][3]}\n{data[1][3]} \n {data[2][3]} \n{data[3][3]}"

new_row = [s1, s2, s3, s4, '0 \n   ']

data.append(new_row)

row_labels = ['salarios', 'ganancias', 'consumo b0', 'consumo b1', 'total']
columns = ['Hogar 0', 'Hogar 1', 'Firma 0', 'Firma 1', 'total']

# Crear el DataFrame
df = pd.DataFrame(data, columns=columns, index=row_labels)

# Función para calcular la altura de la celda según el número de líneas


def calculate_cell_height(cell_text, base_height=0.05):
    # Contar el número de líneas (se cuentan los '\n')
    # al menos 1 línea aunque no haya '\n'
    num_lines = cell_text.count('\n') + 1
    return base_height * num_lines


# Graficar la tabla usando matplotlib
fig, ax = plt.subplots(figsize=(10, 6))  # Establecer tamaño de la figura
ax.axis('tight')
ax.axis('off')

# Crear la tabla
table = ax.table(cellText=df.values, colLabels=df.columns,
                 rowLabels=df.index, cellLoc='center', loc='center')

# Ajustar el tamaño de la fuente
table.auto_set_font_size(False)
table.set_fontsize(10)

# Ajustar la altura de las filas automáticamente según el contenido
for i in range(len(df)+1):  # Recorremos las filas
    # Calcular la altura máxima de todas las celdas en la fila
    max_height = max(calculate_cell_height(cell.get_text().get_text())
                     for (row, col), cell in table.get_celld().items() if row == i)
    # Ajustar la altura de todas las celdas en la fila con la altura máxima
    for (row, col), cell in table.get_celld().items():
        if row == i:
            cell.set_height(max_height)

plt.show()
