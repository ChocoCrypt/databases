#Rodrigo Castillo Camargo
import pyPdf
from pyPdf import PdfFileReader , PdfFileWriter
from random import randint
from os import system
import os
class archivoPDF:
    def __init__(self , nombrearchivo):
        self.nombrearchivo = nombrearchivo
        self.pfdfile = PdfFileReader(file(nombrearchivo, 'rb'))
        self.docinfo = self.pfdfile.getDocumentInfo()
        self.CreationDate = None
        self.FullBanner =  None
        self.Producer = None
        self.Trapped = None
        self.ModDate = None
        self.Creator = None
        self.CreationDate = None

    def PrintMetaData(self):
        print("Fecha de creacion :" + str(self.CreationDate))
        print("Banner :" + str(self.FullBanner))
        print("Producer :" + str(self.Producer))
        print("Trapped :" + str(self.Trapped))
        print("Fecha de Modificacion :" + str(self.ModDate))
        print("Creador :" + str(self.Creator))
        print("Fecha De Creacion :" + str(self.CreationDate))

    def DefMetadata(self):
        cont  = 0
        for metaitem in self.docinfo:
            cont = cont+1
            if(cont == 1 ):
                self.CreationDate = self.docinfo[metaitem]
                #print("Creation Date = " , self.CreationDate)
            if(cont == 2):
                self.FullBanner = self.docinfo[metaitem]
                #print("FullBanner = " , self.FullBanner)
            if(cont == 3):
                self.Producer = self.docinfo[metaitem]
                #print("Producer = " , self.Producer)
            if(cont == 4):
                self.Trapped = self.docinfo[metaitem]
                #print("Trapped =" , self.Trapped)
            if(cont == 5):
                self.ModDate = self.docinfo[metaitem]
                #print("Fecha Modificacion =" , self.ModDate)
            if(cont == 6):
                self.Creator = self.docinfo[metaitem]
                #print("Creador = ", self.Creator)
            if(cont == 7):
                self.CreationDate = self.docinfo[metaitem]
                #print("Creation Date :" , self.CreationDate)
    def clean(self):
        command = "exiftool -all= " + self.nombrearchivo #la herramienta exiftool limpa los metadatos de un archivo
        system(command)



class ImagenPNG:
    def __init__ (self,path):
        self.path  = path
        self.archivo = open(path , "rb" )
        self.binario = open(path , "rb").read()
        self.filesize = None
        self.ModTime = None
        self.accessTime = None
        self.Megapixels = None
        self.ColorType = None
        self.ImageSize = None

    def DefMetadata(self):
        self.filesize = os.popen("exiftool " + self.path +" |grep File\ Size").read().strip('File\ Size :')

        self.ModTime = os.popen("exiftool "+ self.path + " |grep File\ Modification\ Date").read().strip("File\ Modification\ Date/Time :")

        self.accessTime = os.popen("exiftool " + self.path + " |grep File\ Access\ Date/Time").read().strip('File\ Access\ Date/Time :')

        self.Megapixels = os.popen("exiftool " + self.path + " |grep Megapixels").read().strip("Megapixels :")


    def clean(self):
        command = "mat " + self.path
        system(command)



class ImagenJPG:
    def __init__(self,path):
        self.path  = path
        self.archivo = open(path , "rb")
        self.binario = open(path , "rb").read()
        self.fileSize = None
        self.ModTime = None
        self.Camera =  None
        self.Flash = None
        self.GPSLatitudRef = None
        self.GPSAltitudRef = None
        self.GPSLongitudeRef = None
        self.GPSDateStamp = None
        self.GPSTimeStamp = None
        self.GPSAltitude = None
        self.GPSLatitude = None
        self.GPSLongitude = None
        self.GPSPosition =None

    def DefMetadata(self):
         self.fileSize = os.popen("exiftool " + self.path + " |grep File\ Size").read().strip("File\ Size:")

         self.ModTime = os.popen("exiftool " + self.path +  " |grep File\ Modification\ Date/Time").read().strip("File\ Modification\ Date/Time:")

         self.Camera = os.popen("exiftool " +  self.path + "|grep Camera\ Model\ Name ").read().strip("Camera\ Model\ Name:")

         self.Flash = os.popen("exiftool " + self.path + " |grep  Flash").read().strip("Flash:")

         self.GPSLatitudeRef = os.popen("exiftool " + self.path + "|grep GPS\ Latitude\ Ref").read().strip("GPS\ Latitude\ Ref")

         self.GPSAltitudeRef = os.popen("exiftool " + self.path + " |grep GPS\ Altitude\ Ref").read().strip("GPS\ Altitude\ Ref:")

         self.GPSLongitudeRef= os.popen("exiftool " + self.path + "|grep GPS\ Longitude\ Ref").read().strip("GPS\ Longitude\ Ref:")

         self.GPSDateStamp = os.popen("exiftool " +  self.path + " |grep GPS\ Date\ Stamp").read().strip("GPS\ Time\ Date:")

         self.GPSTimeStamp = os.popen("exiftool " +  self.path + " |grep GPS\ Time\ Stamp").read().strip("GPS\ Time\ Stamp:")

         self.GPSAltitude = os.popen("exiftool " +  self.path + "|grep GPS\ Altitude").read().strip("GPS\ Altitude:")

         self.GPSLatitude = os.popen("exiftool " + self.path +  " |grep GPS\ Latitude ").read().strip("GPS\ Latitude:")

         self.GPSLongitude = os.popen("exiftool " +  self.path + " |grep GPS\ Longitude").read().strip("GPS\ Longitude:")

         self.GPSPosition = os.popen("exiftool "+  self.path + " |grep GPS\ Position").read().strip("GPS\ Position:")


    def clean(self):
        command = "mat " + self.path
        system(command)



def Test():
    print("esto ya funciona")







#para borrar los metadatos de los JPG y de los PNG puedo usar el metadata cleaner MAT
#Me falta borrar los datos del PDF y armar el esquema de la base de datos
