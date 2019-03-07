import os,shutil
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

def copiarCarpeta(rutaOrigen, rutaDestino):
    #La carpeta de destino no debe existir
    try:
        shutil.copytree(rutaOrigen,rutaDestino)
        return "Carpeta copiada"
    except OSError:
        return "Carpeta no ha sido copiada"
        
        
def crearArchivo(direccion, nombre):
    try:
        archivo = open(direccion + "\\" + nombre, 'w')
        archivo.close()
        return "Archivo Creado"
    except OSError:
        return "No se pudo crear archivo"

def crearCarpeta(direccion,nombre):
    try:
        #Cambiar \ en windows para  / en Linux
        carpeta = os.mkdir(direccion + "\\" + nombre)
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
        #Cambiar \ de windows, / para linux
        nombre = archivo.split("\\")
        nombre[-1] = nuevoNombre
        nombre = "\\".join(nombre)
        os.rename(archivo,nombre)
        return "Nombre cambiado"
    except OSError:
        return "Nombre no ha sido cambiado"
    
#-------------------------------------------
#Manejo de direcciones

def getDireccionAbsoluta (direccionRelativa):
    return str(os.path.join(Path.home(), Path(direccionRelativa)))

#La direccion es relativa con respecto a la carpeta de usuario
def getRutaRelativa(directorio):
    return str(PurePath.relative_to(Path(directorio), Path.home()))

def getLink(directorio, nombre):
    return  os.path.join("tree", os.path.join(directorio, Path(nombre) ) ) 