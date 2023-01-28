import numpy as np
import pandas as pd
import jinja2

datos_sin_procesar = pd.read_csv("datos.CSV")

sueldos = datos_sin_procesar[datos_sin_procesar.concepto ==
                             "acreditacion de sueldos "]

listado = list(sueldos.val_abs)


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

jinja_var = {'title': sueldos}

template = jinja_env.get_template("content.html")

output_from_parsed_template = template.render(jinja_var)
with open("my_new_file.html", "w") as fh:
    fh.write(output_from_parsed_template)
