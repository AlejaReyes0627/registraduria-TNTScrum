"""
Importación de las clases InterfaceRepositorio Y Modelo Resultados
"""
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

"""
Clase repositorio que hereda de la interfaz que lleva a cabo la asignación de la colección y resultados de los JSON
"""
class RepositorioResultado(InterfaceRepositorio[Resultado]):
    pass