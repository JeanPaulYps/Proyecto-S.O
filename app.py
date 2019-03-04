from flask import Flask, render_template,redirect
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
