import pandas as pd

def atencion():
    mun = input("Ingrese el nombre del municipio: ")
    while True:
        try:
            lim = int(input("Ingrese el Limite de registros: "))
            if lim < 1000:
                break
            print("Error, ese número supera al límite (Límite: 1000)")
        except ValueError:
            print("Error, el número tiene que ser un entero")

    # Llama a la función para obtener datos desde el archivo CSV
    df = obtener_datos_csv(lim, mun.upper())
    df = df[["Estado", "Edad", "Tipo", "Ciudad", "Municipio", "Pais de Origen"]]
    print(df.to_string(index=False))

# Función para obtener datos desde un archivo CSV
def obtener_datos_csv(n, dep):
    # Lee el archivo CSV
    df = pd.read_csv(PARCIAL1/PARCIAL1/Casos_positivos_de_COVID-19_en_Colombia..csv) 

    # Filtra los datos según el Municipio y el límite
    df = df[df['Municipio'] == mun][:n]

    return df
