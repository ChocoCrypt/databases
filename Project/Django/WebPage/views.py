from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from os import system
def openfile(file):
    file = open(file, 'r').read()
    return(file)

def index(response):
    index = open("/home/bogomonsta/Semestre2020-1/BasesDeDatos/Project/WebPage/WebPage/Templates/index.html" , 'r').read()
    # for i in range(0,1000000):
    #     print(i)
    return(HttpResponse(index))

def documentoPdf(response):
    pdf = open("/home/bogomonsta/Semestre2020-1/BasesDeDatos/Project/WebPage/WebPage/Templates/pdf.html" , 'r').read()
    return(HttpResponse(pdf))

def documentopng(response):
    png = open("/home/bogomonsta/Semestre2020-1/BasesDeDatos/Project/WebPage/WebPage/Templates/png.html" , 'r').read()
    return(HttpResponse(png))

def documentojpg(response):
    jpg = open("/home/bogomonsta/Semestre2020-1/BasesDeDatos/Project/WebPage/WebPage/Templates/jpg.html" , 'r').read()
    return(HttpResponse(jpg))

def agarrarpdf(request):
    return(HttpResponse("buena"))

@csrf_exempt #ESTO SEGURO ESTA RE MAL PERO ES LA FORMA QUE ENCONTRE DE HACERLO AUNQUE SERIA BUENO PREGUNTAR COMO NO PONER ESTO Y HACERLO BIEN
def descargarpdf(request):
    if(request.method == "POST"):
        print("*"*100)
        print(request.POST)
        pdf = request.POST
        mipdf = request.POST.get("archivoPdf" , "file")#este es solo el nombre
        print(mipdf)
        print("*" * 100)
        return(HttpResponse("buenaaa , lo lograste y ingresaste :" + str(mipdf)))
    else:
        return(redirect('https://www.google.com'))
