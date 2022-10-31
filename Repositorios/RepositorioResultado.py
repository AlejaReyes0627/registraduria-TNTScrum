"""
Importación de las clases InterfaceRepositorio Y Modelo Resultados
"""
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId
"""
Clase repositorio que hereda de la interfaz que lleva a cabo la asignación de la colección y resultados de los JSON
"""
class RepositorioResultado(InterfaceRepositorio[Resultado]):
        def getMayorNotaPorVotos(self):
            query1={
            "$group":
                {
                    "_id": "$resultado",
                    "max": {
                        "$max": "$numero_votos"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
            pipeline= [query1]
            return self.queryAggregation(pipeline)