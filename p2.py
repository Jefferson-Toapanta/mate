import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
w = np.array([[1, 2], [3, 4]])
g = np.array([[10, 20], [30, 40]])
c = np.array([[100, 200], [300, 400]])
data_numeric = [
    [w[0, 0]+w[0, 1], w[1, 0]+w[1, 1], -w[0, 0]-w[1, 0], -w[0, 1]-w[1, 1],
     w[0, 0]+w[0, 1]+w[1, 0]+w[1, 1]-w[0, 0]-w[1, 0]-w[0, 1]-w[1, 1]],
    [g[0, 0]+g[0, 1], g[1, 0]+g[1, 1], -g[0, 0]-g[1, 0], -g[0, 1]-g[1, 1],
        g[0, 0]+g[0, 1] + g[1, 0]+g[1, 1]-g[0, 0]-g[1, 0]-g[0, 1]-g[1, 1]],
    [-c[0, 0], -c[1, 0], +c[0, 0]+c[1, 0], 0, -c[0, 0]-c[1, 0]+c[0, 0]+c[1, 0]],
    [-c[0, 1], -c[1, 1], 0, +c[0, 1]+c[1, 1], -c[0, 1]-c[1, 1]+c[0, 1]+c[1, 1]]
]

s1_numeric = data_numeric[0][0] + data_numeric[1][0] + \
    data_numeric[2][0] + data_numeric[3][0]
print(s1_numeric)
s2_numeric = data_numeric[0][1] + data_numeric[1][1] + \
    data_numeric[2][1] + data_numeric[3][1]
s3_numeric = data_numeric[0][2] + data_numeric[1][2] + \
    data_numeric[2][2] + data_numeric[3][2]
s4_numeric = data_numeric[0][3] + data_numeric[1][3] + \
    data_numeric[2][3] + data_numeric[3][3]


new_row_numeric = [s1_numeric, s2_numeric, s3_numeric, s4_numeric, 0]

print(new_row_numeric)


# Añadir la nueva fila  a los datos numéricos
data_numeric.append(new_row_numeric)

# Definir etiquetas de filas y columnas
row_labels = ['salarios', 'ganancias', 'consumo b1', 'consumo b2', 'total']
columns = ['Hogar 1', 'Hogar 2', 'Firma 1', 'Firma 2', 'Total']

# Crear el DataFrame
df_numeric = pd.DataFrame(data_numeric, columns=columns, index=row_labels)

# Graficar la tabla usando matplotlib
fig, ax = plt.subplots(figsize=(10, 6))  # Establecer tamaño de la figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df_numeric.values, colLabels=df_numeric.columns,
                 rowLabels=df_numeric.index, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)  # Ajustar el tamaño de la fuente según sea necesario
table.scale(1.5, 1.5)  # Ajustar la escala para que todo encaje bien

plt.show()
