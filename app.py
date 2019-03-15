from flask import Flask, render_template,redirect,request, session, url_for
from pathlib import Path
import os, funcionalidades, manejoRutas

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
    absolutaPadre = manejoRutas.getDireccionPadre(rutaAbsoluta)
    relativaPadre = manejoRutas.getDireccionRelativa(absolutaPadre)
    if relativaPadre != "":
        return redirect(url_for('hello_world', directorio = relativaPadre))
    else:
        return redirect(url_for('otro'))

   
#un cambio xd
#copiar?origen=C:\Users\Jean Paul\Desktop\archivo.txt&destino=C:\Users\Jean Paul\Desktop\destino
@app.route('/copiar/<path:directorio>', methods = ['POST'])
def copiar(directorio):
    if request.method == "POST":
        nombre = request.form["nombre"]
        session["origenElemento"] =manejoRutas.unirDireccion(manejoRutas.getDireccionAbsoluta(directorio), nombre)
        return redirect(url_for('hello_world', directorio = directorio))

@app.route('/copiar/', methods = ['POST'])
def copiar2():
    if request.method == "POST":
        nombre = request.form["nombre"]
        session["origenElemento"] = manejoRutas.unirDireccion( manejoRutas.getDireccionAbsoluta(""), nombre)
        return redirect(url_for('otro'))

@app.route('/pegar/<path:directorio>', methods = ['POST'])
def pegar(directorio):
    if request.method == "POST":
        origen = session["origenElemento"]
        destino = manejoRutas.getDireccionAbsoluta(directorio)
        if os.path.isfile(origen):
            funcionalidades.copiarArchivo(origen,destino)
        else:
            funcionalidades.copiarCarpeta(origen,destino)
        del session["origenElemento"]
        return redirect(url_for('hello_world', directorio = directorio))

@app.route('/pegar/', methods = ['POST'])
def pegar2():
    if request.method == "POST":
        origen = session["origenElemento"]
        destino = manejoRutas.getDireccionAbsoluta("")
        if os.path.isfile(origen):
            funcionalidades.copiarArchivo(origen,destino)
        else:
            funcionalidades.copiarCarpeta(origen,destino)
        del session["origenElemento"]
        return redirect(url_for('otro'))

#crearCarpeta?direccion=C:\Users\Jean Paul\Desktop&nombre=PruebaDeFuncion
@app.route('/crearCarpeta/<path:directorio>', methods = ['POST'])
def crearCarpeta(directorio):
    if request.method == "POST":  
        nombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta(directorio)
        print(funcionalidades.crearCarpeta(rutaAbsoluta,nombre))
        return redirect(url_for('hello_world', directorio = directorio))

@app.route('/crearCarpeta/', methods = ['POST'])
def crearCarpeta2():
    if request.method == "POST":  
        nombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta("")
        print(funcionalidades.crearCarpeta(rutaAbsoluta,nombre))
        return redirect(url_for('otro'))    

#crearArchivo?direccion=C:\Users\Jean Paul\Desktop&nombre=ArchivoDePrueba.txt
@app.route('/crearArchivo/<path:directorio>', methods = ['POST'])
def crearArchivo(directorio):
    if request.method == "POST":  
        nombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta(directorio)
        print(funcionalidades.crearArchivo(rutaAbsoluta,nombre))
        return redirect(url_for('hello_world', directorio = directorio))

@app.route('/crearArchivo/', methods = ['POST'])
def crearArchivo2():
    if request.method == "POST":  
        nombre = request.form["nuevoNombre"]
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta("")
        print(funcionalidades.crearArchivo(rutaAbsoluta,nombre))
        return redirect(url_for('otro'))


#cambiarNombre?archivo=C:\Users\Jean Paul\Desktop\ArchivoDePrueba.txt&nombre=holi.txt
@app.route('/cambiarNombre/<path:directorio>', methods = ['POST', 'GET'])
def cambiarNombre(directorio):
    if request.method == "GET":
        direccion = manejoRutas.getDireccionAbsoluta(directorio)
        contenidoCarpeta = funcionalidades.getArchivos(directorio)
        archivos = contenidoCarpeta[0]
        directorios = contenidoCarpeta[1]
        return render_template('nombre.html', arch= archivos, directorios = directorios, ruta = directorio)
    
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

@app.route('/cambiarPermisos/<path:directorio>', methods = ['POST', 'GET'])
def cambiarPermisos(directorio): # Configurar todo  con los permisos
    if request.method == "GET":
        direccion = manejoRutas.getDireccionAbsoluta(directorio)
        contenidoCarpeta = funcionalidades.getArchivos(directorio)
        archivos = contenidoCarpeta[0]
        directorios = contenidoCarpeta[1]
        return render_template('permisos.html', arch= archivos, directorios = directorios, ruta = directorio)
    
    if request.method == "POST":
        permisos = request.form["permisos"]
        uRead = request.form["uread"]
        print(uRead +"hola" )
        uWrite = request.form["uwrite"]
        uExecute = request.form["uexecute"]
        userPermisos= int(uRead)+int(uWrite)+int(uExecute)
        gRead = request.form["gread"]
        gWrite = request.form["gwrite"]
        gExecute = request.form["gexecute"]
        groupPermisos= int(gRead)+int(gWrite)+int(gExecute)
        oRead = request.form["oread"]
        oWrite = request.form["owrite"]
        oExecute = request.form["oexecute"]
        otherPermisos= int(oRead)+int(oWrite)+int(oExecute)
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta(directorio)
        rutaAbsolutaConArchivo = manejoRutas.unirDireccion(rutaAbsoluta, permisos)
        print(str("0o"+str(userPermisos)+str(groupPermisos)+str(otherPermisos)))
        funcionalidades.cambiarPermisos(rutaAbsolutaConArchivo,str("0o"+str(userPermisos)+str(groupPermisos)+str(otherPermisos)))
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
        permisos = request.form["permisos"]
        uRead = request.form["uread"]
        uWrite = request.form["uwrite"]
        uExecute = request.form["uexecute"]
        userPermisos= int(uRead)+int(uWrite)+int(uExecute)
        gRead = request.form["gread"]
        gWrite = request.form["gwrite"]
        gExecute = request.form["gexecute"]
        groupPermisos= int(gRead)+int(gWrite)+int(gExecute)
        oRead = request.form["oread"]
        oWrite = request.form["owrite"]
        oExecute = request.form["oexecute"]
        otherPermisos= int(oRead)+int(oWrite)+int(oExecute)
        rutaAbsoluta = manejoRutas.getDireccionAbsoluta("")
        rutaAbsolutaConArchivo = manejoRutas.unirDireccion(rutaAbsoluta, permisos)
        print(str("0o"+str(userPermisos)+str(groupPermisos)+str(otherPermisos)))
        funcionalidades.cambiarPermisos(rutaAbsolutaConArchivo,str("0o"+str(userPermisos)+str(groupPermisos)+str(otherPermisos)))
        return redirect(url_for('inicio'))
