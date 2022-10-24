from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos

class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidatos()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidatos(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        CandidatoActual=Candidatos(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula=infoCandidato["cedula"]
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        CandidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        CandidatoActual.partido_candidato = infoCandidato["partido_candidato"]
        return self.repositorioCandidato.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)