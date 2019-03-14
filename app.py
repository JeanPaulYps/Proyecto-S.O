from flask import Flask, render_template,redirect,request, session, url_for
from pathlib import Path
import os, funcionalidades, manejoRutas

app = Flask(__name__)
@app.route('/')
def inicio():
    return redirect("/tree/", code = 302)

@app.route('/tree/<path:directorio>')
def hello_world(directorio):
    direccion = manejoRutas.getDireccionAbsoluta(directorio)
    contenidoCarpeta = funcionalidades.getArchivos(directorio)
    archivos = contenidoCarpeta[0]
    directorios = contenidoCarpeta[1]

    return render_template('main.html', arch = archivos, directorios = directorios, ruta = directorio)


@app.route('/tree/')
def otro():
    direccion = manejoRutas.getDireccionAbsoluta("")
    contenidoCarpeta = funcionalidades.getArchivos(direccion)
    archivos = contenidoCarpeta[0]
    directorios = contenidoCarpeta[1]
    return render_template('main.html', arch = archivos, directorios = directorios, ruta = "")


#borrar?ruta=C:\Users\Jean Paul\Desktop\holi.txt
@app.route('/borrar')
def borrar ():
    rutaRelativa= str(request.args.get("ruta"))
    rutaRelativa =rutaRelativa[5:]
    rutaAbsoluta = manejoRutas.getDireccionAbsoluta(rutaRelativa)
    print(rutaAbsoluta)
    if os.path.isfile(rutaAbsoluta):
        funcionalidades.borrarArchivo(rutaAbsoluta)
    else:
        funcionalidades.borrarCarpeta(rutaAbsoluta)
    return otro()
   
#un cambio xd
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
@app.route('/cambiarNombre/<path:directorio>', methods = ['POST', 'GET'])
def cambiarNombre(directorio):
    if request.method == "GET":
        direccion = manejoRutas.getDireccionAbsoluta(directorio)
        contenidoCarpeta = funcionalidades.getArchivos(directorio)
        archivos = contenidoCarpeta[0]
        directorios = contenidoCarpeta[1]
        return render_template('nombre.html', arch= archivos,directorios = directorios, ruta = directorio)
    
    if request.method == "POST":
        seleccion = request.form["seleccion"]
        nuevoNombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta(directorio)
        rutaAbsolutaConArchivo = manejoRutas.unirDireccion(rutaAbsoluta, seleccion)
        funcionalidades.cambiarNombre(rutaAbsolutaConArchivo,nuevoNombre)
        return redirect(url_for('hello_world', directorio = directorio))

@app.route('/cambiarNombre/', methods = ['POST', 'GET'])
def cambiarNombre2():
    if request.method == 'GET':
        direccion = manejoRutas.getDireccionAbsoluta("")
        contenidoCarpeta = funcionalidades.getArchivos(direccion)
        archivos = contenidoCarpeta[0]
        directorios = contenidoCarpeta[1]
        return render_template('nombre.html', arch= archivos,directorios = directorios )

    if request.method == 'POST':
        seleccion = request.form["seleccion"]
        nuevoNombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta("")
        rutaAbsolutaConArchivo = manejoRutas.unirDireccion(rutaAbsoluta, seleccion)
        funcionalidades.cambiarNombre(rutaAbsolutaConArchivo,nuevoNombre)
        return redirect(url_for('inicio'))

@app.route('/cambiarPermisos2/<path:directorio>', methods = ['POST', 'GET'])
def cambiarPermisos(directorio): # Configurar todo  con los permisos
    if request.method == "GET":
        direccion = manejoRutas.getDireccionAbsoluta(directorio)
        contenidoCarpeta = funcionalidades.getArchivos(directorio)
        archivos = contenidoCarpeta[0]
        directorios = contenidoCarpeta[1]
        return render_template('permisos.html', arch= archivos,directorios = directorios, ruta = directorio)
    
    if request.method == "POST":
        seleccion = request.form["seleccion"]
        nuevoNombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta(directorio)
        rutaAbsolutaConArchivo = manejoRutas.unirDireccion(rutaAbsoluta, seleccion)
        funcionalidades.cambiarPermisos(rutaAbsolutaConArchivo,nuevoNombre)
        return redirect(url_for('hello_world', directorio = directorio))

@app.route('/cambiarPermisos/', methods = ['POST', 'GET'])
def cambiarPermisos2():
    if request.method == 'GET':
        direccion = manejoRutas.getDireccionAbsoluta("")
        contenidoCarpeta = funcionalidades.getArchivos(direccion)
        archivos = contenidoCarpeta[0]
        directorios = contenidoCarpeta[1]
        return render_template('permisos.html', arch= archivos,directorios = directorios )

    if request.method == 'POST':
        seleccion = request.form["seleccion"]
        nuevoNombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta("")
        rutaAbsolutaConArchivo = manejoRutas.unirDireccion(rutaAbsoluta, seleccion)
        funcionalidades.cambiarNombre(rutaAbsolutaConArchivo,nuevoNombre)
        return redirect(url_for('inicio'))