"""
Importación de las clases RespositorioCandidatos y Modelo de Candidatos 
"""
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos

"""
Clase controladora que administra los métodos del modelo a la base de datos
"""
class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidatos()
        
    """
    Método para hacer un GETALL
    """
    def index(self):
        return self.repositorioCandidato.findAll()
    
    """
    Método que hace un POST 
    @param infoCandidato: información del candidato
    """
    def create(self,infoCandidato):
        nuevoCandidato=Candidatos(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    
    """
    Método que hace un GETBYID 
    @param id: id del candidato impuesto por defecto en mongo
    """
    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    
    """
    Método que hace un PUT
    @param infoCandidato: información del candidato
    @param id: id del candidato impuesto por defecto en mongo
    """
    def update(self,id,infoCandidato):
        CandidatoActual=Candidatos(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula=infoCandidato["cedula"]
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        CandidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        CandidatoActual.partido_candidato = infoCandidato["partido_candidato"]
        return self.repositorioCandidato.save(CandidatoActual)
    
    """
    Método que hace un DELETE
    @param id: id del candidato impuesto por defecto en mongo
    """
    def delete(self,id):
        return self.repositorioCandidato.delete(id)