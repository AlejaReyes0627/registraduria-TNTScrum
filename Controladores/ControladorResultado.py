"""
Importación de las clases Respositorios y Modelos
"""

from Modelos.Resultado import Resultado
from Modelos.Mesas import Mesas
from Modelos.Candidatos import Candidatos
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioCandidatos import RepositorioCandidatos

"""
Clase controladora que administra los métodos del modelo a la base de datos
"""
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesas = RepositorioMesas()
        self.repositorioCandidatos = RepositorioCandidatos()

    """
    Método para hacer un GETALL
    @return método para encontrar todos los Resultados
    """
    def index(self):
        return self.repositorioResultado.findAll()
    '''Asignación de mesa y candidato a Resultado'''
    def create(self,infoResultado,numero_mesa,cedula_candidato):
        nuevoResultado=Resultado(infoResultado)
        laMesa=Mesas(self.repositorioMesas.findById(numero_mesa))
        elCandidato=Candidatos(self.repositorioCandidatos.findById(cedula_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    """
    Método que hace un GETBYID 
    @param id: id de los Resultados impuesto por defecto en mongo
    @return método para encontrar el Resultado por su Id
    """
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    '''def update(self,id,infoResultado,numero_mesa,cedula_candidato):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.año=infoInscripcion["año"]
        elResultado.semestre = infoInscripcion["semestre"]
        elResultado.notaFinal=infoInscripcion["nota_final"]
        elResultado = Mesas(self.repositorioMesass.findById(id_Mesas))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        laInscripcion.Mesas = elMesas
        laInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(laInscripcion)
    def delete(self, id):
        return self.repositorioInscripcion.delete(id)'''