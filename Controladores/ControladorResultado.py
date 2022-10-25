from Modelos.Resultado import Resultado
from Modelos.Mesas import Mesas
from Modelos.Candidatos import Candidatos
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesas = RepositorioMesas()
        self.repositorioCandidatos = RepositorioCandidatos()
    def index(self):
        return self.repositorioResultado.findAll()
    '''Asignación de mesa y candidato a Resultado'''
    def create(self,infoResultado,numero_mesa,cedula_candidato):
        nuevoResultado=Resultado(infoResultado)
        infoResultado=Resultado(self.repositorioResultado.findById(id))
        laMesa=Mesas(self.repositorioMesa.findById(numero_mesa))
        elCandidato=Candidatos(self.repositorioCandidato.findById(cedula_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_votos=infoResultado["numero_votos"]
        return self.repositorioResultado.save(nuevoResultado)
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