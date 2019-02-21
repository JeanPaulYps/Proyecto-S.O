from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    direccion = os.getcwd()
    direccion = os.chdir("..")
    archivos = os.listdir(direccion)
    directorios = []
    arch = []
    for archivo in os.listdir(direccion):
        if os.path.isfile(archivo):
            arch.append(archivo)
        else:
            directorios.append(archivo)
    
    print(arch)
    print(directorios)
    return render_template('main.html', arch = arch, directorios = directorios)