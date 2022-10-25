from Modelos.Partidos import Partidos
from Repositorios.RepositorioPartidos import RepositorioPartidos
class ControladorPartidos():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()
    def index(self):
        return self.repositorioPartidos.findAll()
    def create(self,infoPartidos):
        nuevoPartido=Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevoPartido)
    def show(self,id):
        elPartido=Partidos(self.repositorioPartidos.findById(id))
        return elPartido.__dict__
    def update(self,id,infoPartidos):
        partidoActual=Partidos(self.repositorioPartidos.findById(id))
        partidoActual.nombre=infoPartidos["nombre"]
        partidoActual.lema= infoPartidos["lema"]
        return self.repositorioPartidos.save(partidoActual)
    def delete(self,id):
        return self.repositorioPartidos.delete(id)