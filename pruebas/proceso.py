import numpy as np
import pandas as pd

datos_sin_procesar = pd.read_csv(
    "H:/dashboards/credicoop_django/pruebas/000035840-MOVCTA-10010306316-20221107-103411.CSV", sep=";")
meses_del_ano = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                 "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
meses_del_ano_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
anos = [2018, 2019, 2020, 2021, 2022]
datos = datos_sin_procesar.copy()
datos.columns = datos.columns.str.lower()
datos['descripcion'] = datos['descripcion'].str.lower()
datos['fecha'] = pd.to_datetime(datos['fecha'], format='%Y%m%d')
columnas = ['debito', 'credito', 'saldo']
for columna in columnas:
    datos[columna] = datos[columna].str.replace('.', '', regex=True)
    datos[columna] = datos[columna].str.replace(',', '.', regex=True)
    datos[columna] = datos[columna].astype(float)

anos = range(datos.fecha.iloc[-1].year, datos.fecha.iloc[0].year)


conceptos = []

datos['concepto'] = np.where(datos.descripcion.str.contains("pago de servicios ente: "),
                             datos.descripcion.map(
    lambda x: x[len("pago de servicios ente: "):]),
    np.where(datos.descripcion.str.contains("compra con tarjeta cabal debito"),
             datos.descripcion.map(
        lambda x: x[len("compra con tarjeta cabal debito tarj:xxxx comercio:"):]),
    np.where(datos.descripcion.str.contains("transf."), "transferencias",
             np.where(datos.descripcion.str.contains(
                 "debito/cred aut-segurcoop seg"),
        "debito/cred aut-segurcoop seg",
        np.where(datos.descripcion.str.contains("constitucion de plazo fijo"), "constitucion de plazo fijo",
                 np.where(datos.descripcion.str.contains("mercado libre") | datos.descripcion.str.contains("mercadolibre"), "mercadolibre",

                          np.where(
                     datos.descripcion.str.contains(
                         "debito/credito automatico-tarjeta cabal"),
                     "cabal",
                     np.where(datos.descripcion.str.contains(
                         "debito/credito automatico-tarjeta visa"), "visa",
                         np.where(datos.descripcion.str.contains("cajero automatico"),
                                  "retiro de cajero automatico",
                                  np.where(
                                  datos.descripcion.str.contains(
                                      "compra/venta de moneda extranjera"),
                                  "compra/venta de moneda extranjera", datos.descripcion
                         ))))))))))


''' datos = pd.merge(
    datos, st.session_state['datos_ccl'], on='fecha', how='inner')


datos['ccl'] = datos['ccl'].fillna(method='bfill')
datos = datos.fillna(0)
datos = datos.dropna()

datos['debito_usd_ccl'] = round(
    datos['debito'] / datos['ccl'], 2)
datos['credito_usd_ccl'] = round(
    datos['credito'] / datos['ccl'], 2)

datos['val_abs_usd_ccl'] = datos['credito_usd_ccl'] + \
    datos['debito_usd_ccl'] '''

datos = datos.fillna(0)
datos = datos.dropna()

datos['ano'] = pd.DatetimeIndex(datos['fecha']).year

anos = datos['ano'].sort_values(ascending=True).unique()
ultimo_ano = anos[-1]

datos['mes'] = pd.DatetimeIndex(datos['fecha']).month
datos = datos.set_index('fecha')
datos = datos.sort_values(by='fecha')
datos['val_abs'] = abs(datos['credito'] + datos['debito'])
datos_procesados = datos

print(datos)
datos.to_csv("datos.csv")
