import pandas as pd

def centimetros_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo excel:
df = pd.read_excel("productos_medidas.xlsx")

# Añadir una columna al Dataframe que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Pulgadas"] = df["Centímetros"].apply(centimetros_a_pulgadas)
df.to_excel("productos_medidas_convertidas.xlsx", index=False)

print("Conversión completada y guardada en un nuevo archivo llamado 'productos_medidas_convertidas.xlsx'")