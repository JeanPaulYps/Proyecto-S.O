import os,shutil,manejoRutas
from pathlib import Path, PurePath


#//---------------------------------------------
#Operaciones no validas para carpetas y archivos

def borrarArchivo (ruta):
    try:
        os.remove(ruta)
        return "Archivo encontrado"
    except OSError:
        return "Archivo no encontrado"

def borrarCarpeta (ruta):
    try:
        os.rmdir(ruta)
        return "Archivo encontrado"
    except OSError:
        return "Archivo no encontrado"

def copiarArchivo (rutaOrigen, rutaDestino):
    try:
        shutil.copy2(rutaOrigen,rutaDestino)
        return "Archivo copiado"
    except OSError:
        return "Archivo no enocontrado"

#Para copiar la carpeta, la carpeta de destino no debe existir
def copiarCarpeta(rutaOrigen, rutaDestino):

    try:
        shutil.copytree(rutaOrigen,rutaDestino)
        return "Carpeta copiada"
    except OSError:
        return "Carpeta no ha sido copiada"
        
        
def crearArchivo(direccion, nombre):
    try:
        archivo = open(manejoRutas.unirDireccion(direccion,nombre), 'w')
        archivo.close()
        return "Archivo Creado"
    except OSError:
        return "No se pudo crear archivo"

def crearCarpeta(direccion,nombre):
    try:
        carpeta = os.mkdir(manejoRutas.unirDireccion(direccion,nombre))
        return "Carpeta creada"
    except OSError:
        return "No se pudo crear carpeta"

#//------------------------------------------
#Operaciones validas para carpetas y archivos 

def cambiarPermisos (archivo,codigo):
    try:
        os.chmod(archivo,int(codigo,8))
        print("\nPermisos cambiados\n")
    except OSError:
        print("ERROR archivo no encontrado\n")

def cambiarNombre(archivo,nuevoNombre):
    try:
        nombre = manejoRutas.getDireccionPadre(archivo)
        nombre = manejoRutas.unirDireccion(nombre, nuevoNombre)
        os.rename(archivo,nombre)
        return "Nombre cambiado"
    except OSError:
        return "Nombre no ha sido cambiado"
    
def getArchivos(direccion):
    direccionAbsoluta = manejoRutas.getDireccionAbsoluta(direccion)
    direccionRelativa = manejoRutas.getDireccionRelativa(direccionAbsoluta)
    carpetas = []
    archivos = []
    for archivo in os.listdir(direccionAbsoluta):
        rutaArchivo = os.path.join(direccionAbsoluta, archivo)
        if os.path.isfile(rutaArchivo):
            tupla = (manejoRutas.getLink(direccionRelativa, archivo), archivo)
            archivos.append(tupla)
        elif os.path.isdir(rutaArchivo):
            tupla = (manejoRutas.getLink(direccionRelativa, archivo), archivo)
            carpetas.append(tupla)
        else:
            tupla = (manejoRutas.getLink(direccionRelativa, archivo), archivo)
            archivos.append(tupla)
    return (archivos,carpetas)
