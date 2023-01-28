from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    titulo = "PASANDO PARAMETROS"
    lista = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']

    import random
    meses = ['enero', 'febrero', 'marzo', 'abril']
    anos = [2018, 2019, 2020]
    valores = []
    request.session['fav_color'] = 'blue'
    print(request.session['fav_color'])
    for x in anos:
        valores.append([[x, random.randint(10000, 100000)]
                       for x, y in zip(meses, range(len(meses)))])
    if request.method == "POST":
        import csv
        csv_file = request.FILES['file']
        print(csv_file)
        data_set = csv_file.read().decode('UTF-8')
        data = data_set.split("\n")
        # data = csv.DictReader(request.FILES['file'])
        # reader = csv.DictReader(data_set)
        # data=csv.reader
        print(len(data))
        lista_valores = []
        for x in range(len(data)):
            if x == 0 or x == len(data):
                pass
            else:
                lista_valores.append(data[x].split(";"))
        request.session['dataset'] = lista_valores
        # print(data_set)
    # csv_file = request.FILES['file']

    return render(request, 'index.html', {'titulo': titulo, 'lista': lista, 'valores': valores},
                  )
