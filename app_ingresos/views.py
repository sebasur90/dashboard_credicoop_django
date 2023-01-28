from django.shortcuts import render

from django.http import HttpResponse

import pandas as pd


def myview(request):
    # request.session['dataset']
    datos = pd.DataFrame(request.session['dataset'])
    datos.columns = ['FECHA', 'DESCRIPCION', 'COMBTE', 'DEBITO', 'CREDITO', 'SALDO',
                     'CODIGO']

    return HttpResponse(datos)
