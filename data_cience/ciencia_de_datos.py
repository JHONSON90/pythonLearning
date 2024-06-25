import pandas as pd

try:
    data = pd.read_csv("data_cience/movimientonominasep-oct-nov.csv")
    print("La importacion se realizo satisfactoriamente")
except:
    print("No se pudo importar adecuadamente")
