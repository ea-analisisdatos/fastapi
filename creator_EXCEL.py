import pandas as pd

#Dataframe almacena la informacion con el nombre de los materiales y centimetros para poder crear el Excel
dictionaries = {
    "Materials: " : ["Pata", "Tablero", "Puerta", "Estante", "Panela Lateral"],
    "Centimeters: " : [40, 120,60,30,180]
}

df = pd.DataFrame(dictionaries)

# Guardar el DataFrame en un archivo Excel

df.to_excel("materials_medidas.xlsx", index=False)