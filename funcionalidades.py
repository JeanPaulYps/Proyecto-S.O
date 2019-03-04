import os,shutil

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
        archivo = open(nombre, 'w')
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
    
