from flask import Flask, render_template
from pathlib import Path
import os

app = Flask(__name__)

@app.route('/<directorio>')
def hello_world(directorio):
    direccion = os.getcwd()
    if not os.path.isfile(directorio):
        direccion = os.chdir(directorio)
    archivos = os.listdir(direccion)
    directorios = []
    arch = []
    for archivo in archivos:
        if os.path.isfile(archivo):
            arch.append(archivo)
        else:
            directorios.append(archivo)
    print(os.getcwd())
    print(arch)
    print(directorios)
    return render_template('main.html', arch = arch, directorios = directorios)

@app.route('/')
def inicio():
    os.chdir( str(Path.home()))
    direccion =  str(Path.home())
    archivos = os.listdir(direccion)
    directorios = []
    arch = []
    for archivo in archivos:
        if os.path.isfile(archivo):
            arch.append(archivo)
        else:
            directorios.append(archivo)    
    print(os.getcwd())
    return render_template('main.html', arch = arch, directorios = directorios)
