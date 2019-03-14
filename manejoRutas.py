import os
from pathlib import Path, PurePath

def getDireccionAbsoluta (direccionRelativa):
    return str(os.path.join(Path.home(), Path(direccionRelativa) ) )

#La direccion es relativa con respecto a la carpeta de usuario
def getDireccionRelativa(directorio):
    return str(PurePath.relative_to(Path(directorio), Path.home() ) )

def getLink(directorio, nombre):
    return  os.path.join("tree", os.path.join(directorio, Path(nombre) ) ) 

def unirDireccion(ruta, nombreArchivo):
    return str(os.path.join(ruta,nombreArchivo))

def getDireccionPadre(directorio):
    directorio = PurePath(directorio)
    return str(directorio.parent)