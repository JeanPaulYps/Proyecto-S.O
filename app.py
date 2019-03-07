from flask import Flask, render_template,redirect,request
from pathlib import Path
import os,funcionalidades

app = Flask(__name__)
@app.route('/')
def inicio():
    return redirect("/tree/", code = 302)

@app.route('/tree/<path:directorio>')
def hello_world(directorio):
    direccion = funcionalidades.getDireccionAbsoluta(directorio)
    archivos = os.listdir(direccion)
    directorios = []
    arch = []
    rutaRelativa = funcionalidades.getRutaRelativa(direccion)
    for archivo in archivos:
        if os.path.isfile(archivo):
            tupla = (funcionalidades.getLink(rutaRelativa, archivo), archivo)
            arch.append(tupla)
        else:
            tupla = (funcionalidades.getLink(rutaRelativa, archivo), archivo)
            directorios.append(tupla)
    return render_template('main.html', arch = arch, directorios = directorios)


@app.route('/tree/')
def otro():
    direccion = funcionalidades.getDireccionAbsoluta("")
    archivos = os.listdir(direccion)
    directorios = []
    arch = []
    rutaRelativa = funcionalidades.getRutaRelativa(direccion)
    for archivo in archivos:
        if os.path.isfile(archivo):
            tupla = (funcionalidades.getLink(rutaRelativa, archivo), archivo)
            arch.append(tupla)
        else:
            tupla = (funcionalidades.getLink(rutaRelativa, archivo), archivo)
            directorios.append(tupla)
    return render_template('main.html', arch = arch, directorios = directorios)


#borrar?ruta=C:\Users\Jean Paul\Desktop\holi.txt
@app.route('/borrar')
def borrar ():
    ruta = str(request.args.get("ruta"))
    print(ruta)
    if os.path.isfile(ruta):
        funcionalidades.borrarArchivo(ruta)
    else:
        funcionalidades.borrarCarpeta(ruta)
    return "archivo borrado"

#copiar?origen=C:\Users\Jean Paul\Desktop\archivo.txt&destino=C:\Users\Jean Paul\Desktop\destino
@app.route('/copiar')
def copiar():
    origen = str(request.args.get("origen"))
    destino = str(request.args.get("destino"))
    print(origen)
    print(destino)
    if os.path.isfile(origen):
        funcionalidades.copiarArchivo(origen,destino)
    else:
        funcionalidades.copiarCarpeta(origen,destino)
    return "archivo copiado"

#crearCarpeta?direccion=C:\Users\Jean Paul\Desktop&nombre=PruebaDeFuncion
@app.route('/crearCarpeta')
def crearCarpeta():
    direccion = str(request.args.get("direccion"))
    nombre = str(request.args.get("nombre"))
    
    funcionalidades.crearCarpeta(direccion,nombre)
    return "carpeta creada"
#crearArchivo?direccion=C:\Users\Jean Paul\Desktop&nombre=ArchivoDePrueba.txt
@app.route('/crearArchivo')
def crearArchivo():
    direccion = str(request.args.get("direccion"))
    nombre = str(request.args.get("nombre"))
    print(direccion)
    print(nombre)
    print(funcionalidades.crearArchivo(direccion,nombre))
    return "archivo creado"

#cambiarNombre?archivo=C:\Users\Jean Paul\Desktop\ArchivoDePrueba.txt&nombre=holi.txt
@app.route('/cambiarNombre')
def cambiarNombre():
    archivo = str(request.args.get("archivo"))
    nombre = str(request.args.get("nombre"))
    print(archivo)
    print(nombre)
    print(funcionalidades.cambiarNombre(archivo,nombre))
    return "nombre cambiado"