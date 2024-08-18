import pandas as pd

#Dataframe almacena la informacion con el nombre de los productos y centimetros para poder crear el Excel
dictionaries = {
    "Productos" : ["Pata", "Tablero", "Puerta", "Estante", "Panela Lateral"],
    "Centímetros" : [40, 120,60,30,180]
}

df = pd.DataFrame(dictionaries)

# Guardar el DataFrame en un archivo Excel

df.to_excel("productos_medidas.xlsx", index=False)