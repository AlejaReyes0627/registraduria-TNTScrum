"""
Importación de las clases InterfaceRepositorio Y Modelo Candidatos
"""
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Candidatos import Candidatos

"""
Clase repositorio que hereda de la interfaz que lleva a cabo la asignación de la colección y resultados de los JSON
"""
class RepositorioCandidatos(InterfaceRepositorio[Candidatos]):
    pass