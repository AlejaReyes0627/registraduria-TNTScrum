from Modelos.Resultado import Resultado
from Modelos.Estudiante import Estudiante
from Modelos.Materia import Materia
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Repositorios.RepositorioMateria import RepositorioMateria
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioEstudiantes = RepositorioEstudiante()
        self.repositorioMaterias = RepositorioMateria()
    def index(self):
        return self.repositorioResultado.findAll()
    '''Asignación de mesa y candidato a Resultado'''
    def create(self,infoResultado,numero_mesa,cedula_candidato):
        nuevoResultado=Resultado(infoResultado)
        infoResultado=Resultado(self.repositorioResultado.findById(id))
        laMesa=Mesa(self.repositorioMesa.findById(numero_mesa))
        elCandidato=Candidato(self.repositorioCandidato.findById(cedula_candidato))
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
        elResultado = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        laInscripcion.estudiante = elEstudiante
        laInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(laInscripcion)
    def delete(self, id):
        return self.repositorioInscripcion.delete(id)'''