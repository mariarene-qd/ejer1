'''
VA LEER UN ARCHVIO.CSV 
DESDE PANDAS
OPERACIONES MATEMATICAS Y ESTADISTICAS
'''

# importar la libreria pandas
import pandas as pd

# 1. Leer datos desde el archivo CSV
# df=variable data frame tabla
df = pd.read_csv("estudiantes.csv")

# 2. Mostrar la tabla completa
print("****** Tabla completa*")
print(df)

# 3. Filtrar alumnos con calificación mayor a 8
print("\n📌 Alumnos con calificación mayor a 8:")
print(df[df['Nota'] > 90])


# 4. Sumar todas las notas
suma_notas = df['Nota'].sum()
print(f"\n📌 Suma total de las notas: {suma_notas}")