from flask import Flask, render_template, request , send_file
from werkzeug.utils import secure_filename
from extractor import *
from queries import *

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template('index.html'))

@app.route("/pdf/")
def pdf():
    return(render_template("pdf.html"))

#finished!
@app.route("/pdf/descargarpdf" , methods = ["GET" , "POST"])
def descargarpdf():
    if(request.method == 'POST'):
        f = request.files['file']
        newname = f.filename.replace(" " , "")
        pdfname = newname
        f.save(secure_filename( newname))
        pdf = archivoPDF(newname)
        pdf.DefMetadata()
        pdfname = newname
        global pdfname

        #arreglando el cration date
        firstDate = str(pdf.CreationDate)
        firstDate = firstDate.replace("'" , " ")
        #arreglando el ModDate
        secondDate = str(pdf.ModDate)
        secondDate = secondDate.replace("'", " ")
        insertPdf(pdf.nombrearchivo  ,firstDate , pdf.FullBanner, pdf.Trapped , secondDate, pdf.Producer)
        pdf.clean()
        print("el error es \n \n \n " , firstDate, type(pdf.ModDate))
        return (render_template("devolverpdf.html"))
    else:
        return(request.method)

@app.route("/pdf/devolverpdf")
def devolverpdf():
    return(send_file(pdfname))

@app.route("/jpg/")
def jpg():
    return(render_template("jpg.html"))

@app.route("/jpg/descargarjpg" , methods = ["GET" , "POST"])
def descargarjpg():
    if(request.method == 'POST'):
        f = request.files['file']
        newname = f.filename.replace(" " , "")
        global jpgname
        jpgname = newname
        f.save(secure_filename(newname))
        imagenjpg = ImagenJPG(newname)
        imagenjpg.DefMetadata()
        insertJPG(imagenjpg.path , str(imagenjpg.ModTime) , str(imagenjpg.Camera) , str(imagenjpg.Flash) , str(imagenjpg.GPSLatitudeRef), str(imagenjpg.GPSAltitudeRef) , (imagenjpg.GPSLongitudeRef) , imagenjpg.GPSDateStamp , imagenjpg.GPSTimeStamp , imagenjpg.GPSAltitude , str(imagenjpg.GPSLatitude).replace(" ", "").replace('"', "").replace("'", "").replace("\n",""), str(imagenjpg.GPSLongitude).replace(" ", "").replace('"', "").replace("'", "").replace("\n","")  , str(imagenjpg.GPSPosition).replace(" ", "").replace('"', "").replace("'", "").replace("\n",""))

        imagenjpg.clean()

        return(render_template("devolverjpg.html"))
    else:
        return(request.method)


@app.route("/jpg/devolverjpg")
def devolverjpg():
    #si quisiera que el cliente la descargara facil podria comprimirla, pero no se si tenga sentido
    return(send_file(jpgname))



@app.route("/png/")
def png():
    return(render_template("png.html"))


@app.route("/png/descargarpng" , methods = ["GET" , "POST"])
def descargarPNG():
    if(request.method == 'POST'):
        f = request.files['file']
        newfilename = f.filename.replace(" " , "")#esto es para poder agarrar el path sin compliques
        print("new filename :"+ newfilename)
        f.save(secure_filename(newfilename))
        imagenpng = ImagenPNG(newfilename)
        global pngname
        pngname = newfilename
        imagenpng.DefMetadata()
        pngname = newfilename
        #ver si es necesario arreglar el moddate
        insertPNG( imagenpng.path ,imagenpng.ModTime , imagenpng.accessTime , imagenpng.Megapixels ,str(imagenpng.ColorType) , str(imagenpng.ImageSize) )
        imagenpng.clean()
        return (render_template("devolverpng.html"))
    else:
        return(request.method)


@app.route("/png/devolverpng")
def devolverpng():
    #si quisiera que el cliente la descargara facil podria comprimirla, pero no se si tenga sentido
    return(send_file(pngname))


app.run( debug = True) # aca puedo poner el puerto que se me de la gana
