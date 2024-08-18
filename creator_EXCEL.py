import pandas as pd

#Dataframe almacena la informacion con el nombre de los materiales y centimetros para poder crear el Excel
diccionario = {
    "Materiales: " : ["Pata", "Tablero", "Puerta", "Estante", "Panela Lateral"],
    "Centímetros: " : [40, 120,60,30,180]
}

df = pd.DataFrame(diccionario)

# Guardar el DataFrame en un archivo Excel

df.to_excel("productos_medidas.xlsx", index=False)